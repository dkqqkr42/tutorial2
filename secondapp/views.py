from django.shortcuts import render
from django.http import HttpResponse
from .models import Hospital

def show(request):
    hospital = Hospital.objects.all()
    return render(request, 'show.html',{'list':hospital})
    # html = ''
    # for c in curriculum:
    #     html += '%s번 %s<br>' % (c.id, c.name)
    # return HttpResponse(html)