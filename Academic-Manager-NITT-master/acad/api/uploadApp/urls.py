from django.urls import path
from .views import MaterialFileView,TimeTableFileView,AssignAssignmentView,SubjectView,SubmitAssignmentView,ClassroomView
from .views import PollView,PollResponseView
urlpatterns = [
    path('classroom/subjects/materials', MaterialFileView.as_view()),
    path('classroom', ClassroomView.as_view()),
    path('classroom/timetable', TimeTableFileView.as_view()),
    path('classroom/subjects/assignassignment',AssignAssignmentView.as_view()),
    path('classroom/subjects/assignassignment/submitassignment',SubmitAssignmentView.as_view()),
    path('classroom/subjects',SubjectView.as_view()),
    path('classroom/poll',PollView.as_view()),
    path('classroom/poll/responses',PollResponseView.as_view()),
]