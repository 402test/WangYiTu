from django.contrib import admin


from user.models import UserProfile,EmailVerifyRecord
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    pass


class EmailVerifyRecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)