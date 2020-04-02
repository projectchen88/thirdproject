from flask import Flask, render_template, request, redirect, url_for
import os, pymongo

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'recipe'
COLLECTION_FOOD_RECIPE = 'food_recipe'


# Connect to Mongo
conn = pymongo.MongoClient(MONGO_URI)
# Set to link to Mongo database
data_food_recipe = conn[DATABASE_NAME][COLLECTION_FOOD_RECIPE]


@app.route('/')
def index():
    result = data_food_recipe.find({})
    return render_template ('index.html'
    , data = result
    )

@app.route('/new_recipe')
def new_recipe ():
    return render_template('new_recipe.html') 
    
@app.route('/new_recipe', methods=['POST'])
def upload_recipe ():
    ''' Upload the recipe submitted by the user '''
    # Recipe name 
    # dish_name = request.form.get('dish_name')
    # # Recipe image
    # dish_image = request.files.get('dish_image')
    # # Recipe description
    # dish_description = request.form.get('dish_description')
    # # Ingredients
    # dish_ingredient1 = request.form.get('dish_ingredient1')
    # dish_ingredient2 = request.form.get('dish_ingredient2')
    # dish_ingredient3 = request.form.get('dish_ingredient3')
    # dish_ingredient4 = request.form.get('dish_ingredient4')
    # dish_ingredient5 = request.form.get('dish_ingredient5')
    # dish_ingredient6 = request.form.get('dish_ingredient6')
    # dish_ingredient7 = request.form.get('dish_ingredient7')
    # dish_ingredient8 = request.form.get('dish_ingredient8')
    # dish_ingredient9 = request.form.get('dish_ingredient9')
    # dish_ingredient10 = request.form.get('dish_ingredient10')
    # # Instructions
    # dish_instruction1 = request.form.get('dish_instruction1')
    # dish_instruction2 = request.form.get('dish_instruction2')
    # dish_instruction3 = request.form.get('dish_instruction3')
    # dish_instruction4 = request.form.get('dish_instruction4')
    # dish_instruction5 = request.form.get('dish_instruction5')
    # dish_instruction6 = request.form.get('dish_instruction6')
    # dish_instruction7 = request.form.get('dish_instruction7')
    # dish_instruction8 = request.form.get('dish_instruction8')
    # dish_instruction9 = request.form.get('dish_instruction9')
    # dish_instruction10 = request.form.get('dish_instruction10')
    
    return redirect ( url_for('index') )

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
