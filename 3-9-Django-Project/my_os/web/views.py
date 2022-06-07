import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET


@require_GET
def get_home(request):
   return render(request, 'home.html', {'date_and_time': datetime.datetime.now()})


@require_GET
def get_index(request, user_name):
   return render(request, 'index.html', {'guest': user_name})
