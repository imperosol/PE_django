from django.shortcuts import render
from .models import Innovations


def innovation_1(request):
    context = {'tables': Innovations.get_avancement_vaccination()}
    return render(request, 'innovations/innovation_1.html', context)
