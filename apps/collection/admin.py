from django.contrib import admin
from collection.models import Collection_M
# Register your models here.
class Collection_MAdmin(admin.ModelAdmin):
    pass
admin.site.register(Collection_M,Collection_MAdmin)