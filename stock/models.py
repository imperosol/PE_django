from django.db import models
from vaccin.models import Vaccin
from centre.models import Centre


class Stock(models.Model):
    centre_id = models.ForeignKey(Centre, on_delete=models.CASCADE, verbose_name='Centre')
    vaccin_id = models.ForeignKey(Vaccin, on_delete=models.CASCADE, verbose_name='Vaccin')
    doses = models.IntegerField()

    def __str__(self):
        return f"{self.centre_id.label} ({self.vaccin_id.label})"

    @staticmethod
    def get_list_vaccin_label():
        values_name = Stock.objects.all().values_list('vaccin_id__label').distinct()
        return [v[0] for v in values_name]

    @staticmethod
    def get_list_vaccin_id():
        values_id = Stock.objects.all().values_list('vaccin_id__id').distinct()
        return [v[0] for v in values_id]

    @staticmethod
    def get_detail() -> list[list[str, int]]:
        NAME, ID = 0, 1  # for readability
        v_id = Stock.get_list_vaccin_id()  # get only id of vaccines
        centres = Stock.objects.all().values_list('centre_id__label', 'centre_id__id').distinct()
        result = []
        for centre in centres:
            row = [centre[NAME]]
            for vaccin in v_id:
                detail = Stock.objects.values_list('doses', flat=True).filter(centre_id=centre[ID], vaccin_id=vaccin)
                row.append(sum([d for d in detail]))
            result.append(row)
        return result

    @staticmethod
    def get_global() -> list[list[str, int]]:
        NAME, ID = 0, 1  # for readability
        centres = Stock.objects.all().values_list('centre_id__label', 'centre_id__id').distinct()
        result: list[list[str, int]] = [[
            c[NAME],
            sum([dose for dose in Stock.objects.values_list('doses', flat=True).filter(centre_id=c[ID])])
        ] for c in centres
        ]
        # result is a list of lists. Each list has two elements : the name of the centre and the total number of
        # doses in
        return result
