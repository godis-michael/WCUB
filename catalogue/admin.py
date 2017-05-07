from django.contrib import admin
from catalogue import models

myModels = [models.Bancnote, models.Subscriber]

admin.site.register(myModels)
