from django.db import models
from django.core.validators import FileExtensionValidator


STATUS = (
    (0, 'INACTIVE'),
    (1, 'ACTIVE')
)

# Create your models here.
class Social(models.Model):
    site = models.CharField(max_length=64)
    link = models.URLField(max_length=256)
    active = models.SmallIntegerField(choices=STATUS)
    icon = models.FileField(upload_to='images/', validators=[FileExtensionValidator(['png', 'svg'])])

    class Meta:
        verbose_name_plural = "Social"

    def __str__(self):
        return self.site


class Website(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(max_length=256)
    tagline = models.TextField()
    email = models.EmailField(max_length=256)
    mobile = models.CharField(max_length=32)
    address = models.TextField()
    logo = models.FileField(upload_to='images/', validators=[FileExtensionValidator(['png', 'svg', 'jpg', 'jpeg', 'webp'])])

    class Meta:
        verbose_name_plural = "Website"

    def __str__(self):
        return self.name
