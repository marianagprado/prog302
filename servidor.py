from flask import Flask
app=Flask(__name__)
@app.route("/")
def teste():
    return "<b>teste</b>"
app.run()