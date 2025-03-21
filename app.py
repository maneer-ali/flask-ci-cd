from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a CI/CD demo with Cloud Build and Cloud Run! and my name is maneer ali and see the magic"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
