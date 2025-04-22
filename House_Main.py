import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide", page_icon=":rocket:")
st.title("Raditya Erlang Arkananta - Portfolio")
st.header("Data Scientist Enthusiast")

import base64

import os
import base64

def set_bg_from_local(image_file):
    # Get the full path to the image relative to this script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, image_file)

    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(
                rgba(0, 0, 0, 0.5), 
                rgba(0, 0, 0, 0.5)
            ), 
            url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call it at the top of your app
set_bg_from_local("Starry Night.jpg")


# Create horizontal tabs
tabs = st.tabs(["👤 About Me", "📊 Data Analytics Projects", "🤖 Machine Learning", "📬 Contact Me"])

with tabs[0]:
    import tentang_saya
    tentang_saya.tampilkan_tentang_saya()

with tabs[1]:
    st.subheader("📊 Data Analytics Projects")
    st.markdown("This section showcases a collection of data analytics projects that highlight my skills in data wrangling, visualization, and statistical analysis. The projects demonstrates practical insights derived from real-world datasets using tools like Python, Pandas, as well as Visualization tools such as PowerBI.")
    import project_a
    import project_b

    with st.expander("📁 Project A - Pakistani E-Commerce Customer Analysis"):
        project_a.show_project_a()

    with st.expander("📁 Project B - Ticket System Review & Analysis"):
        project_b.show_project_b()

with tabs[2]:
    st.subheader("🤖 Machine Learning Projects")
    st.markdown("This section features machine learning projects focused on predictive modeling, classification, and clustering. These projects illustrate my ability to build, evaluate, and deploy ML models using frameworks like scikit-learn to Predict Housing Prices or Churning Customers")

    import ml_project_a
    import ml_project_b

    with st.expander("📁 ML Project A - House Price Prediction"):
        ml_project_a.show_ml_project_a()

    with st.expander("📁 ML Project B - Customer Churn Prediction"):
        ml_project_b.show_ml_project_b()

with tabs[3]:
    import kontak
    kontak.tampilkan_kontak()
