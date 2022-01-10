from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Company)
admin.site.register(Campaign)

admin.site.register(POISector)
admin.site.register(POIInterests)
admin.site.register(POIJobs)
admin.site.register(POIType)
admin.site.register(POI)
