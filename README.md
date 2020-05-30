# PROJECT 3 : FOOD RECIPE WEBSITE

### Objective :   
To build a sharing platform for everyone to share their cooking recipe. It is where everyone can search for cooking ideas and build a community for like-minded people to connect, share and enjoy the possibility of good food in the world.
#### UX

For my user,

    * they are able to share their recipe
    * they are able to edit and remove their recipe
    * they are able to share with the friends via social media 
    * they are able to create their own account and create a profile (future development)
    * they can set up their own fan club (future development)
    
For my browser,

    * they are able to find their choice of recipe 
    * they are able to leave message and discuss with the owner of the recipe
    * they are able to join and create interest-groups
    
For advertisers,

    * they are able to host the advertisement on our website
    * they are able to tap on our strong network of users to market their product
    
For us,

    * we are to build and grow our users
    * we are to generate revenue through advisement and sponsors 
    * we are able to refer the business to related business
    
    
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
1a | `NAVBAR : click 'HOME'`| `Goto Home page and display logo, turning wok and editor's choice of 3 recipes`| **Pass** 
1b | `NAVBAR : click 'HOW TO'`|`Display full list of all recipes` | **Pass** 
1c | `NAVBAR : click 'SUBMIT RECIPE'`|`Show a form for user to enter new recipe` | **Pass** 
1c | `-> SUBMIT RECIPE page : click on the 'Submit Recipe' button`|`Create recipe and goto 'HOW TO' page` | **Pass** 
1d | `NAVBAR : click 'CONTACT US'`|`bring page to footer of page to show contact and email ` | **Pass** 
2 | `HOME page : click on the pic of a recipe`|`Show full details of a recipe` | **Pass** 
3 | `HOW TO page : click on the pic of a recipe`|`Show full details of a recipe` | **Pass** 
4a | `RECIPE page : click on the 'Edit Recipe (top right side)' button`|`Display form with recipe details for editing` | **Pass** 
4b | `-> EDIT page : click on the 'Update the flavor now' button`|`Update the changes and render display 'HOW TO' page` | **Pass** 
4c | `RECIPE page : click on the 'Remove' button (top right side)`|`Show message to ask user to confirm the deletion` | **Pass** 
4d | `-> CONFIRM DELETE page : click on the 'Delete Recipe' button`|`remove from database and render display 'HOW TO' page`  | **Pass** 

#### Deployment
This site is hosted using Heroku App Link : 
_https://dashboard.heroku.com/apps/thirdproject-foodrecipe_

    The website is deployed on Github 
    Regular commits are made and once finalised.
    Below are the commands to initalise and make regular commits, enter the commands in bash terminal in AWS
        * git init .
        * git add . 
        * git commit -m "Commit Message"
        * git remote add origin https://github.com/tattoochan/my-first-website.git
        * git push -u origin master   
 
_Deploy Heroku:_

    i) Install Heroku using bash
    ii) Login to Heroku
    iii) Install gunicorn
    iv) Create Procfile and requirements.txt
    V) Commit and push to Heroku 
    vi) Set up the Environment Variables
    vii) Update Dependencies


#### Credits

    * Uses W3School for many reference (https://www.w3schools.com/)
    * Uses fontawesome for the social media icons (https://fontawesome.com/)
    * Uses Bootstrap for templates (https://getbootstrap.com/)
    
#### Media

    * pictures and information are extracted from http://themeatmen.sg/
    * some images extracted from https://www.pngguru.com/