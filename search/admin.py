from django.contrib import admin
from search import models
# Register your models here.

admin.site.register(models.Movie)
admin.site.register(models.Genre)
admin.site.register(models.Director)
