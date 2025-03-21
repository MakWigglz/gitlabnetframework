from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_from_devops():
    return "Hello from DevOps! This is Mak the Coder demonstrating CI/CD capability"

if __name__ == "__main__":
    app.run(debug=True)
