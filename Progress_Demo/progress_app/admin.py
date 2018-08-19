from django.contrib import admin

from .models import location,progress,students,subject,teachers

admin.site.register(location)
admin.site.register(progress)
admin.site.register(students)
admin.site.register(subject)
admin.site.register(teachers)
