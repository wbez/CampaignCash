from django.core.management.base import BaseCommand, CommandError
from explorer.models import Race, AppCommittee, AppCandidate, Receipts, Committees
import csv

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

        with open('candidates.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = reader.next()
            for row in reader:
                ward = row[0]
                candidate = row[1]
                committeeid = row[2]
                committeename = row[3]

                candidate_name = candidate.split(' ',2)
                candidate_results = AppCandidate.objects.filter(nameFirst = candidate_name[0].capitalize(), nameLast=candidate_name[-1].capitalize()).count()

                if candidate_results == 0:
                    c = AppCandidate()
                    c.nameFirst = candidate_name[0].capitalize()
                    c.nameLast = candidate_name[-1].capitalize()
                    if len(candidate_name) == 3:
                        c.nameMiddle = candidate_name[1].capitalize()
                    c.save()
                    race_obj = Race.objects.get(ward=ward)
                    c.races.add(race_obj)
                    c.save()

                if committeeid == '':
                    print 'no committeeid'
                else:
                    committee_results = AppCommittee.objects.filter(committeeid = int(committeeid)).count()
                    if committee_results == 0:
                        committee = AppCommittee()
                        committee.committeeid = committeeid
                        print 'searching for %s' % committeeid
                        if Committees.objects.filter(id=committeeid).count() == 0:
                            committee.name = committeename
                        else:
                            committee.name = Committees.objects.get(id=committeeid).cmtename
                        print candidate_name[0].capitalize(), candidate_name[-1].capitalize()
                        committee.candidate = AppCandidate.objects.get(nameFirst = candidate_name[0].capitalize(), nameLast=candidate_name[-1].capitalize())
                        committee.save()
                

