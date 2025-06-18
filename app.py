from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Rafa Radhitya Riyanto, 22523079!"

if __name__ == "__main__":
    app.run()
