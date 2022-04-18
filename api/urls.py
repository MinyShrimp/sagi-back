
from django.urls import path
from api.View.Signup import Signup
from api.View.SignupIDOverlap import SignupIDOverlap

urlpatterns = [
    # path('home/', HomeView.as_view()),
    path('signup/', Signup.as_view()),
    path('signup/overlap/', SignupIDOverlap.as_view()),
] 