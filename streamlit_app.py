import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Sample DataFrame
data = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Value': [100, 200, 300]})

# Dropdown for filtering
category = st.selectbox('Select a category:', data['Category'].unique())

# Filter data
filtered_data = data[data['Category'] == category]

# Display filtered data
st.write(filtered_data)
