from django.urls import path
from . import views



urlpatterns = [
    path('trips/', views.TripListCreate.as_view()),
    path('trips/<int:pk>', views.TripRetrieveUpdateDestroy.as_view()),
    path('trips/<int:pk>/complete', views.TripToggleComplete.as_view()),
    
    # Let’s first implement a new user sign up.
    path('signup/', views.signup),
    
    # Let's provide login urls
    path('login/', views.login),
]