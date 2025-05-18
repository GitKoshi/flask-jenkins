from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Je vais chier dans mon froc"

if __name__ == "__main__":
    app.run(debug=True)
