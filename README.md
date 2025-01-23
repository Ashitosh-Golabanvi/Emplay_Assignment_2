Install dependencies: pip install django
Run database migrations: python manage.py migrate
Start the server: python manage.py runserver


URLS To Test API In POSTMAN:
* Status Http Method(Post): http://127.0.0.1:8000/status/
* SignUp Http Method(Get) : http://127.0.0.1:8000/signup/
* SignIn Http Method(Get): http://127.0.0.1:8000/signin/
* SignOut Http Method(Post): http://127.0.0.1:8000/signout/
* Profile Http Method(Post): http://127.0.0.1:8000/profile/

Inputs For Following Endpoints:
* For Sign-Up:
{
  "username": "testuser",
  "password": "testpass",
  "email": "test@example.com"
}


* For Sign-In:
{
    "username": "testuser",
    "password": "testpass"
}
