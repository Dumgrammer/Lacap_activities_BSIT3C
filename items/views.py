from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .models import Items
import json

def parse_request_data(request):
    """Parse data from JSON or form-data (multipart/x-www-form-urlencoded)."""
    if request.content_type == 'application/json':
        try:
            return json.loads(request.body)
        except json.JSONDecodeError:
            return None
    elif request.content_type.startswith('multipart/form-data') or request.content_type == 'application/x-www-form-urlencoded':
        return {key: request.POST.get(key) for key in request.POST}
    return None

def auth_checker(func):
    def wrapper(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({"message": "Unauthorized"}, status=401)
        return func(request, *args, **kwargs)

    return wrapper


@auth_checker
@require_GET
def index(request):
    items = list(Items.objects.values())
    return JsonResponse({"message": "Successful", "data": items}, status=200)


@csrf_exempt
@require_GET
def get_item(request, id):
    try:
        item = Items.objects.get(id=id)
        data = {
            "id": item.id,
            "item_name": item.item_name,
            "item_quantity": item.item_quantity,
            "item_price": item.item_price,
        }
        return JsonResponse({"message": "Successful", "payload": data}, status=200)
    except Items.DoesNotExist:
        return JsonResponse({"message": "Item not found"}, status=404)


@csrf_exempt
@require_GET
def search_items(request):
    search_query = request.GET.get("search", "")  # Get the 'search' query parameter
    if not search_query:
        return JsonResponse({"message": "Please provide a search term"}, status=400)

    items = Items.objects.filter(item_name__icontains=search_query).values()
    return JsonResponse({"message": "Search results", "data": list(items)}, status=200)

@csrf_exempt
@require_POST
def add_item(request):
    data = parse_request_data(request)
    if data is None:
        return JsonResponse({"message": "Invalid request format"}, status=400)

    try:
        item = Items.objects.create(
            item_name=data.get("item_name"),
            item_quantity=data.get("item_quantity", ""),
            item_price=data.get("item_price")
        )

        item_data = {
            "id": item.id,
            "item_name": item.item_name,
            "item_quantity": item.item_quantity,
            "item_price": item.item_price,
            "created_at": item.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": item.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

        return JsonResponse({"message": "Item created", "data": item_data}, status=201)
    except Exception as e:
        return JsonResponse({"message": "Error", "error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PATCH", "PUT"])
def update_item(request, id):
    data = parse_request_data(request)
    if data is None:
        return JsonResponse({"message": "Invalid request format"}, status=400)

    try:
        item = Items.objects.get(id=id)

        if request.method == "PUT":
            item.item_name = data["item_name"]
            item.item_quantity = data["item_quantity"]
            item.item_price = data["item_price"]
        elif request.method == "PATCH":
            item.item_name = data.get("item_name", item.item_name)
            item.item_quantity = data.get("item_quantity", item.item_quantity)
            item.item_price = data.get("item_price", item.item_price)

        item.save()
        return JsonResponse({"message": "Item updated successfully"}, status=200)
    except Items.DoesNotExist:
        return JsonResponse({"message": "Item not found"}, status=404)
    except KeyError:
        return JsonResponse({"message": "Missing required fields"}, status=400)
    except Exception as e:
        return JsonResponse({"message": "Error", "error": str(e)}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, id):
    try:
        item = Items.objects.get(id=id)
        item.delete()
        return JsonResponse({"message": "Item deleted successfully"}, status=200)
    except Items.DoesNotExist:
        return JsonResponse({"message": "Item not found"}, status=404)