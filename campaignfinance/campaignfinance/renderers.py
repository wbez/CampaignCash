from django_medusa.renderers import StaticSiteRenderer
from explorer.models import Race, AppCommittee, AppCandidate, Receipts, Committees

class HomeRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = ["/campaigncash/", ]

        races = Race.objects.all()
        for race in races:
            paths.append(race.get_absolute_url())

        candidates = AppCandidate.objects.all()
        for candidate in candidates:
            paths.append(candidate.get_absolute_url())
            paths.append(candidate.get_absolute_url()+'json/')

        return paths

renderers = [HomeRenderer, ]