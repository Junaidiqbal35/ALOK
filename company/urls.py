from django.urls import path
from company.views import *

urlpatterns = [

    path('data/', get_campaign, name='get-comp'),

]
