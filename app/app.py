from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "4.2.0")
PAYMENT_STATUS = os.getenv("PAYMENT_STATUS", "FAILED")

@app.route("/")
def home():
    return jsonify({
        "application": "retail-platform",
        "version": VERSION,
        "payment_status": PAYMENT_STATUS
    })

@app.route("/health")
def health():
    if PAYMENT_STATUS == "FAILED":
        return jsonify({"status": "unhealthy"}), 500

    return jsonify({
        "status": "healthy",
        "version": VERSION
    }), 200

@app.route("/products")
def products():
    return jsonify({
        "products": [
            {"id": 1, "name": "Laptop"},
            {"id": 2, "name": "Phone"}
        ]
    })



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
