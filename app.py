from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return """
            <h1>Hello from Quantm test 2 repo</h1>
            <h2>10-Feb-2024</h2>
            """


if __name__ == "__main__":
    app.run(debug=False, port=8080)
