import streamlit as st

# Streamlit App Title
st.title("BMI Calculator")

# User Inputs for Height and Weight
height = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, value=170.0)
weight = st.number_input("Enter your weight (kg):", min_value=10.0, max_value=300.0, value=70.0)

# Convert height from cm to meters
height_m = height / 100

# Calculate BMI
if st.button("Calculate BMI"):
    if height_m > 0:
        bmi = weight / (height_m ** 2)
        st.write(f"### Your BMI: {bmi:.2f}")

        # BMI Classification
        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("Normal Weight")
        elif 25.0 <= bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")
    else:
        st.error("Height must be greater than zero!")
