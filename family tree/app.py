# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Faizaan" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/Father")
def home():

    name = "Father" # write your name
    age = "90" # write your age

# define the route to mother webpage
@app.route("/Mother")
def home():

    name = "Mother" # write your name
    age = "48" # write your age

# define the route to friends webpage
@app.route("/Friend")
def home():

    name = "Friend" # write your name
    age = "15" # write your age

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
