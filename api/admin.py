from django.contrib import admin
from api.models import Donor, BloodCenter, History, GetName

admin.site.register(Donor)
admin.site.register(BloodCenter)
admin.site.register(History)
admin.site.register(GetName)