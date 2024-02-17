from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'),    #gokalppo.com/tweetapp
    path('addtweet/',views.addtweet,name='addtweet'),   #gokalppo.com/tweetapp/addtweet
    path('addtweetbyform',views.addtweetbyform,name='addtweetbyform'),  #gokalppo.com/tweetapp/addtweetbyform
    path('addtweetbymodelform',views.addtweetbymodelform,name='addtweetbymodelform'),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path("deletetweet/<int:id>",views.deletetweet,name="deletetweet")
]
