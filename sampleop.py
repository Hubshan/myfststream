import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Header
st.title("Basic Streamlit Operations")
st.header("This is a Streamlit App")

# Display Text
st.write("This is a sample Streamlit application demonstrating basic operations.")

# User Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Buttons
if st.button("Click Me"):
    st.success("Button clicked!")

# Select Box
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# Slider
value = st.slider("Select a value:", 0, 100, 50)
st.write(f"Slider value: {value}")

# File Upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

# Checkbox
if st.checkbox("Show/Hide Message"):
    st.write("Checkbox is checked!")

# Radio Buttons
radio_option = st.radio("Choose a color:", ["Red", "Blue", "Green"])
st.write(f"Selected color: {radio_option}")

# Data Visualization using Matplotlib
st.subheader("Simple Bar Chart")
chart_data = pd.DataFrame({"A": [10, 20, 30], "B": [5, 15, 25]})
fig, ax = plt.subplots()
ax.bar(chart_data.index, chart_data["A"], label="A")
ax.bar(chart_data.index, chart_data["B"], label="B", bottom=chart_data["A"])
ax.set_xlabel("Category")
ax.set_ylabel("Values")
ax.legend()
st.pyplot(fig)

# Session State (Counter Example)
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increment Counter"):
    st.session_state.count += 1
st.write(f"Counter: {st.session_state.count}")
