import streamlit as st
import pandas as pd
import numpy as np

st.title("CSE6242 Data Visualization Project")

st.markdown("""
This website serves as the purpose of demonstrating `CSE6242 Data Visualization Project` for 2020 Spring

## How to use this website?
1. Use the sidebar to select an algorithm
2. Interact and have fun!
""")

option = st.sidebar.selectbox(
    'Which algorithm do you want to try?',
     ["Decision Tree", "Random Forests", "Clustering"])

st.markdown(f"""
### Analyzing `{option}` algorithm
""")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.info("Accuracy vs Iterations")
st.line_chart(chart_data)
