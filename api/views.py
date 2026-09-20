from students.models import Student
from .serializers import StudentSerializer , EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from blogs.models import Blog , Comment
from blogs.serializers import CommentSerializer, BlogSerializer
from rest_framework import mixins, generics,viewsets
from .paginations import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend
from employees.filters import EmployeeFilter

# Create your views here.

#function based view
@api_view(['GET','POST'])
def studentsView(request):
  if request.method == 'GET':
      #get all the data from student table
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)
      return Response(serializer.data, status = status.HTTP_200_OK)
  elif request.method =='POST':
      serializer = StudentSerializer(data= request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status = status.HTTP_201_CREATED)
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET','PUT', 'PATCH','DELETE']) 
def studentDetailView(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist: 
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status =status.HTTP_200_OK)
      
    elif request.method =='PUT':
        serializer = StudentSerializer(student,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)  
        else :
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST )
        
        
    elif request.method =='PATCH':
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student,data = request.data, partial =True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
        
    elif request.method =='DELETE':
        student.delete()
        return Response("delay",status=status.HTTP_204_NO_CONTENT)
        
#class-based view


# class Employees(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many= True)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_200_OK)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
            
# class EmployeeDetailView(APIView):
#     def get_employee(self,pk):
#         try:
#             employee = Employee.objects.get(pk =pk) 
#             return employee
#         except employee.DoesNotExist:
#             raise Http404 
        
#     def get(self,request,pk):
#         employee = self.get_employee(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status = status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         employee = self.get_employee(pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
#     def patch(self,request,pk):
#         employee = self.get_employee(pk)
#         serializer = EmployeeSerializer(employee,data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         employee = self.get_employee(pk)
#         employee.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
        

#                       using mixins



# class Employees(mixins.ListModelMixin , mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
        
        
# class EmployeeDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=  Employee.objects.all()
#     serializer_class= EmployeeSerializer
    
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
    
#     def put(self,request,pk):
#         return self.update(request,pk)
    
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
    
    
    #                       generics
      
# class Employees(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeDetailView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


#viewset - does not handle errors by itself 


# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset123 = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset123,many = True)
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = EmployeeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_OK)
#         return Response(status = status.HTTP_400_BAD_REQUEST)
     
     
#     def retrieve(self,request,pk= None):
#         queryset = Employee.objects.get(pk=pk)
#         serializer = EmployeeSerializer(queryset)
#         return Response(serializer.data)
    
#     def destroy(self, request,pk = None):
#         employee = Employee.objects.get(pk=pk)
#         employee.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

#     def update(self,request,pk):
#         employee = Employee.objects.get(pk= pk)
#         serializer = EmployeeSerializer(employee,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         return Response(status = status.HTTP_400_BAD_REQUEST)
        
#     def partial_update(self,request,pk = None):
#             employee = Employee.objects.get(pk= pk)
#             serializer = EmployeeSerializer(employee,data = request.data, partial=True)
#             if serializer.is_valid(raise_exception = True):
#                 serializer.save()
#                 return Response(serializer.data, status = status.HTTP_200_OK)
#             return Response(status = status.HTTP_400_BAD_REQUEST)
        
        
        
        #ModelViewSet
        
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    #for exact text
   # filterset_fields =['designation']
    filterset_class = EmployeeFilter
    
    
    
    
class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
    
    
class BlogDetailView(generics.DestroyAPIView, generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    

    
    
class CommentDetailView(generics.DestroyAPIView, generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer