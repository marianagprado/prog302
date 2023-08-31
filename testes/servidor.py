from flask import Flask
app=Flask(__name__)
@app.route("/")
def teste():
    return "servidor na rede"
app.run(debug=True, host="0.0.0.0", port=4999)
