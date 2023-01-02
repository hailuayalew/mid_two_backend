from rest_framework import viewsets
from . import models
from . import serializers

class teacherViewset(viewsets.ModelViewSet):
    queryset=models.teacher.objects.all()
    serializer_class=serializers.teacherSerializer