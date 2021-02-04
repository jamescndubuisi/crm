from django.db import models
import uuid
# Create your models here.


class Customer(models.Model):
    # id = models.UUIDField(default=uuid.uuid4())
    name = models.CharField(max_length=50,  null=True)
    phone = models.CharField(max_length=50,  null=True)
    email = models.CharField(max_length=50,  null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),

    )
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    tags = models.ManyToManyField("Tag")
    category =models.CharField(max_length=50,  null=True, choices=CATEGORY)
    description = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Out for Delivery", "Out for Delivery"),
        ("Delivered", "Delivered"),
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=30, null=True, choices=STATUS)
    note = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.product.name




class Tag(models.Model):
    # id = models.UUIDField(default=uuid.uuid4())
    name = models.CharField(max_length=50,  null=True)


    def __str__(self):
        return self.name







