# Django_Asynchronous_Project

Welcome to the Image Analysis and Commenting Platform Django application! This platform allows users to upload images for analysis, view analyzed images with descriptions, and add/view comments to these images. The application also supports infinite scrolling for both images and comments.

First, you must ensure that django is installed in your computer, which can be achieved using the command below:
   pip install django
I created a new django project, navigated to the project directory, and created a new django app using the three respective commands below:
	django-admin startproject image_platform
	cd image_platform
	python manage.py startapp image_api
These commands gave the respective folders and files for the app.

Django uses migrations to propagate changes you make to your models (adding a new model, changing a field, etc.) into the database schema. 
In order to achieve this, I used the following commands:
# Create migrations
python manage.py makemigrations

# Apply migrations to create database tables
python manage.py migrate

This created the necessary tables for your models (AnalyzedImage and Comment) in the database.
In order to access the Django admin interface, I created the superuser account with the following details:
username: admin
email: newyear@gmail.com
password: 12345

To run the developmet server for the django application in windows: 
1. Open the directory where your file is found.
2. Type cmd on the path to open the command prompt.
3. Apply migrations using the following commands:
	python manage.py makemigrations
	python manage.py migrate
4. Run the Development Server using the command below:
	python manage.py runserver
5. Access the Development Server by typing this in your browser while the server is running:
	http://127.0.0.1:8000/admin/
6. Use the cridentials given above to access the admin interface.

Configure External Image Analysis API (Using Google Cloud Vision API)

The app uses Google Cloud Vision API to configure external image analysis. I created a service account key and downloaded the JSON file using the process below:
	In the GCP Console, go to "APIs & Services" > "Credentials."
	Click on "Create Credentials" and choose "Service account key."
	Create a new service account.
	Choose a role with sufficient permissions (I choose Editor).
	Create the key and download the JSON file.
The downloaded JSON file is attached in the directory and linked with the app. This is configured in settings.py using GOOGLE_CLOUD_VISION_CREDENTIALS = JSON file path.
After this, I updated the image analysis view.py file to include image analysis using the Google Cloud Vision API

Implement Infinite Scroll:
In the settings.py, I added aconfiguration that sets up the default pagination class to PageNumberPagination and specifies that each page will contain 10 items. I also Updated the API views to use pagination.

Response Handling:
In views, I customized how the responses are formatted. I modified the AnalyzedImageSerializer in the views.py to include the image URL and description in the response.

Error Handling:
I implemented error handling in the views to provide meaningful responses for various scenarios. For example, in my app, if an exception occurs during the creation of the image instance or the analysis process, it returns a 500 Internal Server Error response with an error message.

Testing:
I included the various tests for API Endpoint and External Service Integration.
To run the tests, open the command prompt or terminal with the path directory of your files and run the command below:
	python manage.py test
