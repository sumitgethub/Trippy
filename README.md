Trip Booking App
This project is a Trip Booking Application built using Django. The application supports two types of users: Admin and Customer. It provides functionalities such as package booking for customers and package management for admins. The app uses authentication and authorization to manage access to various features.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/trip-booking-app.git
cd trip-booking-app
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser for accessing the admin panel:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Usage
Access the admin panel at http://127.0.0.1:8000/admin/ to manage hotels and packages.
Use the API endpoints described below to interact with the application.


1st Account Apis 
a>  http://127.0.0.1:8000/users/rolelist/    #this is role list apis there are two type of roles right now 1 Admin 2 Customer
b> http://127.0.0.1:8000/users/register/   #this is regitser api for customer and Admin
c> http://127.0.0.1:8000/users/register/    #this is same login api 


2nd Admin Apis
a> http://127.0.0.1:8000/trip/hotels/    #create-hotel
b> http://127.0.0.1:8000/trip/packages/ #create package
c> http://127.0.0.1:8000/trip/images/ #add image in package
d> http://127.0.0.1:8000/trip/packages/1/  #edit package
e> http://127.0.0.1:8000/trip/packages/1/ #delete package


3rd Customer Apis
a> http://127.0.0.1:8000/trip/packages/ #get all package
b> http://127.0.0.1:8000/trip/packages/1/  #get single package
c> http://127.0.0.1:8000/trip/Booking/ #package booking api
d> http://127.0.0.1:8000/trip/reviews/ #add rating and review api





