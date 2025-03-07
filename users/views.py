from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.http import require_http_methods

from .models import User
import json

def auth_checker(func):
    def wrapper(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({"message": "Unauthorized"}, status=401)
        return func(request, *args, **kwargs)
    return wrapper

# Create your views here.
@auth_checker
@require_GET
def index(request):
    users = list(User.objects.values())
    return JsonResponse({"message": "Successful", "data": users}, status=200)

@csrf_exempt
@require_GET
def get_user(request, id):
    data = [
        {
         "id": id,
        "username": "Karl"
        }
    ]
    return JsonResponse({"message": "Successful", "payload": data}, status=200)

@csrf_exempt
@require_GET
def get_user(request, id):
    try:
        user = User.objects.get(id=id)
        data = {
            "id": user.id,
            "firstname": user.firstname,
            "middlename": user.middlename,
            "lastname": user.lastname,
            "email": user.email,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
        }
        return JsonResponse({"message": "Successful", "payload": data}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

@csrf_exempt
@require_POST
def add_user(request):
    try:
        data = json.loads(request.body)  # Read JSON body
        user = User.objects.create(
            firstname=data.get("firstname"),
            middlename=data.get("middlename", ""),
            lastname=data.get("lastname"),
            email=data.get("email"),
        )

        user_data = {
            "id": user.id,
            "firstname": user.firstname,
            "middlename": user.middlename,
            "lastname": user.lastname,
            "email": user.email,
            "created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": user.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

        return JsonResponse({"message": "User created", "data": user_data}, status=201)
    except Exception as e:
        return JsonResponse({"message": "Error", "error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PATCH", "PUT"])
def update_user(request, id):
    try:
        data = json.loads(request.body)
        user = User.objects.get(id=id)

        if request.method == "PUT":
            # Full update: Require all fields to be provided
            user.firstname = data["firstname"]
            user.middlename = data["middlename"]
            user.lastname = data["lastname"]
            user.email = data["email"]
        elif request.method == "PATCH":
            # Partial update: Update only provided fields
            user.firstname = data.get("firstname", user.firstname)
            user.middlename = data.get("middlename", user.middlename)
            user.lastname = data.get("lastname", user.lastname)
            user.email = data.get("email", user.email)

        user.save()

        return JsonResponse({"message": "User updated successfully"}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)
    except KeyError:
        return JsonResponse({"message": "Missing required fields"}, status=400)
    except Exception as e:
        return JsonResponse({"message": "Error", "error": str(e)}, status=500)


@csrf_exempt
@require_http_methods('DELETE')
def delete_user(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse({"message": "User deleted successfully"}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)
