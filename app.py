from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return """
            <h1>Hello from Quantm test 2 repo</h1>
            <h2>10-Feb-2024</h2>
            <h3>Testing for #88</h3>
            <h3>umerm64-patch-10</h3>
            <h3>22-March-2024</h3>
            """


if __name__ == "__main__":
    app.run(debug=False, port=8080)
