# Backendify

The application is a generic backend service built using Django Rest Framework (DRF) that provides authentication and post services.The authentication services handle user registration, login, and user management, including the ability to create super-users with additional privileges. The users are authenticated through a secure token based mechanism.The post services in the application enable users to perform CRUD operations on posts. Users can create new posts, retrieve existing posts, update post details, and delete posts when necessary. These services provide a flexible and scalable way to manage and interact with posts within the application.This application also leverages google drive storage as a cloud database service alongside the default database.

Overall, this application provides a solid foundation for building various types of backend services, with a focus on user authentication and post management, leveraging Django Rest Framework and Google's service account for cloud storage functionality.

# Database

To integrate the google drive storage functionality with DRF , follow this blog  : [Django-GDrive](https://django-googledrive-storage.readthedocs.io/en/latest/)

Create the database :  
`python manage.py makemigreations` \
`python manage.py migrate` 


# Endpoints 
Run the server :    
 `python .\manage.py runserver` 

Here are the API endpoints from our backend service :

## Auth

- ### <span style="color:green"> /auth/register  

    Use : `To register a user` \
    Format :  `POST Request`

        {
            "name": "Subham",
            "email": "subhamsubhasis2002@gmail.com",
            "password": "***"
        }
        
- ### <span style="color:green"> /auth/super-register  

    Use : `To register a super-user` \
    Format :  `POST Request`

        {
            "name": "Subham-admin",
            "email": "subhamsubhasis2002@gmail.com",
            "password": "***"
        }


- ### <span style="color:green"> /auth/login
    Use : `To login , Obtain the token from response for future usage` \
    Format : `POST Request`

        {
            "email": "subhamsubhasis2002@gmail.com",
            "password": "***"
        }

- ### <span style="color:green"> /auth/forgot-password  

    Use : `To register a user` \
    Format :  `POST Request`

        {
            "email": "subhamsubhasis2002@gmail.com",
            "password": "newpassword"
        }

- ###  <span style="color:green"> /auth/delete-user

    Use : `To register a user` \
    Format :  `POST Request`

        {
            "email": "subhamsubhasis2002@gmail.com",
        }

- ### <span style="color:green"> /auth/all-users

    Use : `To get all users info` \
    Format :  `GET Request`

- ### <span style="color:green"> /auth/all-users/< email >

    Use : `To get user info` \
    Format :  `GET Request`


- ### <span style="color:green"> /auth/update-profile/< email >

    Use : `To register a user` \
    Format :  `POST Request (Name and profile pic)`

        Format for token in Header :
        Authorization: "Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIwMjBjc2IxMzE3QGlpdHJwci5hYy5pbiIsImV4cCI6MTY4MDgyMDgwNH0.wgsupH5q67u5qjo_pHSe71OHolP2S2iEjUwjEVSFgSk"

-----

## Posts

- ### <span style="color:green"> /post/post/

    Use : `To view and add posts` \
    Permission : \
        `GET - Everyone` \
        `POST - After authentication`

        Format for token in Header :

        Authorization: "Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIwMjBjc2IxMzE3QGlpdHJwci5hYy5pbiIsImV4cCI6MTY4MDgyMDgwNH0.wgsupH5q67u5qjo_pHSe71OHolP2S2iEjUwjEVSFgSk"

- ### <span style="color:green"> /post/post/delete-post/id

    Use : `To delete post by id` \
    Permission : \
        `GET - After authentication`

        Format for token in Header :

        Authorization: "Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIwMjBjc2IxMzE3QGlpdHJwci5hYy5pbiIsImV4cCI6MTY4MDgyMDgwNH0.wgsupH5q67u5qjo_pHSe71OHolP2S2iEjUwjEVSFgSk"

- ### <span style="color:green"> /post/post/< chapterName > 

    Use : `To get all posts by chapter name` \
    Permission : `All can get it (GET request)`

- ### <span style="color:green"> /post/post/id/< id >

    Use : `To get post by id` \
    Permission : \
        `GET - Everyone` \
        `POST,PUT - Teacher after logging in through token` 

        Format for token in Header :

        Authorization: "Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIwMjBjc2IxMzE3QGlpdHJwci5hYy5pbiIsImV4cCI6MTY4MDgyMDgwNH0.wgsupH5q67u5qjo_pHSe71OHolP2S2iEjUwjEVSFgSk"

- ### <span style="color:green"> /post/post/like/id/< id > 

    Use : `To get likes , dislikes, liked_users, disliked_users, post by id` \
    Permission : \
        `GET - Everyone` \
        `PUT - Everyone`  

# Deployment

### Step 1: Set up the Server

1. Choose a server or hosting provider that supports Python and Django. Some popular options include:
   - [Heroku](https://www.heroku.com/)
   - [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)
   - [DigitalOcean](https://www.digitalocean.com/)
   - [PythonAnywhere](https://www.pythonanywhere.com/)

2. Follow the provider's instructions to set up a new server or application instance. Make sure to configure it with the necessary Python version and dependencies.

3. If using a cloud provider, set up any required environment variables or configuration settings. These may include database credentials, secret keys, or any other custom settings specific to your application.


-----

### Step 2: Prepare the Application


1. Make sure your application is production-ready by performing the following steps:
   - Set `DEBUG = False` in your Django settings.
   - Configure your application to use a production database (e.g., PostgreSQL).
   - Update any sensitive information such as secret keys or database credentials to use environment variables.
   - Run thorough testing to ensure your application functions as expected.

2. Create a requirements file (`requirements.txt`) that lists all the Python packages required by your application. Use the command `pip freeze > requirements.txt` to generate this file.

-----

### Step 3: Prepare the Environment

1. Connect to your server using SSH or the provider's provided method.

2. Clone your Django Rest Framework project repository to your server machine using Git: `git clone <repository-url>`.

3. Create a virtual environment and install the required Python packages using the command `pip install -r requirements.txt`.

4. Run the Django database migrations: `python manage.py migrate`.

5. If applicable, load initial data or create a superuser account using Django management commands.

-----


### Step 4: Configuring GUNICORN and NGINX

Follow this blog for detailed steps : [Deployment](https://realpython.com/django-nginx-gunicorn/)






