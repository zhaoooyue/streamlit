import streamlit as st
import pandas as pd
import numpy as np


PAGES = {
    "Home": "",
    "Visualization": ""
}

selection = st.sidebar.radio("Go to", list(PAGES.keys()))

if selection == "Home":
    st.title("Visualizing Fraud Detection")
    st.markdown(
        """
        This website serves as the purpose of visualizing fraud detection as part of the project delivery from `CSE6242 Data Visualization Project` for 2020 Spring.

        ## What is the problem statement?
        Our aim is to utilize visual analytics and a machine learning technique, to assist in finding important characteristics associated with fraudulent credit card transactions and to develop an effective tool to identify and minimize fraudulent transactions from being approved.

        ## What are the approaches?
        We will be using a mixture of machine learning models including `Gradient Boosting Tree Classifier`, `Random Forest Classifier` and `Linear Regresesion` to compare the results. We will plot feature importance of each model as well.

        ## How to use this website?
        1. Use the sidebar to select an algorithm
        2. Interact and have fun!
        """
    )

elif selection == "Visualization":
    option = st.sidebar.selectbox(
        "Which algorithm do you want to try?",
        ["Gradient Boosting Tree", "Logistic Regression", "Random Forest"],
    )

    if option == "Gradient Boosting Tree":
        st.markdown(
            f"""
            ### Analyzing `{option}` algorithm
            """
        )

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.info("Accuracy vs Iterations")
        st.line_chart(chart_data)
    elif option == "Logistic Regression":
        st.markdown(
            f"""
            ### Analyzing `{option}` algorithm
            """
        )

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.info("Accuracy vs Iterations")
        st.line_chart(chart_data)
    elif option == "Random Forest":
        st.markdown(
            f"""
            ### Analyzing `{option}` algorithm
            """
        )

        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        st.info("Accuracy vs Iterations")
        st.line_chart(chart_data)

