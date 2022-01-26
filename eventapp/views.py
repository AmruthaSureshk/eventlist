from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from datetime import datetime, timedelta, time

from .models import Event




# Create your views here.

def index(request):
    event = Event.objects.all().order_by('startdate').filter(published=True,)
    p = Paginator(event, 10)
    page_number= request.GET.get('page')
    page_obj = p.get_page(page_number)



    return render(request, "index.html", {'context': event, 'page_obj':page_obj,})
