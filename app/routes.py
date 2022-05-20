#url default:  http://127.0.0.1:5000

#1 Next line is to access the Flask object (from __init__ file)
from app import app

#route decorator:
    # Syntax:  @<flask object/bluprint name>.route('url endpoint', <methods>)
    #followed by a regular python function
    #return value of regular python function is what will be displayded on the URL page

    #'/' = index page at root of project
from flask import render_template

@app.route('/')

#2. Return html file from our flask routes


def home():   #for home page
    greeting = 'Welcome to flask week, Foxes!'
    print(greeting)
    return render_template('index.html')  #a call to the render_template function
        #so what will be returned is the return value of the render_template() function 
        #Then,pass into render_template function () the name of the html file I am trying to render
        #to check this, make sure in virtual environment,
            #flask run
            #access URL from command line, not directly from html file
    #render_template() accepts arbitrary number of arguments/parameters.
        #so, to get greeting in example above to show on html page, need to 
        #   give it a variable name (g=greeting) 
        #   then add it as parameter  to render_template, along with the html endpoint url.
        #   only then can it be used as a variable in a Jinma expression on the html page using
        #       the variable "g".


#To run, in terminal:
    #make sure you are in virtual area
    #Type:  flask run




