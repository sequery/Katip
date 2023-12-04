from django.db import models
from users.models import User
from django.urls import reverse
from django import template

register = template.Library()

class Food_Category(models.Model):
    title = models.JSONField()
    description = models.TextField(max_length=255, null=False)
    image = models.ImageField(upload_to='Category_Images/', default='Category_Images/default.jpeg')
    drink_category = models.BooleanField(default=False)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Food_Categories'
        ordering = ['created']


    @property
    def food_count(self):
        return Food.objects.filter(category = self).count()

    def __str__(self):
        return '{}'.format(self.title['tm'])


class Food(models.Model):
    title = models.JSONField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Food_Images/')
    category = models.ForeignKey(Food_Category, on_delete=models.CASCADE)
    discount = models.IntegerField(null=True, blank=True)
    discount_unit = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.title['tm'])

    @property
    def food_size(self):
        return Food_Size.objects.filter(food = self)


class Food_Size(models.Model):
    title = models.JSONField()
    food = models.ForeignKey(Food, related_name='food_size', on_delete=models.CASCADE)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.title['tm'])



class Hall(models.Model):
    title = models.JSONField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created']

    @property
    def table_count(self):
        return Table.objects.filter(hall = self).count()

    def __str__(self):
        return '{}'.format(self.title['tm'])



class Table(models.Model):
    number = models.IntegerField()
    hall = models.ForeignKey(Hall, related_name='table', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    reserve_time = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.number)



class Waiter(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default='Unnamed')
    surname = models.CharField(max_length=255, null=False, blank=False, default='Unnamed')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)

class Order(models.Model):
    code = models.CharField(max_length=255, null=False, default='Invalid')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE)
    cost = models.FloatField(null=False, blank=False, default='Unrecorded')
    discount = models.FloatField(null=False, blank=False, default=0)
    service_cost = models.FloatField(null=False, blank=False, default=0)
    total_cost = models.FloatField(null=False, blank=False, default='Unrecorded')
    paid = models.FloatField(null=False, default=False)
    bill_taken = models.BooleanField(null=False, default=False)
    takeaway = models.BooleanField(null=False, default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.code)




class Order_Items(models.Model):
    order = models.ForeignKey(Order,related_name = 'order_items', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_size = models.ForeignKey(Food_Size, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default='Unrecorded')
    discount = models.FloatField(null=False, blank=False, default=0)
    cost = models.FloatField(null=False, blank=False, default='Unrecorded')
    total_cost = models.FloatField(null=False, blank=False, default='Unrecorded')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    @register.simple_tag()
    def multiply(qty, unit_price, *args, **kwargs):
        return qty * unit_price
