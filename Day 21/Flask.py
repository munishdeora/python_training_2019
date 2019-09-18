# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:04:31 2019

@author: de
"""

Flask - A lightweight micro framework that helps to create web apps.
Web Server Gateway Interface(WSGI) - a simple calling convention for web servers to forward requests to web applications or frameworks
Jinja2(template engine), redis(database), Werkzeug(WSGI toolkit).
Backend Web Development , used to deploy machine learning model


# Working of Flask
1. create a folder named "Flask_demo" and perform all your flask working here
2. create a file named "app.py" in the "Flask_demo" folder

Flask_demo
  |--app.py

a. Normal Web App
---------------------------------------------------------------------
1. from flask import Flask
flask is a module that contains all the plugins that is used to create a web app
Flask is a class that is needed to be imported for further functionality.

2. app = Flask(__name__)
an instance or object of Flask class. __name__ is needed so that Flask knows where to look for templates, static files, and so on.

3. @app.route("/hello")  - decorator to tell Flask what URL should trigger our function.

4. app.run() -  to trigger our web app
5. debug = True - to handle any changes made in our application during development process. Not to use at the time of deployment

------------------------------------------------------------------------------
Linking Html Page
-----------------------------------------------------------
To display html file on the flask web app

1. Create a folder named "templates" in the Flask_demo folder to store the html file.
Note - All the html files will be stored here and folder name should be templates(any other name will raise error)


Flask_demo
  |--app.py
  |--templates
     |-- demo.html

2. Creating a file demo.html and storing it in templates
3. To use the demo.html file import render_template and return render_template(filename) in the function to display the html page

4. To add any style , image , or using another file is also possible and to store them we should have a folder named static. So create one -

Flask_demo
  |--app.py
  |--templates
     |-- demo.html
  |--static
     |--demo.css
     |--demo.py

--------------------------------------------------------------------------------------
To handle request method
1. Importing request
2. Adding methods in route()
3. Providing the conditions
--------------------------------------------------------------------------------------

Dynamic Web App

Using JINJA2 template and many more
{{}}
{% %}
---------------------------------------------------------------------------------------
Last Task-
To take data from a form and validate it

1. Create a form in html which accept name
2. import url_for which is used to render the form data to our app.py
3. request.form help to access the form data
4. Created a python file that contain a function to check whether the name entered is
   in correct format or not using regex

5. Import the python file and send the name entered in the form in the function
5. Showing the response in the response page
----------------------------------------------------------------------------------------
