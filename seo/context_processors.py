from .models import *
import datetime


def base_social_render(request):
    date = datetime.date.today()
    year = date.strftime("%Y")
    social = Social.objects.filter(active=1).order_by('?')
    return{ 'seo_social': social, 'time_year': year }


def base_website_render(request):
    website = Website.objects.first()
    return{ 'seo_website': website }