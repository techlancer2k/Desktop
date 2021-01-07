from rest_framework import serializers
from .models import MaterialFile,TimeTableFile,AssignAssignment,Subject,SubmitAssignment,Classroom
from .models import Poll,PollResponses
class ClassroomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class MaterialFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaterialFile
        fields = '__all__'
        
    




class TimeTableFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = TimeTableFile
        fields = '__all__'



class AssignAssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AssignAssignment
        fields = '__all__'

class SubmitAssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubmitAssignment
        fields = '__all__'

class PollSerializers(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class PollResponseSerializers(serializers.ModelSerializer):
    class Meta:
        model = PollResponses
        fields = '__all__'