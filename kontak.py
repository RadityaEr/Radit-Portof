import streamlit as st

def tampilkan_kontak():
    st.markdown("""
        <style>
        .title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            color: #4A90E2;
            margin-bottom: 0.3em;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #ccc;
            margin-bottom: 2em;
        }
        .contact-box {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 2em;
            max-width: 600px;
            margin: 0 auto 2em;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }
        .contact-link {
            margin: 1em 0;
            font-size: 1.1em;
            color: #eee;
        }
        .contact-link a {
            text-decoration: none;
            color: #87CEFA;
        }
        .contact-icon {
            margin-right: 0.5em;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">📬 Get in Touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Feel free to reach out via any of the platforms below!</div>', unsafe_allow_html=True)

    # Entire box content inside one block
    st.markdown('''
        <div class="contact-box">
            <div class="contact-link">
                <span class="contact-icon">🔗</span>
                <a href="https://www.linkedin.com/in/raditya-erlang-arkananta/" target="_blank">LinkedIn Profile - Raditya Erlang Arkananta</a>
            </div>
            <div class="contact-link">
                <span class="contact-icon">💻</span>
                <a href="https://github.com/RadityaEr" target="_blank">GitHub Profile - RadityaEr</a>
            </div>
            <div class="contact-link">
                <span class="contact-icon">📧</span>
                <a href="mailto:erlang_work@yahoo.com">erlang_work@yahoo.com</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)
