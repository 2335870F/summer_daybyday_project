# summer_daybyday_project

Summer project to further develop skills learned in Web Application Development class:


This web application is called The Think Tank. Its purpose is to allow users to upload 
information about their courses at university all in one place. Unlike moodle, 
this is a place to store all of your current plans, from university work to plans at the 
weekend to grocery lists. Users can create 'entries' which are forms
the user can edit.
Users can register for The Think Tank, allowing them to create a username, add entries, and 
add progress reports and ratings to their own entries to measure how well they are keeping up with
their tasks, as well as suggest a category to us that they feel is missing! Users are 
able to customise their profile by uploading a personalised bio to make the page more 
friendly and fun, and by adding a profile picture. 
Users can only navigate their own categories and entries when signed in, so the anonymous
user will not find there is much to do. Anonymous users can however of course sign in or 
sign up, or read the About Us page for more information.


How To Run:<br/>
<br/>
python manage.py makemigrations<br/>
python manage.py migrate<br/>
python populate_script.py<br/>
python manage.py runserver<br/>

The site is available on https://localhost:8000






