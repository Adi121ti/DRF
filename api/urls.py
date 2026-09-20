from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet,basename = 'employees')

urlpatterns =[
    path('students/',views.studentsView),
    path('student/<int:pk>/' , views.studentDetailView),
    # path('employees/',views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view())
]