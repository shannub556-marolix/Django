from django.contrib import admin



from .models import User_Details

class DetailsAdmin(admin.ModelAdmin):
    list_display = ['username','password']

admin.site.register(User_Details,DetailsAdmin)
