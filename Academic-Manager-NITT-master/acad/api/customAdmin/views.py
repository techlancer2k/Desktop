from rest_framework import viewsets
from .serializers import CustomAdminSerializer
from .models import CustomAdminData

# Create your views here.

class CustomAdminViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    
    queryset = CustomAdminData.objects.all().order_by('adminRollNo')
    serializer_class = CustomAdminSerializer