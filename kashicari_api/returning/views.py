import base64
import requests

from django.http import JsonResponse
from rest_framework.decorators import api_view

from exhibit.models import Item, STATUS_AVAILABLE


@api_view(['POST'])
def return_item(request):
    binary_image = base64.b64decode(request.POST['image'])  # デコードしてバイナリデータにする
    item_id = request.POST['item_id']

    is_complete = validate_image(binary_image)
    if is_complete:  # 正しい商品が返却されていた場合は、dbのstatusを変える
        item = Item.objects.get(pk=item_id)
        item.status = STATUS_AVAILABLE
        item.save()
    return JsonResponse({"is_complete": is_complete})


# NECの高速画像検索APIでimageが登録されているか調べるメソッド
def validate_image(binary_image):
    GROUP_ID = 1068
    files = {'image': binary_image}
    url = "https://www3.arche.blue/mvp5/v1/%d/search" % GROUP_ID
    res = requests.post(url, files=files)
    if res.status_code == 200:
        data = res.json()
        score = data[0]['score']
        if score > 0.30:
            return True
        else:
            return False
    else:
        return False  # NOTE: サーバー側の時の対処考える
