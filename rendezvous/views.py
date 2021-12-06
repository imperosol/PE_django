from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import RDV
from patient.models import Patient
from centre.models import Centre


@login_required
@permission_required('rendezvous.add_rdv')
def select_patient(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'rendezvous/select_patient.html', context)


@login_required
@permission_required('rendezvous.add_rdv')
def vaccination_patient(request):
    patient_id = request.GET['patient_id']
    injections = RDV.get_nbr_injections(patient_id)
    if injections == 0:
        centres = Centre.objects.filter(stock__doses__gt=0).distinct()
    elif injections < RDV.get_max_injections(patient_id):
        vaccin_patient = RDV.get_vaccin(patient_id)
        centres = Centre.objects.filter(stock__doses__gt=0, stock__vaccin_id=vaccin_patient).distinct()
    else:
        centres = None
    context = {'centres': centres, 'injections': injections, 'patient_id': patient_id}
    return render(request, 'rendezvous/select_centre.html', context)


@login_required
def select_vaccin(request):
    centre_id = request.GET.get('centre_id')
    patient_id = request.GET.get('patient_id')
    list_vaccin = RDV.get_vaccin_in_centre(centre_id)
    context = {'vaccins': list_vaccin, 'centre_id': centre_id, 'patient_id': patient_id}
    return render(request, 'rendezvous/select_vaccin.html', context)


@login_required
def insert(request):
    vaccin_id = request.POST.get('vaccin_id')
    centre_id = request.POST.get('centre_id')
    patient_id = request.POST.get('patient_id')
    if vaccin_id == "":
        vaccin_id = RDV.get_vaccin(patient_id)
    injections = RDV.get_nbr_injections(patient_id) + 1
    new_rdv = RDV.insert(centre_id, vaccin_id, patient_id, injections)
    context = {'new': new_rdv}
    return render(request, 'rendezvous/inserted.html', context)
