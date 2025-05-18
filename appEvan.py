from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Heureusement que chatgpt existe ^^"

if __name__ == "__main__":
    app.run(debug=True)
