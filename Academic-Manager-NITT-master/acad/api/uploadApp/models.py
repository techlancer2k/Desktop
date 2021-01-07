from django.db import models

class Classroom(models.Model):
    batch = models.IntegerField()
    department = models.CharField(max_length=2)
    section = models.CharField(max_length=1)

    class Meta:
        unique_together = ('batch', 'department','section',)




class Subject(models.Model):
    classroom_id = models.ForeignKey(
        'Classroom',
        on_delete=models.CASCADE
    )
    semester = models.IntegerField()
    subject_code = models.CharField(max_length=6)

    class Meta:
        unique_together = ('classroom_id', 'semester','subject_code',)
    

    def __str__(self):
        return self.subject_code
    

class MaterialFile(models.Model):
    subject_id = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE
    )
    
    topic = models.CharField(max_length=100)
    
    upload_date = models.DateTimeField(auto_now=False)
    file = models.FileField(blank=False, null=False)
    class Meta:
        unique_together = ('subject_id','topic',)

class Poll(models.Model):
    classroom_id = models.ForeignKey(
        'Classroom',
        on_delete=models.CASCADE
    )
    title = models.TextField(max_length=500)
    option1 = models.TextField(max_length=100)
    option2 = models.TextField(max_length=100)
    option3 = models.TextField(max_length=100)
    option4 = models.TextField(max_length=100)
    option5 = models.TextField(max_length=100)
    deadline = models.DateTimeField()

class PollResponses(models.Model):
    poll_id = models.ForeignKey(
        'Poll',
        on_delete=models.CASCADE
    )
    rollno = models.IntegerField()
    response = models.IntegerField()
    class Meta:
        unique_together = ('rollno', 'poll_id',)
    




    
    #def __str__(self):
   #     return 'topic:{} subject:{} batch:{} subject_code{}'.format(self.topic,self.subject_code,self.batch,self.subject_code)



    
   # def __str__(self):
   #     return 'semester:{} subject:{} batch:{} '.format(self.semester,self.subject_code,self.batch)

class TimeTableFile(models.Model):

    classroom_id = models.ForeignKey(
        'Classroom',
        on_delete=models.CASCADE
    )

    semester = models.IntegerField()
    upload_date = models.DateTimeField(auto_now=False)
    file = models.FileField(blank=False, null=False)
    class Meta:
        unique_together = ('classroom_id', 'semester',)
    
    
   # def __str__(self):
   #     return 'semester:{} batch:{} '.format(self.semester,self.subject_code,self.batch)

class SubmitAssignment(models.Model):
    rollno = models.IntegerField()
    assigned_assignment_id = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )
    submission_timestamp = models.DateTimeField(auto_now=False)
    file = models.FileField(blank=False, null=False)
    class Meta:
        unique_together = ('assigned_assignment_id', 'rollno',)

class AssignAssignment(models.Model):
    
    subject_id = models.ForeignKey(
        'Subject',
        on_delete=models.CASCADE,
    )
    
    topic = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now=False)
    deadline = models.DateTimeField()
    file = models.FileField(blank=False, null=False)
    class Meta:
        unique_together = ('subject_id','topic',)



    