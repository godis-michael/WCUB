from django.contrib import admin
from catalogue import models

myModels = [models.Bancnote, models.Subscriber, models.Article]

admin.site.register(myModels)
