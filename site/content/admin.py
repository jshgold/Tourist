from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display= ('spot','dep','yea','mont')

admin.site.register(Content,ContentAdmin)
