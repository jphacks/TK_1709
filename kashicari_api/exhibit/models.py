from django.db import models

STATUS_AVAILABLE = "available"
STATUS_UNAVAILABLE = "unavailable"
STATUS_SET = (
    (STATUS_AVAILABLE, "レンタル可能"),
    (STATUS_UNAVAILABLE, "貸し出し中"),
)


class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    price = models.IntegerField()  # レンタル価格
    deadline = models.DateField()  # アイテムの返却日
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_AVAILABLE, max_length=11)
    username = models.TextField(default='Yamada')
    category1 = models.CharField(null=True, blank=True, max_length=128)
    category2 = models.CharField(null=True, blank=True, max_length=128)
    category3 = models.CharField(null=True, blank=True, max_length=128)
    category4 = models.CharField(null=True, blank=True, max_length=128)
    category5 = models.CharField(null=True, blank=True, max_length=128)

    def __str__(self):
        return self.name
