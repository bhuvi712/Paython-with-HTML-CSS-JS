from django.urls import path
from .  import views

urlpatterns = [
    path("", views.index, name= "index"),
    # path("<str:name>", views.greet, name= "greet"),
    # path("Bhunesh", views.Bhunesh, name= "Bhunesh"),
    # path("David", views.Bhunesh, name= "David")

]