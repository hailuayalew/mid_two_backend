from student.viewsets import studentViewset
from rest_framework import routers
from Employee.viewsets import EmployeeViewset
from teacher.viewsets import teacherViewset


router1=routers.SimpleRouter()
router1.register('student',studentViewset)

router2=routers.SimpleRouter()
router2.register('employee',EmployeeViewset)


router3=routers.DefaultRouter()
router3.register('teacher',teacherViewset)