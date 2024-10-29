from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Let the DBMS roll..."

if __name__ == "__main__":
    app.run(debug=True)