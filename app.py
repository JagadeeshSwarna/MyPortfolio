from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin


app = Flask(__name__)  # initialising the flask app with the name 'app'
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(port=8000,debug=True) # running the app on the local machine on port 8000
