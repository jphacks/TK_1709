import codecs
import csv
import os
from kashicari_api import settings
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Item
from .serializer import ItemSerializer
from ntt import morpho


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        data_dict = request.data.copy()

        # category取得
        categories = morpho.get_categories(data_dict['name'])
        if len(categories) < 5:
            des_categories = morpho.get_categories(data_dict['description'])
            categories.extend(des_categories)
        print('categories')
        print(categories)

        # 事前に用意したリストにマッチするカテゴリーのみを取得
        categories = extract_category(categories)
        print('matched categories')
        print(categories)

        # マッチしたカテゴリーを登録
        data_dict = insert_categories(data_dict, categories)

        serializer = self.get_serializer(data=data_dict)
        serializer.is_valid(raise_exception=True)
        # print('serializer')
        # print(serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def extract_category(categories):
    path = os.path.join(settings.BASE_DIR, 'exhibit/item.csv')
    item_list = codecs.open(path, 'r', 'utf-8').readline().split(',')
    # print('item_list')
    # print(item_list)

    matched_categories = []

    for category in categories:
        if category in item_list and category not in matched_categories:
            matched_categories.append(category)

    return matched_categories


def insert_categories(data_dict, categories):
    for i in range(len(categories)):
        key = 'category' + str(i+1)
        data_dict[key] = categories[i]

    return data_dict
