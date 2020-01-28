from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead


# Create your views here.
def home(request):
    #return HttpResponse('Leads')
    fields = {
        'titulo': 'Leads',
        'leads': Lead.objects.all()
    }

    return render(request, 'leads/leads.html', fields)


def home_param(request, lead_id):
    return HttpResponse('Leads %s' % lead_id)
