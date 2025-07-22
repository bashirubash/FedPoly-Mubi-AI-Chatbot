# FedPoly Mubi AI Chatbot (Render Deployment)

## Features:
- Academic assistant chatbot for Federal Polytechnic Mubi.
- Powered by `mistralai/Mistral-7B-Instruct-v0.2`.
- Handles registration, results, hostel, fees, etc.
- No fine-tuning required.

## Deployment on Render:
1. Create a new **Web Service** on [render.com](https://render.com/).
2. Connect your GitHub repo or upload these files.
3. Render will automatically use `render.yaml` and `Procfile`.

## Local Run (Optional):
```bash
pip install -r requirements.txt
python app.py
