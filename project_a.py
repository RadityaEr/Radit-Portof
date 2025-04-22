import streamlit as st
import requests

def show_project_a():
    st.markdown("## 🧾 Download")

    col1, col2 = st.columns(2)

    # Column 1 - Dashboard PDF
    pdf_path = r"E:\Coding\4 - Portofolio Posting\RFM Analysis in Pakistan E Commerce\dashboard\Dashboard.pdf"
    with col1:
        if st.button("📄 Prepare PDF Download"):
            try:
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📄 Download Dashboard (PDF)",
                        data=f.read(),
                        file_name="rfm_dashboard.pdf",
                        mime="application/pdf",
                        key="pdf_download_btn"
                    )
            except FileNotFoundError:
                st.warning("Dashboard PDF not found.")

    # Column 2 - Power BI File
    pbix_path = r"E:\Coding\4 - Portofolio Posting\RFM Analysis in Pakistan E Commerce\dashboard\Pakistani_Project_PowerBI.pbix"
    with col2:
        if st.button("📊 Prepare Power BI Download"):
            try:
                with open(pbix_path, "rb") as f:
                    st.download_button(
                        label="📊 Download Power BI File (.pbix)",
                        data=f.read(),
                        file_name="Pakistani_Project_PowerBI.pbix",
                        mime="application/octet-stream",
                        key="pbix_download_btn"
                    )
            except FileNotFoundError:
                st.warning("Power BI file not found.")

    st.markdown("---")
    st.markdown("## 📘 Project Description")

    github_raw_url = "https://raw.githubusercontent.com/RadityaEr/Pakistan-RFM-Analysis/main/README.md"
    try:
        response = requests.get(github_raw_url)
        if response.status_code == 200:
            st.markdown(response.text, unsafe_allow_html=True)
        else:
            st.error("Could not fetch README from GitHub.")
    except Exception as e:
        st.error(f"Error fetching README: {e}")
