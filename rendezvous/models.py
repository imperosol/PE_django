from django.db import models

from centre.models import Centre
from vaccin.models import Vaccin
from patient.models import Patient


class RDV(models.Model):
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    vaccin = models.ForeignKey(Vaccin, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    injection = models.PositiveIntegerField()

    @staticmethod
    def insert(_centre: int, _vaccin: int, _patient: int, _injection: int):
        new = RDV.objects.create(
            centre=Centre.objects.get(pk=_centre),
            vaccin=Vaccin.objects.get(pk=_vaccin),
            patient=Patient.objects.get(pk=_patient),
            injection=_injection
        )
        new.save()
        return new

    @staticmethod
    def get_nbr_injections(patient_id):
        result = RDV.objects.filter(patient=patient_id).aggregate(models.Max('injection'))['injection__max']
        return result if result is not None else 0

    @staticmethod
    def get_max_injections(patient_id):
        vaccin_id = RDV.get_vaccin(patient_id)
        vaccin_patient = Vaccin.objects.get(pk=vaccin_id)
        return vaccin_patient.doses

    @staticmethod
    def get_vaccin(patient_id):
        return RDV.objects.filter(patient=patient_id).values_list('vaccin', flat=True)[0]

    @staticmethod
    def get_vaccin_in_centre(centre_id):
        return Vaccin.objects.filter(stock__doses__gt=0, stock__centre_id=centre_id)
