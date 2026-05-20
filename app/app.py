from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])

@app.before_request
def count_request():
    from flask import request
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()

@app.route("/")
def home():
    return jsonify({
        "service": "platform-demo-service",
        "version": "0.2.0"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
