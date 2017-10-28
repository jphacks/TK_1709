from django.http import JsonResponse
from rest_framework.decorators import api_view

from exhibit.models import Item, STATUS_UNAVAILABLE


@api_view(['POST'])
def rent_item(request):
    try:
        item_id = request.POST['item_id']
        item = Item.objects.get(pk=item_id)
        item.status = STATUS_UNAVAILABLE
        item.save()
        is_complete = True
    except Exception:
        is_complete = False
    return JsonResponse({"is_complete": is_complete})
