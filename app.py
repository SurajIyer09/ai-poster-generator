import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="AI Poster Generator", layout="centered")
st.markdown("<h1 style='text-align: center; font-size: 42px;'>AI Poster Generator 🎬</h1>", unsafe_allow_html=True)

api_url = "https://rltlbdfuwf.execute-api.ap-south-1.amazonaws.com/v1/poster"

st.write("Describe your poster idea (e.g., *A knight standing in the rain at sunset*)")
user_prompt = st.text_input("Your Prompt")

if st.button("Generate Poster 🎨", use_container_width=True):
    if not user_prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating your poster..."):
            style_prefix = "ultra-realistic, cinematic, high detail, 4k render — "
            full_prompt = style_prefix + user_prompt

            try:
                response = requests.post(api_url, json={"prompt": full_prompt})
                response.raise_for_status()
                result = response.json()

                if "image_url" in result:
                    image_url = result["image_url"]
                    st.image(image_url, caption="Generated Poster", use_container_width=True)

                    # Download button
                    img_data = requests.get(image_url).content
                    st.download_button(
                        label="📥 Download Poster",
                        data=img_data,
                        file_name="ai_poster.png",
                        mime="image/png",
                        use_container_width=True
                    )
                else:
                    st.error(f"Failed to generate poster: {result.get('error', 'Unknown error')}")
            except Exception as e:
                st.error(f"Failed to generate poster: {str(e)}")
