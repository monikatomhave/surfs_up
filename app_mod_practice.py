from flask import Flask
# Create a New Flask App Instance
# We're now ready to create a new Flask app instance. "Instance" is a general term in programming 
# to refer to a singular version of something. Add the following to your code to create a new Flask 
# instance called app:
# You probably noticed the __name__ variable inside of the Flask() function. Let's pause for 
# a second and identify what's going on here.

# This __name__ variable denotes the name of the current function. You can use the __name__ variable
# to determine if your code is being run from the command line or if it has been imported into 
# another piece of code. Variables with underscores before and after them are called magic methods
# in Python.
app = Flask(__name__)
# Create Flask Routes
# Our Flask app has been created—let's create our first route!

# First, we need to define the starting point, also known as the root. 
@app.route('/')

# Notice the forward slash inside of the app.route? This denotes that we want to put our data at 
# the root of our routes. The forward slash is commonly known as the highest level of hierarchy 
# in any computer system.

# Next, create a function called hello_world(). Whenever you make a route in Flask, you put the 
# code you want in that specific route below @app.route(). Here's what it will look like:

def hello_world():
    return 'Hello world'

# Skill drill, create another route
@app.route('/skilldrill')
def skilldrill():
    return "This is another route created."