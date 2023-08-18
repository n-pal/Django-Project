from django.contrib import admin

# Register your models here.
from E_Shop.models import *
# Register your models here.
class UserDisplay(admin.ModelAdmin):
    list_display = ["name","email", "address", "password"]
    list_filter = ["name", "address"]
    search_fields = ["name", "number"]
class CategoryDisplay(admin.ModelAdmin):
    list_display = ["CategoryName"]
class ProductDisplay(admin.ModelAdmin):
    list_display = ["name", "price", "quantity", "description"]
admin.site.register(UserRegister, UserDisplay)
admin.site.register(Category, CategoryDisplay)
admin.site.register(Product, ProductDisplay)

admin.site.register(Contactus)

class Orderdisplay(admin.ModelAdmin):
    list_display=['userid','productid','price','datetime']
admin.site.register(Order,Orderdisplay)