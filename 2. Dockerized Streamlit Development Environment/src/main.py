import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Streamlit Demo: Interactive App")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Explorer", "Visualization"])

# Home Page
if page == "Home":
    st.header("Welcome to the Streamlit App")
    st.write(
        """
        This is a demo app built with Streamlit, showcasing:
        - Interactive widgets
        - Data manipulation and visualization
        - Dynamic content updates
        """
    )
    st.image(
        "https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.png",
        width=300,
    )

    st.write("Select a page from the sidebar to explore!")

# Data Explorer Page
elif page == "Data Explorer":
    st.header("Upload and Explore Your Data")

    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.stop()

        # Display the dataset
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        # Dataset summary
        if st.checkbox("Show Dataset Summary"):
            st.write(df.describe())

        # Data shape
        st.write("Dataset shape:", df.shape)
    else:
        st.info("Upload a CSV file to explore your data.")

# Visualization Page
elif page == "Visualization":
    st.header("Data Visualization")

    # Generate sample data
    st.subheader("Random Data Visualization")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sine Wave")
    ax.set_title("Sample Sine Wave")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()

    st.pyplot(fig)

    # Interactive chart
    st.subheader("Interactive Data")
    random_data = pd.DataFrame(
        np.random.randn(50, 3),
        columns=["A", "B", "C"]
    )
    st.line_chart(random_data)

    st.write("Explore the sidebar to navigate through the app!")

