from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm


@login_required
def add(request):
    context = {'form': PatientForm()}
    return render(request, 'patient/add.html', context)


@login_required
def added(request):
    form = PatientForm(request.POST)
    new_patient = form.save()
    context = {'new': new_patient}
    return render(request, 'patient/added.html', context)


def view_all(request):
    patients = get_list_or_404(Patient)
    context = {
        'patients': patients
    }
    return render(request, 'patient/view_all.html', context)
