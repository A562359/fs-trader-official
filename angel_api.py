import os
from smartapi import SmartConnect
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    obj = SmartConnect(api_key=os.getenv("API_KEY"))
    data = obj.generateSession(
        os.getenv("CLIENT_CODE"),
        os.getenv("PASSWORD"),
        os.getenv("TOTP")
    )
    return obj

def fetch_pcr_data(obj):
    try:
        ce_oi = 0
        pe_oi = 0
        symbols = [
            "NIFTY23JUL18000CE", "NIFTY23JUL18000PE",
            "NIFTY23JUL18200CE", "NIFTY23JUL18200PE"
        ]
        for symbol in symbols:
            data = obj.ltpData("NFO", "NIFTY", symbol)
            quote = obj.getQuote("NFO", "NIFTY", symbol)
            oi = quote['data']['openInterest']
            if symbol.endswith("CE"):
                ce_oi += oi
            else:
                pe_oi += oi
        pcr = round(pe_oi / ce_oi, 2) if ce_oi else None
        trend = "Bullish 📈" if pcr > 1.3 else "Bearish 🔻" if pcr < 0.7 else "Neutral ⚖️"
        return {"pcr": pcr, "trend": trend, "ce_oi": ce_oi, "pe_oi": pe_oi}
    except Exception as e:
        return {"error": str(e)}
