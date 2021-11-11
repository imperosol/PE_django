from django.db import models

from patient.models import Patient
from rendezvous.models import RDV
from vaccin.models import Vaccin


class Innovations:
    @staticmethod
    def get_avancement_vaccination():
        patients = Patient.objects.all()
        vaccines, incomplets, non_vaccines = [], [], []
        for p in patients:
            vax = RDV.objects.filter(patient_id=p.id).values("vaccin_id").annotate(injection=models.Max("injection"))
            if len(vax) == 0:
                non_vaccines.append(p)
            else:
                doses = Vaccin.objects.get(pk=vax[0]['vaccin_id']).doses
                if doses == vax[0]['injection']:
                    vaccines.append(p)
                else:
                    incomplets.append(p)
        return {
            "vaccines": vaccines,
            "incomplets": incomplets,
            "non_vaccines": non_vaccines
        }
