from flask import Flask, render_template, request, redirect,jsonify


#create a Flask app 
app = Flask(__name__)


@app.route("/")
def recommendation():

	return "hello"
    


if __name__ == "__main__":
    app.run(debug=True)