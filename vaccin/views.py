from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VaccinForm
from .models import Vaccin


def view_all(request):
    vaccins = get_list_or_404(Vaccin)
    context = {'vaccins': vaccins}
    return render(request, 'vaccin/view_all.html', context)


@login_required
def add(request):
    context = {'form': VaccinForm()}
    return render(request, 'vaccin/add.html', context)


@login_required
def added(request):
    form = VaccinForm(request.POST)
    new_vaccin = form.save()
    context = {'new': new_vaccin}
    return render(request, 'vaccin/added.html', context)


@login_required
def update(request):
    vaccins = get_list_or_404(Vaccin)
    context = {'vaccins': vaccins}
    return render(request, 'vaccin/update.html', context)


@login_required
def updated(request):
    vaccin_id = request.POST.get('id_vaccin')
    new_doses = request.POST.get('new_doses')
    updated_vaccin = get_object_or_404(Vaccin, pk=vaccin_id)
    updated_vaccin.update(doses=new_doses)
    context = {'vaccin': updated_vaccin}
    return render(request, 'vaccin/updated.html', context)
