import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

API_URL = "https://rltlbdfuwf.execute-api.ap-south-1.amazonaws.com/v1/poster"

st.set_page_config(page_title="AI Poster Generator 🎨", layout="centered")

# Updated header
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🧠 AI Poster Generator</h1>", unsafe_allow_html=True)

prompt = st.text_input("Enter your poster prompt", value="a futuristic sci-fi movie poster with neon lights")

if st.button("Generate Poster"):
    with st.spinner("Generating..."):
        response = requests.post(API_URL, json={"prompt": prompt})
        if response.status_code == 200:
            data = response.json()
            image_url = data["image_url"]
            st.success("Poster generated successfully!")
            
            # Display image
            st.image(image_url, use_container_width=True)

            # Download button
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                img_bytes = image_response.content
                st.download_button(
                    label="⬇️ Download Poster",
                    data=img_bytes,
                    file_name="poster.png",
                    mime="image/png"
                )

                # Upload to S3 button (optional re-upload)
                if st.button("⬆️ Upload to S3 Again"):
                    upload_response = requests.post(API_URL, json={"prompt": prompt})
                    if upload_response.status_code == 200:
                        st.success("Poster re-uploaded to S3 successfully!")
                    else:
                        st.error("Upload failed.")

        else:
            st.error(f"Failed to generate poster: {response.text}")
