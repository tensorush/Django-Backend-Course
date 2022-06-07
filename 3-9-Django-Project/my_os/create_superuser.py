import os

from django.contrib.auth.models import User


try:
    User.objects.create_superuser(os.environ['DJANGO_SUPERUSER_USERNAME'],
                                  os.environ['DJANGO_SUPERUSER_EMAIL'],
                                  os.environ['DJANGO_SUPERUSER_PASSWORD'])
except:
    pass
