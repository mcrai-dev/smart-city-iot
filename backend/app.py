# backend/app.py
from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CSV_PATH = "./data/co2.csv"

@app.route("/api/points")
def get_points():
    try:
        df = pd.read_csv(CSV_PATH)
        data = df.dropna(subset=["lat", "lon"]).to_dict(orient="records")
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
