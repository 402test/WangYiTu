from django.contrib import admin

# Register your models here.
from multi.models import Multi_M

class Multi_M_Admin(admin.ModelAdmin):
    search_fields = ('multi_name','multi_s','music_type')

admin.site.register(Multi_M,Multi_M_Admin)
