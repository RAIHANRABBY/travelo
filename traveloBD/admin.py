from django.contrib import admin
from .models import Dist_info,Tour_places,Gallery_photos,PopulerPlaces

# Register your models here.
admin.site.register(Dist_info)
admin.site.register(Tour_places)
admin.site.register(Gallery_photos)
admin.site.register(PopulerPlaces)
