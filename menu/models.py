from django.db import models

# Menu Model
'''
This model will be used to create item(food/beverage) with the following field:
    item name
    item description
    item price
    image(maybe)
'''

class Menu(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.item_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"