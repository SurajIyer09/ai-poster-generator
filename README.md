# 🎨 AI Poster Generator

Generate stunning AI-based posters from simple text prompts using Streamlit + AWS Lambda + Amazon Bedrock SDXL + S3.

---

## 🔥 Features

- 🖋️ Enter a prompt to generate a poster
- 🎨 AI image generation with Stable Diffusion XL (SDXL)
- 💾 Download poster to your local device
- 🌐 Web-based UI with Streamlit
- ☁️ AWS Lambda integration
- 📤 Poster saved to S3 (optional)

---

## 🚀 How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/ai-poster-generator.git
   cd ai-poster-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 🛠️ Backend Setup with AWS Lambda

- Runtime: Python 3.11
- Region: ap-south-1
- Bedrock SDXL is invoked from `us-east-1`
- Uses:
  - `boto3` for AWS SDK
  - IAM role with `bedrock:InvokeModel`, `s3:PutObject`, `s3:GetObject`

---

## 📁 Project Structure

```
ai-poster-generator/
├── app.py                 # Streamlit frontend
├── lambda_function.py     # AWS Lambda function
├── requirements.txt       # Dependencies
└── README.md              # Project info
```

---

## 🧠 Powered By

- [Streamlit](https://streamlit.io)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Stable Diffusion XL](https://stability.ai/blog/stable-diffusion-xl)

---

## 📥 Download Feature

Click the **Download Poster** button after image generation.

---

## 📜 License

MIT License

---

## ✨ Contribute

Have an idea or improvement? PRs welcome!
