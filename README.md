# PROJECT 3 : FOOD RECIPE

### Objective :   
    To build a database to share food recipe and allow user to upload a new recipe, edit and remove an existing recipe.

#### SCOPE
The website allows User to :
    
    CREATE
    * submit a new recipe
    READ
    * read and display all job posting from databases
    UPDATE
    * edit and update an existing recipe
    DELETE
    * select and remove an existing recipe

#### Demo
    A live demo can be found here. https://thirdproject-foodrecipe.herokuapp.com/

#### UX
    My Considerations for the website:
    * user able to submit, make changes and remove a recipe on the website
    * easy for user to navigate and simple to read the details

#### Technologies
    1. HTML
    2. CSS
    3. Bootstrap (3.3.7)
    4. MongoDB
    5. Python 3
    6. Flask
    7. Jinja

#### Features
				
**My Design of the site :**

    * Easy for user to navigate and read and share recipe
    
    Limitations: 
    * no function for user to login
    * search function not implement due to time limitation
    * Social media links not link not set up

#### Testing
Manual Testing is done to ensure that the all functions are functional.
Test Results as follows :

*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1 | `On the Landing Page, click on the "Submit a recipe" in navbar`| `Link to the submission of new recipe page and show entry form`| **Pass** 
2 | `Enter the details in form and submit`|`Render successful submission page with success message passed over` | **Pass** 
3 | `Click on the thumbnail of the recipe to select and display the full detail for the selected recipe`|`display the full detail of the recipe` | **Pass** 
3a | `In recipe page> Click "Edit" link on top right of page`|`Show form with details of selected recipe and allow user to enter new info or upload new image` | **Pass** 
3b | `Click "Update the flavor now" to save the changes`|`Render successful submission page with success message passed over` | **Pass** 
4a | `In recipe page> Click "Remove" link on top right of page`|`Render page to check with user if the removal of the selected recipe is final` | **Pass** 
4b | `Click "Yes I am sure. Proceed to go back to landing`|`Render successful submission page with success message passed over` | **Pass** 
5 | `In recipe page> Click "Home" link on top right of page`|`Return to landing page` | **Pass** 
6 | `In successful page> Click "Cook it" button`|`Return to landing page` | **Pass** 

#### Deployment
This site is hosted using Heroku App Link : 
_https://dashboard.heroku.com/apps/thirdproject-foodrecipe_

    All codes are uploaded to GitHub and links are made to Heroku by installing in bash terminal in projects.
    Regular commits are push to the Github subsequently push to heroku to deploy.
    .gitignore file is added to remove files that are not required or files that we do not wish to be uploaded to Github

_Deploy Heroku:_

    i) Install Heroku using bash
    ii) Login to Heroku
    iii) Install gunicorn
    iv) Create Procfile and requirements.txt
    V) Commit and push to Heroku 
    vi) Set up the Environment Vasriables
    vii) Update Dependencies


#### Credits
    Uses W3School for many reference (https://www.w3schools.com/)
    Uses fontawesome for the social media icons (https://fontawesome.com/)
    Uses Bootstrap for templates (https://getbootstrap.com/)

 