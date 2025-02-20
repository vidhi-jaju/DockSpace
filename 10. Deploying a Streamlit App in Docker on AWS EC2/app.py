import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import RocCurveDisplay, PrecisionRecallDisplay, ConfusionMatrixDisplay

def main():
    st.title("Binary Classification WebApp")    
    st.markdown("Are your mushrooms edible or poisonous? 🍄")

    st.sidebar.title("Binary Classification")
    st.sidebar.markdown("Are your mushrooms edible or poisonous?")

    @st.cache_data
    def load_data():
        try:
            data = pd.read_csv('mushrooms.csv')
            label = LabelEncoder()
            for col in data.columns:
                data[col] = label.fit_transform(data[col])
            return data
        except FileNotFoundError:
            st.error("Error: `mushrooms.csv` not found! Please upload the dataset.")
            return None

    @st.cache_data
    def split(df):
        y = df['type']
        x = df.drop(columns=['type'])
        return train_test_split(x, y, test_size=0.3, random_state=0)

    def plot_metrics(metrics_list, model, x_test, y_test, y_pred):
        for metric in metrics_list:
            st.subheader(metric)

            if metric == 'Confusion Matrix':
                fig, ax = plt.subplots()
                cm = confusion_matrix(y_test, y_pred)
                ConfusionMatrixDisplay(cm).plot(ax=ax)
                st.pyplot(fig)

            if metric == 'ROC Curve':
                fig, ax = plt.subplots()
                RocCurveDisplay.from_estimator(model, x_test, y_test, ax=ax)
                st.pyplot(fig)

            if metric == 'Precision-Recall Curve':
                fig, ax = plt.subplots()
                PrecisionRecallDisplay.from_estimator(model, x_test, y_test, ax=ax)
                st.pyplot(fig)

    df = load_data()
    if df is None:
        return  # Stop execution if CSV not found

    x_train, x_test, y_train, y_test = split(df)
    class_names = ['edible', 'poisonous']
    
    st.sidebar.subheader("Choose Classifier")
    classifier = st.sidebar.selectbox("Classifier", 
                                      ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest"))

    if classifier == "Support Vector Machine (SVM)":
        st.sidebar.subheader("Model Hyperparameters")
        C_svm = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_svm')
        kernel = st.sidebar.radio("Kernel", ("rbf", "linear"), key='kernel')
        gamma = st.sidebar.radio("Gamma (Kernel Coefficient)", ("scale", "auto"), key='gamma')
    
        metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))
    
        if st.sidebar.button("Classify", key='classify_svm'):
            st.subheader("Support Vector Machine (SVM) Results")
            model = SVC(C=C_svm, kernel=kernel, gamma=gamma)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            st.write("Accuracy:", model.score(x_test, y_test))
            st.write("Precision:", precision_score(y_test, y_pred))
            st.write("Recall:", recall_score(y_test, y_pred))
            plot_metrics(metrics, model, x_test, y_test, y_pred)

    if classifier == "Logistic Regression":
        st.sidebar.subheader("Model Hyperparameters")
        C_lr = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_lr')
        max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, key='max_iter')
        
        metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))
    
        if st.sidebar.button("Classify", key='classify_lr'):
            st.subheader("Logistic Regression Results")
            model = LogisticRegression(C=C_lr, max_iter=max_iter)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            st.write("Accuracy:", model.score(x_test, y_test))
            st.write("Precision:", precision_score(y_test, y_pred))
            st.write("Recall:", recall_score(y_test, y_pred))
            plot_metrics(metrics, model, x_test, y_test, y_pred)

    if classifier == "Random Forest":
        st.sidebar.subheader("Model Hyperparameters")        
        n_estimators = st.sidebar.number_input("The number of trees in the forest", 100, 5000, step=10, key='n_estimators')
        max_depth = st.sidebar.number_input("The maximum depth of the tree", 1, 20, step=1, key='max_depth')
        bootstrap = st.sidebar.radio("Bootstrap samples when building trees", (True, False), key='bootstrap')
        
        metrics = st.sidebar.multiselect("What metrics to plot?", ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve'))
    
        if st.sidebar.button("Classify", key='classify_rf'):
            st.subheader("Random Forest Results")
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, bootstrap=bootstrap, n_jobs=-1)
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            st.write("Accuracy:", model.score(x_test, y_test))
            st.write("Precision:", precision_score(y_test, y_pred))
            st.write("Recall:", recall_score(y_test, y_pred))
            plot_metrics(metrics, model, x_test, y_test, y_pred)
                        
    if st.sidebar.checkbox("Show raw data", False):
        st.subheader("Mushroom Data Set (Classification)")
        st.write(df)
    
if __name__ == '__main__':
    main()