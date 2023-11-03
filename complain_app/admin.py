from django.contrib import admin

# Register your models here.
from complain_app.models import *

admin.site.register(Organization)
admin.site.register(Department)
admin.site.register(Complain_category)
admin.site.register(Before_complain_resolved_file)
admin.site.register(After_complain_resolved_file)
admin.site.register(Complain)
admin.site.register(Complain_traking)
