import os
from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"]
)


@app.before_request
def before_request():
    from flask import g
    g.start_time = time.time()


@app.after_request
def after_request(response):
    from flask import request, g

    latency = time.time() - g.start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        http_status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).observe(latency)

    return response


@app.route("/")
def home():
    environment = os.getenv("ENVIRONMENT", "local")
    version = os.getenv("APP_VERSION", "3.0.0")
    return f"""
    <html>
        <head>
            <title>DevOps Application</title>
        </head>
        <body>
            <h1>Hello from DevOps Kubernetes project</h1>
            <p>Environment: {environment}</p>
            <p>Version: {version}</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return "OK"


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
