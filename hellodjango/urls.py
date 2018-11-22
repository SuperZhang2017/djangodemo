from django.urls import path
from hellodjango import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('hello/', views.hello,name='hello'), #这里 r'^$' 里面得加上 ^$ 。如果里面还要配置 URL 结尾记的加上反斜杠，如 r'^index/$'
    path('index/', views.index),
    path('login/',views.register),
    path('student/',views.saveStudent,name='student'),
    path('studentList/',views.studentList,name='list'),
    path('editStudent/<int:nid>/', views.editStudent, name='edit'),
    path('delStudent/<int:nid>/', views.delStudent, name='del'),

]





