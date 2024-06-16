from django.contrib import admin
from authentication.models import UserArea
import public.models as models

class IncidenceAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, extra_context=None):       
        self.exclude = ('designated_area', 'solved_date', 'target_date')
        return super(IncidenceAdmin, self).change_view(request, object_id, extra_context)

# All the tables created
admin.site.register(models.Incidence, IncidenceAdmin)
admin.site.register(models.AccessRequest)
admin.site.register(models.Subject)
admin.site.register(UserArea)
admin.site.register(models.PriorityRanges)