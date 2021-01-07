
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import MaterialFile,TimeTableFile,Subject,AssignAssignment,SubmitAssignment,Classroom
from .models import Poll,PollResponses
from .serializers import MaterialFileSerializers,TimeTableFileSerializers,AssignAssignmentSerializers,SubjectSerializers,SubmitAssignmentSerializers,ClassroomSerializers
from .serializers import PollSerializers,PollResponseSerializers
from django.http import JsonResponse

def details(rollno):
  department_code = rollno[0:3]
  batch_code = rollno[4:6]
  section_code = rollno[8]

  department_dict = {
  '101':'AR',
  '102':'CL',
  '103':'CE',
  '104':'',
  '105':'',
  '106':'CS',
  '107':'EE',
  '108':'EC',
  '109':'',
  '110':'IC',
  '111':'ME',
  '112':'MT',
  '114':'PR'
  }
  if(int(section_code)%2 == 0 and department_code not in ['101','102','112']):
    section = 'B'
  else:
    section = 'A'

  department = department_dict[department_code]
  updated_request = {}
  updated_request.update({'batch' : '20'+ batch_code})
  updated_request.update ({'department' : department})
  updated_request.update ({'section' : section})
  return(updated_request)



class ClassroomView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def get(self, request, format=None):
    """
    Return class given roll no .
    """
    snippets = Classroom.objects.all()
    
    rollno = self.request.query_params.get('rollno', None)
      
    
    
    requested_batch = details(rollno)['batch']
    requested_department = details(rollno)['department']
    requested_section  = details(rollno)['section']
    
    if rollno is not None:
      snippets = snippets.filter(batch=requested_batch,department=requested_department,section=requested_section)
    serializer = ClassroomSerializers(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


  def post(self, request, *args, **kwargs):


    rollno = request.data.get('rollno')
    detail = details(rollno)
    request.data._mutable = True
    request.data.pop('rollno')
    request.data.update(detail)
    request.data._mutable = False

    classroom_serializer = ClassroomSerializers(data=request.data)
    if classroom_serializer.is_valid():
      classroom_serializer.save()
      return Response(classroom_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(classroom_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubjectView(APIView):#Generates a Subject Identifier which will be unique for each subject of each class
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
      """
      Return a list of all subjects given roll no and semester as query paramaters.
      """
      snippets = Subject.objects.all()
    
      
      required_classroom = self.request.query_params.get('classroom_id', None)
      required_semester = self.request.query_params.get('semester',None)
    
    

    
      if required_classroom is not None:
        snippets = snippets.filter(classroom_id=required_classroom,semester=required_semester)
      serializer = SubjectSerializers(snippets, many=True)
      return JsonResponse(serializer.data, safe=False)


    def post(self, request, *args, **kwargs):



      subject_serializer = SubjectSerializers(data=request.data)
      if subject_serializer.is_valid():
          subject_serializer.save()
          return Response(subject_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(subject_serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class MaterialFileView(APIView):

  parser_classes = (MultiPartParser, FormParser)
  
  #authentication_classes = [authentication.TokenAuthentication]
  #permission_classes = [permissions.IsAdminUser]
  
  def get(self, request, format=None):
    """
    Return list of materials based on subject ID.
    """
    snippets = MaterialFile.objects.all()
    required_subject = self.request.query_params.get('subject_id', None)
    
    
    if required_subject is not None:
      snippets = snippets.filter(subject_id=required_subject)
    
    serializer = MaterialFileSerializers(snippets, many=True)
    return(JsonResponse(serializer.data,safe=False))


  def post(self, request, *args, **kwargs):
  
    file_serializer = MaterialFileSerializers(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TimeTableFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
      
      snippets = TimeTableFile.objects.all()
      
      required_classroom = self.request.query_params.get('classroom_id', None)
      required_semester = self.request.query_params.get('semester', None)

      if required_classroom is not None:
        snippets = snippets.filter(classroom_id=required_classroom,semester=required_semester)
      
      serializer = TimeTableFileSerializers(snippets, many=True)
      return JsonResponse(serializer.data, safe=False)


    def post(self, request, *args, **kwargs):
      

      file_serializer = TimeTableFileSerializers(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class AssignAssignmentView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
      """
      Return a list of all assignments given roll no and semester as query parameters.
      """
     
      snippets = AssignAssignment.objects.all()

      serializer = AssignAssignmentSerializers(snippets, many=True)
      required_subject = self.request.query_params.get('subject_id', None)
    
      if required_subject is not None:
        snippets = snippets.filter(subject_id=required_subject)
      serializer = AssignAssignmentSerializers(snippets, many=True)
      return JsonResponse(serializer.data, safe=False)



    def post(self, request, *args, **kwargs):


      
      file_serializer = AssignAssignmentSerializers(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubmitAssignmentView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
      """
      Return a list of all assignments given assignment id.
      """
     
      snippets = SubmitAssignment.objects.all()

      serializer = SubmitAssignmentSerializers(snippets, many=True)
      required_assignment = self.request.query_params.get('assigned_assignment_id', None)
    
      if required_assignment is not None:
        snippets = snippets.filter(assigned_assignment_id=required_assignment)
      serializer = SubmitAssignmentSerializers(snippets, many=True)
      return JsonResponse(serializer.data, safe=False)



    def post(self, request, *args, **kwargs):


      
      file_serializer = SubmitAssignmentSerializers(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PollView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
      
      snippets = Poll.objects.all()
      
      required_classroom = self.request.query_params.get('classroom_id', None)
      

      if required_classroom is not None:
        snippets = snippets.filter(classroom_id=required_classroom)
      
      serializer = PollSerializers(snippets, many=True)
      return JsonResponse(serializer.data, safe=False)


    def post(self, request, *args, **kwargs):
      

      file_serializer = PollSerializers(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollResponseView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, format=None):
      
      snippets = PollResponses.objects.all()
      
      required_poll = self.request.query_params.get('poll_id', None)
      

      if required_poll is not None:
        snippets = snippets.filter(poll_id=required_poll)
      
      serializer = PollResponseSerializers(snippets, many=True)
      votes = serializer.data
      vote_counts = {
        'Poll ID' : required_poll,
        '1' : 0,
        '2' : 0,
        '3' : 0,
        '4' : 0,
        '5' : 0,

      }
      for i in votes:
        vote_counts[str((i.get('response') ))] += 1
      

      return JsonResponse(vote_counts)


    def post(self, request, *args, **kwargs):
      

      file_serializer = PollResponseSerializers(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)