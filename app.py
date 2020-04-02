import os, pymongo
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'recipe'
COLLECTION_FOOD_RECIPE = 'food_recipe'


# Connect to Mongo
conn = pymongo.MongoClient(MONGO_URI)
# Set to link to Mongo database
data_food_recipe = conn[DATABASE_NAME][COLLECTION_FOOD_RECIPE]


@app.route('/') # map the root route to the index function
def index():
    result = data_food_recipe.find({})
    return render_template ('index.html'
    ,data = result
    )

@app.route('/new_recipe')
def new_recipe ():
    return render_template('new_recipe.html') 
    
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
