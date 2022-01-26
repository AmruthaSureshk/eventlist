from django.shortcuts import render
from eventapp.models import Event
from django.db.models import Q


# Create your views here.
#search the event by title or keyword in decription
def SearchResult(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Event.objects.all().filter(Q(title__contains=query)| Q(description__contains=query))
        return render(request, 'search.html', {'query': query, 'products': products})
