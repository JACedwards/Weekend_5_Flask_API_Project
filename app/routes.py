#url default:  http://127.0.0.1:5000

#1 Next line is to access the Flask object (from __init__ file)

from app import app

#route decorator:
    # Syntax:  @<flask object/bluprint name>.route('url endpoint', <methods>)
    #followed by a regular python function
    #return value of regular python function is what will be displayded on the URL page

    #'/' = index page at root of project

from flask import render_template

#API call:  need to import the requests module (which needs to be installed:  pip install requests)
import requests as r
from flask_login import login_required



@app.route('/')  #Each @app is for a separate html page
#2. Return html file from our flask routes
def home():   #for home page
    greeting = 'Calling all Pokmon Newbies.  \nStart Pokemon for Morons here:'
    print(greeting)
    
    return render_template('index.html', greeting = greeting)  


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    poke = {}

    for i in range(1,21):
        data = r.get('https://pokeapi.co/api/v2/pokemon/' + str(i))
        # print(data)
        if data.status_code == 200:
            # print('test')
            data = data.json()
        else:
            return "Data source not responding"

        name = data['forms'][0]['name']
        # # print(name)
        url =  "https://www.pokemon.com/us/pokedex/" + name
        # print(url)   
        poke[name]=url

    return render_template('pokemon.html', poke = poke)


from .services import getabilities

@app.route('/abilities', methods=['GET', 'POST'])
@login_required
def abilities():
    able_dict_sorted = getabilities()
    
    return render_template('abilities.html', able_dict_sorted = able_dict_sorted)



# 


####To run, in terminal:
    #make sure you are in virtual area
    #Type:  flask run

