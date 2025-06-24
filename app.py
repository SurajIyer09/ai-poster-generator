import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(page_title="AI Poster Generator")

st.markdown("<h1 style='text-align: center; font-size: 48px;'>AI Poster Generator 🎨</h1>", unsafe_allow_html=True)
st.write("Enter a creative prompt and generate your custom AI poster instantly!")

# Input field
prompt = st.text_input("Enter your poster prompt", "A futuristic city with glowing skyscrapers")

# Button to trigger API
if st.button("Generate Poster"):
    with st.spinner("Generating your poster..."):
        response = requests.post(
            "https://rltlbdfuwf.execute-api.ap-south-1.amazonaws.com/v1/poster",
            json={"prompt": prompt},
        )

        if response.status_code == 200:
            image_url = response.json().get("image_url")
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            st.image(image, caption="Your AI Poster", use_column_width=True)

            # Download button
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_data = buffered.getvalue()
            b64 = base64.b64encode(img_data).decode()
            href = f'<a href="data:file/png;base64,{b64}" download="ai_poster.png">📥 Download Poster</a>'
            st.markdown(href, unsafe_allow_html=True)

        else:
            st.error("Failed to generate poster: " + response.text)
