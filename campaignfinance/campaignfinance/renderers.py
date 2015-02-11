from django_medusa.renderers import StaticSiteRenderer
from explorer.models import Race, AppCommittee, AppCandidate, Receipts, Committees

class HomeRenderer(StaticSiteRenderer):
    def get_paths(self):
        paths = ["/", ]

        items = Race.objects.all()
        for item in items:
            paths.append(item.get_absolute_url())

        return paths

renderers = [HomeRenderer, ]