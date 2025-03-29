import streamlit as st
st.title("Interactive Unit Converter")
st.write("This is an interactive unit converter. Choose a unit type, enter the value, and convert it to another unit.")
unit_type = st.selectbox("Choose unit type", ("Length", "Mass", "Temperature"))
if unit_type == "Length":
    st.subheader("Length Converter")
    length_units = ["Meter", "Kilometer", "Mile"]
    
    from_unit = st.selectbox("From unit", length_units)
    to_unit = st.selectbox("To unit", length_units)
    value = st.number_input("Enter value in " + from_unit, min_value=0.0)
    
    def convert_length(value, from_unit, to_unit):
        conversions = {
            "Meter": 1,
            "Kilometer": 1000,
            "Mile": 1609.34
        }
        return value * conversions[from_unit] / conversions[to_unit]
    
    if value:
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
elif unit_type == "Mass":
    st.subheader("Mass Converter")
    mass_units = ["Kilogram", "Gram", "Pound"]
    
    from_unit = st.selectbox("From unit", mass_units)
    to_unit = st.selectbox("To unit", mass_units)
    value = st.number_input("Enter value in " + from_unit, min_value=0.0)
    
    def convert_mass(value, from_unit, to_unit):
        conversions = {
            "Kilogram": 1,
            "Gram": 1000,
            "Pound": 2.20462
        }
        return value * conversions[from_unit] / conversions[to_unit]
    
    if value:
        result = convert_mass(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
elif unit_type == "Temperature":
    st.subheader("Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    
    from_unit = st.selectbox("From unit", temp_units)
    to_unit = st.selectbox("To unit", temp_units)
    value = st.number_input("Enter value in " + from_unit, min_value=-273.15)
    
    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
            else:
                return value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            else:
                return value
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            else:
                return value
    
    if value:
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
