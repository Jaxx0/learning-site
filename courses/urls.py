from django.urls import path

from . import views

urlpatterns = [
    path('', views.course_list, name='list'),
    path('<int:course_pk>/<int:step_pk>/t', views.text_detail, name='text'),
    path('<int:course_pk>/<int:step_pk>/q', views.quiz_detail, name='quiz'),
    path('<int:pk>', views.course_detail, name='detail'),
]
