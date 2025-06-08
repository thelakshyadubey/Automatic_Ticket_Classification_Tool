import streamlit as st
import base64

def inject_custom_css(
    bg_image_path: str,
    header_image_path: str,
    sidebar_image_path: str = "",
    css_path: str = "style.css"
):
    # Read and encode images
    with open(bg_image_path, "rb") as bg_file:
        bg_base64 = base64.b64encode(bg_file.read()).decode()
    with open(header_image_path, "rb") as header_file:
        header_base64 = base64.b64encode(header_file.read()).decode()
    
    # Handle optional sidebar image
    if sidebar_image_path:
        with open(sidebar_image_path, "rb") as sidebar_file:
            sidebar_base64 = base64.b64encode(sidebar_file.read()).decode()
    else:
        sidebar_base64 = ""

    # Read CSS template
    with open(css_path, "r", encoding="utf-8") as css_file:
        css_template = css_file.read()

    # Replace placeholders with actual base64 strings
    css_filled = (
        css_template
        .replace("{{BACKGROUND_IMAGE}}", bg_base64)
        .replace("{{HEADER_IMAGE}}", header_base64)
        .replace("{{SIDEBAR_IMAGE}}", sidebar_base64)
    )

    # Inject the CSS
    st.markdown(f"<style>{css_filled}</style>", unsafe_allow_html=True)
