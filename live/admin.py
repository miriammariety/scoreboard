from django.contrib import admin
from .models import Event, Cluster, Scores
# Register your models here.
admin.site.register(Event)
admin.site.register(Cluster)
admin.site.register(Scores)