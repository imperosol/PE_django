from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patient
from .forms import PatientForm


@permission_required('patient.add_patient')
@login_required
def add(request):
    context = {'form': PatientForm()}
    return render(request, 'patient/add.html', context)


@permission_required('patient.add_patient')
@login_required
def added(request):
    form = PatientForm(request.POST)
    new_patient = form.save()
    context = {'new': new_patient}
    return render(request, 'patient/added.html', context)


def view_all(request):
    patients = Patient.objects.all()
    context = {
        'patients': patients
    }
    return render(request, 'patient/view_all.html', context)
