import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import CustomUser


@csrf_exempt
def signup(request):
    """
    Handles user signup by validating input and creating a new user.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            # Validate email format
            try:
                validate_email(email)
            except ValidationError:
                return JsonResponse({'error': 'Invalid email format'}, status=400)

            # Check for existing users
            if CustomUser.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)
            if CustomUser.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)

            # Create the user
            CustomUser.objects.create_user(username=username, password=password, email=email)
            return JsonResponse({'message': 'User created successfully'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@csrf_exempt
def signin(request):
    """
    Handles user sign-in by authenticating and logging in the user.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Validate input
            if not username or not password:
                return JsonResponse({'error': 'Username and password are required'}, status=400)

            # Authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                if not user.is_active:
                    return JsonResponse({'error': 'Account is inactive'}, status=403)
                login(request, user)
                return JsonResponse({'message': 'Logged in successfully'}, status=200)

            return JsonResponse({'error': 'Invalid credentials'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)


@login_required
def user_profile(request):
    """
    Retrieves and returns the profile information of the logged-in user.
    """
    user = request.user
    return JsonResponse({
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name
    }, status=200)


@csrf_exempt
def signout(request):
    """
    Logs out the current user.
    """
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'User is not logged in'}, status=401)

        logout(request)
        return JsonResponse({'message': 'Logged out successfully'}, status=200)

    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
