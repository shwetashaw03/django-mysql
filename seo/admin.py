from django.contrib import admin
from django.utils.html import format_html
from .models import *
from .svg import correct, wrong

# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    fields = ['site', ('link', 'active'), 'icon']
    list_display = ['site', 'status', 'logo']

    def status(self, obj):
        if(obj.active):
            return format_html(correct())
        else:
            return format_html(wrong())

    def logo(self, obj):
        dim = '20px'
        return format_html(f'<img src="/media/{obj.icon}" width={dim} height={dim}/>')


class WebsiteAdmin(admin.ModelAdmin):
    fields = ['name', 'url', 'tagline', ('email', 'mobile'), 'address', 'logo']
    list_display = ['name', 'email', 'logo']

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        val = Website.objects.all()
        if(val):
            return False
        else:
            return True

    # This will help you to disable delete functionaliyt
    # def has_delete_permission(self, request, obj=None):
    #     return False

     

admin.site.register(Website,WebsiteAdmin)
admin.site.register(Social,SocialAdmin)