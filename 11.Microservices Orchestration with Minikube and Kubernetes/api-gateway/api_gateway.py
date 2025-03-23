from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_SERVICE_URL = os.getenv('BACKEND_SERVICE_URL', 'http://backend-service:5000')

@app.route('/')
def hello():
    try:
        backend_response = requests.get(f"{BACKEND_SERVICE_URL}/")
        return {
            "message": "API Gateway Response",
            "backend": backend_response.json(),
            "hostname": os.uname().nodename,
            "version": "1.0.0"
        }
    except requests.exceptions.RequestException as e:
        return {
            "error": "Failed to connect to backend service",
            "details": str(e)
        }, 503

@app.route('/health')
def health():
    return {
        "status": "healthy",
        "service": "api-gateway"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080) 