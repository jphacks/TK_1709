from .split_images import split_object
from rest_framework.decorators import api_view
from django.http import JsonResponse
from boto3.session import Session
import cv2
import uuid
from django.conf import settings
import numpy as np
import base64

# Create your views here.
@api_view(['POST'])
def split_image(request):
    imgs = split_object(request.POST['img'])
    file_urls = []

    for img in imgs:
        byte_img = cv2.imencode('.png', img)[1].tobytes()
        AWS_ACCESS_KEY = settings.STATIC_SETTINGS['AWS_ACCESS_KEY_ID']
        AWS_SECRET_ACCESS_KEY = settings.STATIC_SETTINGS['AWS_SECRET_ACCESS_KEY']
        session = Session(aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='ap-northeast-1')
        s3 = session.resource('s3')
        bucket = s3.Bucket('kashicari')
        filename = str(uuid.uuid4()) + '.png'
        bucket.put_object(Key=filename, Body=byte_img)
        object_acl = s3.ObjectAcl('kashicari', filename)
        object_acl.put(ACL='public-read')

        file_urls.append('https://s3-ap-northeast-1.amazonaws.com/kashicari/'+filename)

    return JsonResponse({'file_urls': file_urls})