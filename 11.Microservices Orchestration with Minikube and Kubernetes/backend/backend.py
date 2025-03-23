from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "message": "ਹੋ ਉਮਰਾਂ ਵਾਰੇ ਤਾਂ ਬੀਬਾ ਰੱਬ ਜਾਨ ਦਾ, ਜਿੰਦਗੀ ਜਿਓਨੀ ਕਿਵੇਂ ਜੱਟ ਨੂ ਪਤਾ",
        "hostname": os.uname().nodename,
        "version": "1.0.0"
    }

@app.route('/health')
def health():
    return {
        "status": "healthy",
        "service": "backend"
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 