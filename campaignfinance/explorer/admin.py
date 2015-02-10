from django.contrib import admin
from explorer.models import Receipts,Race,AppCandidate,AppCommittee

class RaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class AppCandidateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nameFirst','nameLast')}

class AppCommitteeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Receipts)
admin.site.register(Race,RaceAdmin)
admin.site.register(AppCommittee, AppCommitteeAdmin)
admin.site.register(AppCandidate, AppCandidateAdmin)