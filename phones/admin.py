from django.contrib import admin

# Register your models here.
from phones.models import Phone # Импортируем модели в данный файл


@admin.register(Phone) # регистрация для какой модели данный класс является обязательным

class PhoneAdmin(admin.ModelAdmin): # создаем спец класс-представитель в административной панели
    # list_display = ['id', 'name', 'price', 'image', 'release_date', 'lte_exists', 'slug', ] 
    # prepopulated_fields = {"slug": ("name", )}
   pass