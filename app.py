from flask import Flask, render_template, request, redirect, url_for
import os, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# setting up the upload folder
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))+'/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.getenv("SECRET","randomsecretkey1234")

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'recipe'
COLLECTION_FOOD_RECIPE = 'food_recipe'

# Connect to Mongo
conn = pymongo.MongoClient(MONGO_URI)
# Set to link to Mongo database
data_food_recipe = conn[DATABASE_NAME][COLLECTION_FOOD_RECIPE]

''' Index page '''
@app.route('/')
def index():
    result = data_food_recipe.find({})
    return render_template ('index.html'
    , data = result
    )

''' Render a empty template for user to enter the new recipe '''
@app.route('/new_recipe')
def new_recipe ():
    return render_template('new_recipe.html', data={}) 
    
''' Upload the recipe submitted by the user '''
@app.route('/new_recipe', methods=['POST'])
def upload_recipe ():
    # Recipe name 
    dish_name = request.form.get('dish_name')
    # Recipe image
    dish_image = request.files.get('dish_image')
    # Recipe description
    dish_description = request.form.get('dish_description')
    
    # Ingredients
    dish_ingredient1 = request.form.get('dish_ingredient1')
    dish_ingredient2 = request.form.get('dish_ingredient2')
    dish_ingredient3 = request.form.get('dish_ingredient3')
    dish_ingredient4 = request.form.get('dish_ingredient4')
    dish_ingredient5 = request.form.get('dish_ingredient5')
    dish_ingredient6 = request.form.get('dish_ingredient6')
    dish_ingredient7 = request.form.get('dish_ingredient7')
    dish_ingredient8 = request.form.get('dish_ingredient8')
    dish_ingredient9 = request.form.get('dish_ingredient9')
    dish_ingredient10 = request.form.get('dish_ingredient10')
    
    # Ingredient Portion
    dish_ingredient1_portion = request.form.get('dish_ingredient1_portion')
    dish_ingredient2_portion = request.form.get('dish_ingredient2_portion')
    dish_ingredient3_portion = request.form.get('dish_ingredient3_portion')
    dish_ingredient4_portion = request.form.get('dish_ingredient4_portion')
    dish_ingredient5_portion = request.form.get('dish_ingredient5_portion')
    dish_ingredient6_portion = request.form.get('dish_ingredient6_portion')
    dish_ingredient7_portion = request.form.get('dish_ingredient7_portion')
    dish_ingredient8_portion = request.form.get('dish_ingredient8_portion')
    dish_ingredient9_portion = request.form.get('dish_ingredient9_portion')
    dish_ingredient10_portion = request.form.get('dish_ingredient10_portion')
    
    # Instructions
    dish_instruction1 = request.form.get('dish_instruction1')
    dish_instruction2 = request.form.get('dish_instruction2')
    dish_instruction3 = request.form.get('dish_instruction3')
    dish_instruction4 = request.form.get('dish_instruction4')
    dish_instruction5 = request.form.get('dish_instruction5')
    dish_instruction6 = request.form.get('dish_instruction6')
    dish_instruction7 = request.form.get('dish_instruction7')
    dish_instruction8 = request.form.get('dish_instruction8')
    dish_instruction9 = request.form.get('dish_instruction9')
    dish_instruction10 = request.form.get('dish_instruction10')
    # Preparation time
    dish_prep_time = request.form.get('dish_prep_time')
    # Cooking time
    dish_cook_time = request.form.get('dish_cook_time')
    # Servings 
    dish_serving = request.form.get('dish_serving')
    # Cusine style
    dish_type = request.form.get('dish_type')
    # Skill level
    dish_skill = request.form.get('dish_skill')
    
    # Insert the data into the Mongo database
    data_food_recipe.insert({
        'dish_name' : dish_name,
        'dish_image' : dish_image.filename,
        'dish_description' : dish_description,
        'dish_prep_time' : dish_prep_time,
        'dish_cook_time' : dish_cook_time,
        'dish_serving' : dish_serving,
        'dish_type' : dish_type, 
        'dish_skill' : dish_skill,
        'dish_ingredient': [
            {
                'numbering' : '1.',
                'dish_ingredient' : dish_ingredient1,
                'dish_portion' : dish_ingredient1_portion,
            },
            {
                'numbering' : '2.',
                'dish_ingredient' : dish_ingredient2,
                'dish_portion' : dish_ingredient2_portion,
            },
            {
                'numbering' : '3.',
                'dish_ingredient' : dish_ingredient3,
                'dish_portion' : dish_ingredient3_portion,
            },
            {
                'numbering' : '4.',
                'dish_ingredient' : dish_ingredient4,
                'dish_portion' : dish_ingredient4_portion,
            },
            {
                'numbering' : '5.',
                'dish_ingredient' : dish_ingredient5,
                'dish_portion' : dish_ingredient5_portion,
            },
            {
                'numbering' : '6.',
                'dish_ingredient' : dish_ingredient6,
                'dish_portion' : dish_ingredient6_portion,
            },
            {
                'numbering' : '7.',
                'dish_ingredient' : dish_ingredient7,
                'dish_portion' : dish_ingredient7_portion,
            },
            {
                'numbering' : '8.',
                'dish_ingredient' : dish_ingredient8,
                'dish_portion' : dish_ingredient8_portion,
            },
            {
                'numbering' : '9.',
                'dish_ingredient' : dish_ingredient9,
                'dish_portion' : dish_ingredient9_portion,
            },
            {
                'numbering' : '10.',
                'dish_ingredient' : dish_ingredient10,
                'dish_portion' : dish_ingredient10_portion,
            },
            ],
        'dish_instructions' : [
            {
                'numbering' : '1.',
                'dish_instruction' : dish_instruction1,
            },
            {
                'numbering' : '2.',                
                'dish_instruction' : dish_instruction2,
            },
            {
                'numbering' : '3.',
                'dish_instruction' : dish_instruction3,
            },
            {
                'numbering' : '4.',
                'dish_instruction' : dish_instruction4,
            },
            {
                'numbering' : '5.',
                'dish_instruction' : dish_instruction5,
            },
            {
                'numbering' : '6.',
                 'dish_instruction' : dish_instruction6,
            },
            {
                'numbering' : '7.',
                'dish_instruction' : dish_instruction7,
            },
            {
                'numbering' : '8.',
                'dish_instruction' : dish_instruction8,
            },
            {
                'numbering' : '9.',
                'dish_instruction' : dish_instruction9,
            },
            {
                'numbering' : '10.',
                'dish_instruction' : dish_instruction10,
            },
            ],
    })
    
    ''' Upload image file to static folder '''
    dish_image.save(os.path.join(app.config['UPLOAD_FOLDER'], dish_image.filename ))

    return render_template(
        'successful.html', 
        message0 = "Congratulations !",
        message1 = 'Thank you for submitting your {} recipe!'.format(dish_name), 
        message2 ='We will help more tongue taste good food')
        
@app.route('/recipe/<task_id>')
def recipe (task_id) :
    result = data_food_recipe.find_one({
        '_id':ObjectId(task_id)
    })
    return render_template ('recipe.html', data=result)

@app.route('/recipe/edit/<task_id>')
def edit_recipe(task_id):
    result = data_food_recipe.find_one({
        '_id':ObjectId(task_id)
    })
    return render_template('edit_recipe.html', data=result)

@app.route('/recipe/edit/<task_id>', methods=['POST'])
def update_recipe(task_id):
    # Recipe name 
    dish_name = request.form.get('dish_name')
    # Recipe image
    # dish_image = request.files.get('dish_image')
    # Recipe description
    dish_description = request.form.get('dish_description')
    
    # Ingredients
    dish_ingredient1 = request.form.get('dish_ingredient1')
    dish_ingredient2 = request.form.get('dish_ingredient2')
    dish_ingredient3 = request.form.get('dish_ingredient3')
    dish_ingredient4 = request.form.get('dish_ingredient4')
    dish_ingredient5 = request.form.get('dish_ingredient5')
    dish_ingredient6 = request.form.get('dish_ingredient6')
    dish_ingredient7 = request.form.get('dish_ingredient7')
    dish_ingredient8 = request.form.get('dish_ingredient8')
    dish_ingredient9 = request.form.get('dish_ingredient9')
    dish_ingredient10 = request.form.get('dish_ingredient10')
    
    # # Ingredient Portion
    dish_ingredient1_portion = request.form.get('dish_ingredient1_portion')
    dish_ingredient2_portion = request.form.get('dish_ingredient2_portion')
    dish_ingredient3_portion = request.form.get('dish_ingredient3_portion')
    dish_ingredient4_portion = request.form.get('dish_ingredient4_portion')
    dish_ingredient5_portion = request.form.get('dish_ingredient5_portion')
    dish_ingredient6_portion = request.form.get('dish_ingredient6_portion')
    dish_ingredient7_portion = request.form.get('dish_ingredient7_portion')
    dish_ingredient8_portion = request.form.get('dish_ingredient8_portion')
    dish_ingredient9_portion = request.form.get('dish_ingredient9_portion')
    dish_ingredient10_portion = request.form.get('dish_ingredient10_portion')
    
    # # Instructions
    dish_instruction1 = request.form.get('dish_instruction1')
    dish_instruction2 = request.form.get('dish_instruction2')
    dish_instruction3 = request.form.get('dish_instruction3')
    dish_instruction4 = request.form.get('dish_instruction4')
    dish_instruction5 = request.form.get('dish_instruction5')
    dish_instruction6 = request.form.get('dish_instruction6')
    dish_instruction7 = request.form.get('dish_instruction7')
    dish_instruction8 = request.form.get('dish_instruction8')
    dish_instruction9 = request.form.get('dish_instruction9')
    dish_instruction10 = request.form.get('dish_instruction10')
    # Preparation time
    dish_prep_time = request.form.get('dish_prep_time')
    # Cooking time
    dish_cook_time = request.form.get('dish_cook_time')
    # Servings 
    dish_serving = request.form.get('dish_serving')
    # Cusine style
    dish_type = request.form.get('dish_type')
    # Skill level
    dish_skill = request.form.get('dish_skill')
    
    data_food_recipe.update({
        '_id':ObjectId(task_id)
    }, {
        '$set': {
            'dish_name' : dish_name,
            # 'dish_image' : dish_image.filename,
            'dish_description' : dish_description,
            'dish_prep_time' : dish_prep_time,
            'dish_cook_time' : dish_cook_time,
            'dish_serving' : dish_serving,
            'dish_type' : dish_type, 
            'dish_skill' : dish_skill,
            'dish_ingredient': [
                {
                    'numbering' : '1.',
                    'dish_ingredient' : dish_ingredient1,
                    'dish_portion' : dish_ingredient1_portion,
                },
                {
                    'numbering' : '2.',
                    'dish_ingredient' : dish_ingredient2,
                    'dish_portion' : dish_ingredient2_portion,
                },
                {
                    'numbering' : '3.',
                    'dish_ingredient' : dish_ingredient3,
                    'dish_portion' : dish_ingredient3_portion,
                },
                {
                    'numbering' : '4.',
                    'dish_ingredient' : dish_ingredient4,
                    'dish_portion' : dish_ingredient4_portion,
                },
                {
                    'numbering' : '5.',
                    'dish_ingredient' : dish_ingredient5,
                    'dish_portion' : dish_ingredient5_portion,
                },
                {
                    'numbering' : '6.',
                    'dish_ingredient' : dish_ingredient6,
                    'dish_portion' : dish_ingredient6_portion,
                },
                {
                    'numbering' : '7.',
                    'dish_ingredient' : dish_ingredient7,
                    'dish_portion' : dish_ingredient7_portion,
                },
                {
                    'numbering' : '8.',
                    'dish_ingredient' : dish_ingredient8,
                    'dish_portion' : dish_ingredient8_portion,
                },
                {
                    'numbering' : '9.',
                    'dish_ingredient' : dish_ingredient9,
                    'dish_portion' : dish_ingredient9_portion,
                },
                {
                    'numbering' : '10.',
                    'dish_ingredient' : dish_ingredient10,
                    'dish_portion' : dish_ingredient10_portion,
                },
                ],
            'dish_instructions' : [
                {
                    'numbering' : '1.',
                    'dish_instruction' : dish_instruction1,
                },
                {
                    'numbering' : '2.',                
                    'dish_instruction' : dish_instruction2,
                },
                {
                    'numbering' : '3.',
                    'dish_instruction' : dish_instruction3,
                },
                {
                    'numbering' : '4.',
                    'dish_instruction' : dish_instruction4,
                },
                {
                    'numbering' : '5.',
                    'dish_instruction' : dish_instruction5,
                },
                {
                    'numbering' : '6.',
                     'dish_instruction' : dish_instruction6,
                },
                {
                    'numbering' : '7.',
                    'dish_instruction' : dish_instruction7,
                },
                {
                    'numbering' : '8.',
                    'dish_instruction' : dish_instruction8,
                },
                {
                    'numbering' : '9.',
                    'dish_instruction' : dish_instruction9,
                },
                {
                    'numbering' : '10.',
                    'dish_instruction' : dish_instruction10,
                },
                ],
        }
    })    
    
    
    return render_template(
        'successful.html', 
        message0 = "Brillant !",
        message1 = 'We have updated your {} recipe!'.format(dish_name), 
        message2 ='Soup taste better when brewed longer'
        )

@app.route('/recipe/confirm_remove_recipe/<task_id>')
def confirm_remove_recipe(task_id):
    result = data_food_recipe.find_one({
        '_id':ObjectId(task_id)
    })
    return render_template('confirm_remove_recipe.html', data = result)

@app.route('/recipe/remove_recipe/<task_id>/<dish_name>')
def remove_recipe(task_id, dish_name):
    data_food_recipe.delete_one({
        '_id':ObjectId(task_id)
    })
    return render_template('successful.html', 
        message0 = "We just lost one recipe !",
        message1 = 'We have removed your {} recipe!'.format(dish_name), 
        message2 = "Let's look forward to the next better dish !" )

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
