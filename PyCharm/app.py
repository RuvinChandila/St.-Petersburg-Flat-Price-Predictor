import streamlit as st
import pickle
import pandas as pd

# Page config
st.set_page_config(page_title="Flat Price Predictor", layout="wide")

# Load model
@st.cache_resource
def load_model():
    try:
        with open('flat_price_model_2026_full.pkl', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        st.error("❌ Model file 'flat_price_model_2026_full.pkl' not found.")
        return None
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

model = load_model()


# Constants
DISTRICT_OPTIONS = sorted(["Moskovskij", "Nevskij", "Kirovskij", "Krasnoselskij",
                           "Vyborgskij", "Centralnyj", "Petrogradskij"])

# Initialize session state FIRST (before any usage)
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'prediction' not in st.session_state:
    st.session_state.prediction = None
if 'input_summary' not in st.session_state:
    st.session_state.input_summary = {}

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

# Header
if not st.session_state.show_results:
    st.markdown("""
<div class="main-header">
    <div class="main-title"> St. Petersburg Flat Price Predictor</div>
</div>
""", unsafe_allow_html=True)

if model is None:
    st.warning("Model not found. Please ensure 'flat_price_model_2026_full.pkl' is in the same directory.")
    st.stop()

# Initialize session state
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'prediction' not in st.session_state:
    st.session_state.prediction = None
if 'input_summary' not in st.session_state:
    st.session_state.input_summary = {}

# Form Logic
if not st.session_state.show_results:

    with st.container(border=True):
        st.markdown("###  Space & Layout(m²)")
        c1, c2, c3, c4 = st.columns(4)
        kitchen_area = c1.number_input(
            "Kitchen Area", 7, 26, 15,
        )
        bath_area = c2.number_input(
            "Bathroom Area", 7, 36, 7,
        )
        other_area = c3.number_input(
            "Other Area (m²)", 11.0, 95.0, 35.0, 0.5,
        )
        extra_size = c4.number_input(
            "Extra Area", 0, 20, 5,
            help="Balcony/Loggia size (counts as 1/3 of living area)"
        )

        # CALCULATION OF TOTAL AREA
        total_area = kitchen_area + bath_area + other_area + (extra_size / 3)

        st.markdown(f"""
            <div class="total-area-box">
                <span style='color:#bed2e6; font-size: 1rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;'>Total Area</span><br>
                <span style='font-size: 2.5rem; font-weight: 900; color: #4facfe; letter-spacing: -1px;'>{total_area:.2f}</span>
                <span style='font-size: 1.5rem; font-weight: 600; color: #00f2fe;'> m²</span>
            </div>
        """, unsafe_allow_html=True)

        # Input validation
        if total_area < 20 or total_area > 300:
            st.warning("⚠️ Total area seems unusual. Please verify your inputs.")

        st.markdown("<br>", unsafe_allow_html=True)
        r1, r2 = st.columns([2, 1])
        with r1:
            rooms_count = st.select_slider(
                "Number of Rooms",
                options=list(range(0, 10)),
                value=2
            )
        with r2:
            bath_count = st.radio("Bathrooms", [1, 2], horizontal=True)

    with st.container(border=True):
        st.markdown("###  Building & Location")
        c1, c2, c3 = st.columns([0.4, 1, 1])
        district = c1.selectbox("District", DISTRICT_OPTIONS, index=0)
        year = c2.slider("Year Built", 1900, 2020, 2005)
        ceil_height = c3.slider("Ceiling Height (m)", 2.5, 5.0, 3.5, 0.1)

        c1, c2 = st.columns(2)
        floor_max = c1.slider("Total Floors in Building", 1, 25, 14)

        if floor_max > 1:
            floor = c2.slider(
                "Flat Floor",
                min_value=1,
                max_value=floor_max,
                value=min(8, floor_max)
            )
        else:
            floor = 1
            c2.info("Only 1 floor available.")

    with st.container(border=True):
        st.markdown("###  Utilities & Extras")

        col1, col2, col3 = st.columns(3)

        with col1:
            gas = st.toggle(" Gas", True)

        with col2:
            hot_water = st.toggle(" Hot Water", True)

        with col3:
            heating = st.toggle(" Central Heating", True)

        col4, col5 = st.columns(2)

        with col4:
            extra_count = st.number_input("Extra Count", 0, 2, 1)

        with col5:
            extra_type = st.segmented_control(
                "Extra Type",
                options=["balcony", "loggia"],
                default="balcony",
                key="extra_type_widget"
            )
            if extra_type is None:
                extra_type = "balcony"
            model_extra_type = (extra_type if extra_type else "balcony") if extra_count > 0 else "none"

    # Review inputs before calculation
    with st.expander(" Review Inputs"):
        st.write(f"**Total Area:** {total_area:.2f} m²")
        st.write(f"**Rooms:** {rooms_count} rooms, {bath_count} bathroom(s)")
        st.write(f"**Location:** {district}, Floor {floor}/{floor_max}")
        st.write(f"**Built:** {year} ({2026 - year} years old)")
        st.write(f"**Ceiling Height:** {ceil_height} m")
        utilities = []
        if gas:
            utilities.append("Gas")
        if hot_water:
            utilities.append("Hot Water")
        if heating:
            utilities.append("Central Heating")
        st.write(f"**Utilities:** {', '.join(utilities) if utilities else 'None'}")
        if extra_count > 0:
            st.write(f"**Extras:** {extra_count} {extra_type}(s)")

    if st.button(" Calculate Market Value", type="primary", use_container_width=True):
        data = {
            "kitchen_area": kitchen_area,
            "bath_area": bath_area,
            "other_area": other_area,
            "gas": "Yes" if gas else "No",
            "hot_water": "Yes" if hot_water else "No",
            "central_heating": "Yes" if heating else "No",
            "extra_area": extra_size,
            "extra_area_count": extra_count,
            "year": year,
            "ceil_height": ceil_height,
            "floor_max": floor_max,
            "floor": floor,
            "total_area": total_area,
            "bath_count": bath_count,
            "extra_area_type_name": extra_type,
            "district_name": district,
            "rooms_count": rooms_count,
        }

        df_input = pd.DataFrame([data])

        with st.spinner(" Analyzing market data..."):
            try:
                prediction = model.predict(df_input)[0]
                st.session_state.prediction = prediction
                st.session_state.input_summary = data
                st.session_state.show_results = True
                st.rerun()
            except Exception as e:
                st.error(f"❌ Prediction Error: {e}")

else:
    # Results View
    res = st.session_state.prediction
    inputs = st.session_state.input_summary

    with st.container(border=True):
        st.markdown("###  Estimated Market Value")
        st.markdown(f'<div class="price-display">{res:,.0f} ₽</div>', unsafe_allow_html=True)

        # Compact property summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Area", f"{inputs['total_area']:.0f} m²")
        with col2:
            st.metric("Price per m²", f"{res / inputs['total_area']:,.0f} ₽")
        with col3:
            st.metric("Building Age", f"{2026 - inputs['year']} yrs")

    if st.button(" New Calculation", use_container_width=True):
        st.session_state.show_results = False
        st.rerun()