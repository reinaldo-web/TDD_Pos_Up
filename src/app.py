from flask import flask 

app = flask(__name__)

@app.rout ("/")
def index ():
    return "hello, world"
if __name__ == "__main__":
    app.run()

