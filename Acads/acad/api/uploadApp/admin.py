from django.contrib import admin
from .models import MaterialFile,TimeTableFile,AssignAssignment,Subject,SubmitAssignment,Classroom
from .models import Poll,PollResponses
# Register your models here.
admin.site.register(MaterialFile)
admin.site.register(SubmitAssignment)
admin.site.register(TimeTableFile)
admin.site.register(AssignAssignment)
admin.site.register(Subject)
admin.site.register(Classroom)
admin.site.register(Poll)
admin.site.register(PollResponses)

