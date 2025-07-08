from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

routers = DefaultRouter()
routers.register('employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetailView),

    # path('employees/', views.Employees.as_view()),
    # path('employees/<str:emp_id>/', views.EmployeeDetail.as_view())
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view())

    path('', include(routers.urls)),
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
]