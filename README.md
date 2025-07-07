# FS Traders Official (Angel One SmartAPI)

## 🚀 Features
- Live F&O Data using Angel One SmartAPI
- PCR (Put/Call Ratio) calculation
- Trend detection (Bullish / Bearish / Neutral)
- Deployable on Streamlit Cloud or Oracle VM

## ⚙️ Setup

1. Create `.env` in this folder with your credentials:
```
API_KEY=your_api_key
SECRET_KEY=your_secret_key
CLIENT_CODE=your_client_code
PASSWORD=your_password
TOTP=your_totp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run locally:
```bash
streamlit run dashboard.py
```

4. Or push to Streamlit Cloud at https://fstrader.streamlit.app/
