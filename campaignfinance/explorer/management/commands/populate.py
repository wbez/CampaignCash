from django.core.management.base import BaseCommand, CommandError
from explorer.models import Race

class Command(BaseCommand):

    def handle(self, *args, **options):
        wards = range(1,51)

        for ward in wards:
            num_results = Race.objects.filter(ward = ward).count()

            if num_results == 0:
                r = Race()
                r.name = 'Ward %s' % ward
                r.ward = ward
                r.save()

                self.stdout.write('Successfully saved race "%s"' % r.name)