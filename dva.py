import streamlit as st
import pandas as pd
import numpy as np
import json
import time


PAGES = {"Home": "", "Visualization": ""}

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
            ## Analyzing `{option}` algorithm

            Gradient Boosted Tree is an `ensembled` learning model. As compared to training a single model, boosting adds new decision trees to an ensemble of decision trees sequentially. 
            This would help in reducing variance of classifications. The `Gradient Boosted Trees` algorithm also provides feature importances, which provides an idea of which variables are important in classifications for fraud detection.
            """
        )

        sample_strategy = st.selectbox(
            "Please choose your sampling strategy",
            ["Sampled", "Unsampled"],
        )

        if sample_strategy == "Sampled":
            st.info("""
                We used 3-folds cross-validation to fit a model using PySpark MLlib’s Gradient Boosted Tree Classifier.
                To maintain a reasonable training time, we left the maximum number of iterations as 10 and employed 3-folds cross-validation instead of 5-folds.
                """
            )
            with open('gbt_sampled.json') as f:
                sampled_data = json.load(f)
                training_accuracy = sampled_data["train_auc"] * 100
                testing_accuracy = sampled_data["test_auc"] * 100
                train_iteration = st.empty()
                bar = st.progress(0)
                for i in range(int(training_accuracy)):
                    train_iteration.text(f'Training Accuracy: {(i+1)}%')
                    bar.progress(i + 1)
                    time.sleep(0.05)

                test_iteration = st.empty()
                bar2 = st.progress(0)
                for i in range(int(testing_accuracy)):
                    test_iteration.text(f'Testing Accuracy: {(i+1)}%')
                    bar2.progress(i + 1)
                    time.sleep(0.05)
            
            st.info("Sampled strategy analysis completed! Do you want to try unsampled?")

        elif sample_strategy == "Unsampled":
            st.info("""
                We used 3-folds cross-validation to fit a model using PySpark MLlib’s Gradient Boosted Tree Classifier without sampling.
                To maintain a reasonable training time, we left the maximum number of iterations as 10 and employed 3-folds cross-validation instead of 5-folds.
                """
            )
            with open('gbt_unsampled.json') as f:
                unsampled_data = json.load(f)

                show_accuracy = st.checkbox("Display training/testing accuracy")
                if show_accuracy:
                    training_accuracy = unsampled_data["train_auc"] * 100
                    testing_accuracy = unsampled_data["test_auc"] * 100
                    train_iteration = st.empty()
                    bar = st.progress(0)
                    for i in range(int(training_accuracy)):
                        train_iteration.text(f'Training Accuracy: {(i+1)}%')
                        bar.progress(i + 1)
                        time.sleep(0.05)

                    test_iteration = st.empty()
                    bar2 = st.progress(0)
                    for i in range(int(testing_accuracy)):
                        test_iteration.text(f'Testing Accuracy: {(i+1)}%')
                        bar2.progress(i + 1)
                        time.sleep(0.05)

                st.info("We can analyze which features are more important to contribute to this testing accuracy!")
                count = st.slider('What are the top N features?', 0, 10, 0, key="slider")
                if count > 0:
                    df = pd.DataFrame(
                        unsampled_data["feature_importance"][:count],
                        columns=(['Feature Name', 'Feature Importance']))
                    st.dataframe(df)

    elif option == "Logistic Regression":
        st.markdown(
            f"""
            ## Analyzing `{option}` algorithm

            Work in Progress by ZY....
            """
        )

    elif option == "Random Forest":
        st.markdown(
            f"""
            ## Analyzing `{option}` algorithm

            Work in Progress by ZY....
            """
        )
