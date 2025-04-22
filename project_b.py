import streamlit as st
import requests

def show_project_b():
    st.markdown("## 🧾 Download")

    col1, col2 = st.columns(2)

    # Column 1 - Dashboard PDF
    pdf_path = r"E:\Coding\4 - Portofolio Posting\4 - Customer Sentiment\dashboard\Ticket_System_Customer Sentiment Dashboard.pdf"
    with col1:
        if st.button("📄 Prepare PDF Download", key="prepare_pdf_btn"):
            try:
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="📄 Download Dashboard (PDF)",
                        data=f.read(),
                        file_name="customer_sentiment_dashboard.pdf",
                        mime="application/pdf",
                        key="pdf_download_btn"
                    )
            except FileNotFoundError:
                st.warning("Dashboard PDF not found.")

    # Column 2 - Power BI File
    pbix_path = r"E:\Coding\4 - Portofolio Posting\4 - Customer Sentiment\dashboard\Ticket_System_Customer Sentiment Dashboard.pbix"
    with col2:
        if st.button("📊 Prepare Power BI Download", key="prepare_pbix_btn"):
            try:
                with open(pbix_path, "rb") as f:
                    st.download_button(
                        label="📊 Download Power BI File (.pbix)",
                        data=f.read(),
                        file_name="Ticket_System_Customer_Sentiment.pbix",
                        mime="application/octet-stream",
                        key="pbix_download_btn"
                    )
            except FileNotFoundError:
                st.warning("Power BI file not found.")

    st.markdown("---")
    st.markdown("## 📘 Project Description")

    # Fetch and display README from GitHub
    github_raw_url = "https://raw.githubusercontent.com/RadityaEr/Ticketing-System-Sentiment/main/README.md"
    try:
        response = requests.get(github_raw_url)
        if response.status_code == 200:
            st.markdown(response.text, unsafe_allow_html=True)
        else:
            st.error("Could not fetch README from GitHub.")
    except Exception as e:
        st.error(f"Error fetching README: {e}")
