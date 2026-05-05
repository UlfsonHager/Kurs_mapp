""" Detta är en Streamlit-app som låter användaren rita en siffra (0-9) på en canvas och sedan 
använder en maskininlärningsmodell tränad på MNIST-databasen för att gissa vilken siffra det är. 
Vi använder en ExtraTreesClassifier som har tränats på hela MNIST-databasen för att uppnå hög 
noggrannhet enligt tidigare utvärdering.
Appen visar också sannolikheten för varje siffra och exempelbilder 
från MNIST-databasen som matchar den gissade siffran."""

# Importera nödvändiga bibliotek
import numpy as np
import streamlit as st
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import ExtraTreesClassifier
from PIL import Image
from streamlit_drawable_canvas import st_canvas
from scipy.ndimage import center_of_mass, shift

# ── INIT (körs bara en gång tack vare @st.cache_resource) ────────────────────
# cache_resource håller modellen i minnet mellan Streamlit-omladdningar så att
# vi slipper träna om vid varje interaktion.

@st.cache_resource
def init_model(show_spinner=False):
    st.spinner("Laddar MNIST-data... (detta sker bara en gång)")
    X_raw, y_raw = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)

    # Tränar på hela MNIST (70 000 bilder) utan train/test-split eftersom modellen
    # redan är utvärderad i EDA-notebooken och vi vill maximal träningsdata i produktion.
    scaler = StandardScaler()
    X_raw_scaled = scaler.fit_transform(X_raw).astype(np.float32)

    # Bästa hyperparametrar från GridSearchCV i EDA-notebooken
    model = ExtraTreesClassifier(max_depth=None, min_samples_split=2, n_estimators=200, max_features='sqrt',
                                  random_state=42, n_jobs=-1)
    model.fit(X_raw_scaled, y_raw)

    acc = 0.97  # Uppmätt på separat testset i EDA-notebooken
    return model, X_raw, y_raw, acc, scaler

model, X_raw, y_raw, accuracy, scaler = init_model()


# BILDHANTERING & PREDIKTION



def predict_digit(img_array):
    """Omvandlar en ritad canvas-bild (280x280 RGBA) till MNIST-format och returnerar
    den bearbetade bilden samt sannolikheter för siffrorna 0-9."""
    if isinstance(img_array, np.ndarray) and len(img_array.shape) == 3:

        # Steg 1: Konvertera RGBA → gråskala och invertera färger.
        # Canvas har vit bakgrund / svart penna — MNIST har svart bakgrund / vita siffror.
        img_gray = np.mean(img_array[:, :, :3], axis=2).astype(np.uint8)
        img_gray = 255 - img_gray
        img_pil = Image.fromarray(img_gray)

        # Steg 2: Beskär bort tom bakgrund runt siffran så att siffran fyller bilden.
        bbox = img_pil.getbbox()
        if bbox:
            img_pil = img_pil.crop(bbox)

        # Steg 3: Skala till max 20x20 px med bibehållen proportioner.
        # MNIST-spec anger att siffran ska uppta ett 20x20-område inuti 28x28-rutan.
        w, h = img_pil.size
        ratio = 20.0 / max(w, h)
        img_20 = img_pil.resize((int(w * ratio), int(h * ratio)), Image.Resampling.LANCZOS)

        # Steg 4: Klistra in siffran centrerad på en svart 28x28-canvas.
        canvas = Image.new('L', (28, 28), 0)
        w20, h20 = img_20.size
        canvas.paste(img_20, ((28 - w20) // 2, (28 - h20) // 2))

        # Steg 5: Masscentrum-justering — flyttar siffran så att dess tyngdpunkt
        # hamnar exakt i mitten (13.5, 13.5). MNIST-bilderna är preparerade på samma
        # sätt, så detta minskar skillnaden mellan tränings- och prediktionsdata.
        img_np = np.array(canvas).astype(np.float32)
        cy, cx = center_of_mass(img_np)
        if not np.isnan(cy) and not np.isnan(cx):
            img_np = shift(img_np, [13.5 - cy, 13.5 - cx])

        # shift() kan ge pixelvärden utanför 0-255 — klippa till giltigt intervall.
        img_final_np = np.clip(img_np, 0, 255).astype(np.uint8)

        # Steg 6: Platta ut till 784 värden, skala med samma scaler som modellen tränades på.
        final_input_scaled = scaler.transform(img_final_np.reshape(1, 784))

        # Returnera sannolikheter per siffra som dict {"0": 0.02, "1": 0.95, ...}
        probs = model.predict_proba(final_input_scaled)[0]
        label_output = {str(i): float(probs[i]) for i in range(10)}

        return img_final_np, label_output

    return None, {}
   

# ── GRÄNSSNITT ────────────────────────────────────────────────────────────────

st.set_page_config(page_title="MNIST Labration", layout="centered")
st.title("Siffer-igenkänning")
st.caption(f"Modellens noggrannhet: {accuracy:.2%}")

# Tre kolumner: rityta | bearbetad bild | analysresultat
col1, col2, col3 = st.columns([2, 1, 1.5])

with col1:
    stroke_width = st.sidebar.slider("Pen storlek: ", 1, 25, 15)
    st.sidebar.markdown("---")
    st.sidebar.subheader("Siffror från MNIST-databasen")
    digit_to_show = st.sidebar.selectbox("Välj en siffra att granska:", range(10))

    # Så man kan se hur siffrorna ser ut i träningsdata och få en känsla för variationen. Visar 5 slumpmässiga exempel varje gång
    if st.sidebar.button(f"Visa exempel på {digit_to_show}"):
        digit_indices = np.where(y_raw.astype(str) == str(digit_to_show))[0]
        # Slumpar 5 exempel för variation vid upprepade klick
        sample_indices = np.random.choice(digit_indices, 5, replace=False)
        st.sidebar.write(f"Exempel på {digit_to_show}:or:")
        side_cols = st.sidebar.columns(5)
        for i, idx in enumerate(sample_indices):
            with side_cols[i]:
                st.image(X_raw[idx].reshape(28, 28), width=60)

    # Canvasen där användaren ritar sin siffra
    st.markdown("### Rita en siffra (0-9)")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color="#000000",
        background_color="#FFFFFF",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
        update_streamlit=True  # Triggar prediktion direkt när musknappen/pennan lyfts
    )

# ── PREDIKTION ────────────────────────────────────────────────────────────────
# Kontrollerar att något faktiskt ritats (minst en pixel < 255 = inte helt vit canvas)
processed_img = None
predictions = None
if canvas_result.image_data is not None and np.any(canvas_result.image_data[:, :, :3] < 255):
    processed_img, predictions = predict_digit(canvas_result.image_data)

    with col2:
        st.markdown("### 2. Input")
        if processed_img is not None:
            st.image(processed_img, width=120, caption="AI-vy (28x28)")
        else:
            st.caption("Ingen bild bearbetad")

    with col3:
        st.markdown("### 3. Analys")
        if predictions: # Exekveras bara om predict_digit returnerade sannolikheter
            best_guess = max(predictions, key=predictions.get)
            confidence = predictions[best_guess]
            st.metric("Gissning", f"Siffra {best_guess}", f"{confidence:.1%}")
            st.bar_chart(predictions)

    # Galleri: visa de 10 första MNIST-bilderna som matchar modellens gissning
    st.markdown("---")
    st.subheader(f"Tolkat resultat som '{best_guess}:or' av modellen från MNIST-databasen")

    all_indices = np.where(y_raw.astype(str) == str(best_guess))[0]
    indices = all_indices[:10]

    if len(indices) > 0:
        img_cols = st.columns(5)
        for i, idx in enumerate(indices):
            with img_cols[i % 5]:
                st.image(X_raw[idx].reshape(28, 28), width=60)
    else:
        st.warning(f"Kunde inte hitta några referensbilder för siffra {best_guess}.")

else:
    with col3:
        st.info("Väntar på bilden...")