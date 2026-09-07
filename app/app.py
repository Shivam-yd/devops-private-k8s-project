from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    environment = os.getenv("ENVIRONMENT", "local")
    version = os.getenv("APP_VERSION", "2.0.0")

    return f"""
    <html>
        <head>
            <title>DevOps Application</title>
        </head>
        <body>
            <h1>Hello from DevOps CI/CD Project!</h1>
            <p>Environment: {environment}</p>
            <p>Version: {version}</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
