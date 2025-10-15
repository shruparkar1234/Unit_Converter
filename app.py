import streamlit as st
st.title("Hello Streamlit 👋")
st.write("If you can see this page, Streamlit is installed correctly!")

# 🎯 App Title
st.set_page_config(page_title="Unit Converter", page_icon="🔄")
st.title("🔄 Unit Converter")
st.write("Easily convert between Temperature, Length, Volume, and Currency.")

# -------------------------
# Conversion Functions
# -------------------------
# 🌡️ Temperature
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# 📏 Length
def meters_to_centimeters(m):
    return m * 100

def centimeters_to_meters(cm):
    return cm / 100

# 🧴 Volume
def liters_to_milliliters(L):
    return L * 1000

def milliliters_to_liters(mL):
    return mL / 1000

# 💰 Currency
def usd_to_inr(usd, rate=83.0):
    return usd * rate

def inr_to_usd(inr, rate=83.0):
    return inr / rate

# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.header("Select Conversion Category")
category = st.sidebar.selectbox(
    "Choose one:",
    ["Temperature", "Length", "Volume", "Currency"]
)

# -------------------------
# Helper Function: Validate Input
# -------------------------
def get_numeric_input(label, unit=""):
    val = st.text_input(f"{label} {unit}")
    if val:
        try:
            return float(val)
        except ValueError:
            st.warning("⚠️ Please enter a valid number.")
            return None
    return None

# -------------------------
# Conversion Logic by Category
# -------------------------
if category == "Temperature":
    st.subheader("🌡️ Temperature Converter")
    direction = st.radio("Conversion Direction", ["Celsius ➡ Fahrenheit", "Fahrenheit ➡ Celsius"])
    
    unit_label = "°C" if "Celsius" in direction.split("➡")[0] else "°F"
    input_value = get_numeric_input("Enter value:", unit_label)
    
    if input_value is not None:
        if st.button("Convert"):
            if direction == "Celsius ➡ Fahrenheit":
                result = celsius_to_fahrenheit(input_value)
                st.success(f"{input_value:.2f} °C = {result:.2f} °F")
            else:
                result = fahrenheit_to_celsius(input_value)
                st.success(f"{input_value:.2f} °F = {result:.2f} °C")

elif category == "Length":
    st.subheader("📏 Length Converter")
    direction = st.radio("Conversion Direction", ["Meters ➡ Centimeters", "Centimeters ➡ Meters"])
    
    unit_label = "m" if "Meters" in direction.split("➡")[0] else "cm"
    input_value = get_numeric_input("Enter value:", unit_label)
    
    if input_value is not None:
        if st.button("Convert"):
            if direction == "Meters ➡ Centimeters":
                result = meters_to_centimeters(input_value)
                st.success(f"{input_value:.2f} m = {result:.2f} cm")
            else:
                result = centimeters_to_meters(input_value)
                st.success(f"{input_value:.2f} cm = {result:.2f} m")

elif category == "Volume":
    st.subheader("🧴 Volume Converter")
    direction = st.radio("Conversion Direction", ["Liters ➡ Milliliters", "Milliliters ➡ Liters"])
    
    unit_label = "L" if "Liters" in direction.split("➡")[0] else "mL"
    input_value = get_numeric_input("Enter value:", unit_label)
    
    if input_value is not None:
        if st.button("Convert"):
            if direction == "Liters ➡ Milliliters":
                result = liters_to_milliliters(input_value)
                st.success(f"{input_value:.2f} L = {result:.2f} mL")
            else:
                result = milliliters_to_liters(input_value)
                st.success(f"{input_value:.2f} mL = {result:.2f} L")

elif category == "Currency":
    st.subheader("💰 Currency Converter")
    direction = st.radio("Conversion Direction", ["USD ➡ INR", "INR ➡ USD"])
    
    rate = st.number_input("Enter exchange rate (default 83.0):", value=83.0, step=0.5)
    unit_label = "$" if "USD" in direction.split("➡")[0] else "₹"
    input_value = get_numeric_input("Enter amount:", unit_label)
    
    if input_value is not None:
        if st.button("Convert"):
            if direction == "USD ➡ INR":
                result = usd_to_inr(input_value, rate)
                st.success(f"${input_value:.2f} = ₹{result:.2f}")
            else:
                result = inr_to_usd(input_value, rate)
                st.success(f"₹{input_value:.2f} = ${result:.2f}")

