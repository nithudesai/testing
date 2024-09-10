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

if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = 'Option 1'

selected_option = st.radio('Select an option to update the dropdown:', ['Option 1', 'Option 2'])

st.session_state['selected_option'] = selected_option

option = st.selectbox('Your selection affects this dropdown:', [st.session_state['selected_option'], 'Option 3'], key='dynamic_selectbox')
