from django.contrib import admin
from .models import City, Language, Vacancy

# Register your models here.
admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
