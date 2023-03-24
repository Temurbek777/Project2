from django.urls import path
from Quiz.views import *

urlpatterns = [
    path('', Func1, name='home'),
    path('login', Login, name='login')

]


