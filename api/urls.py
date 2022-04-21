
from django.urls import path
from api.View.Test import Test
from api.View.Signup import Signup
from api.View.Login import Login
from api.View.Logout import Logout
from api.View.SignupIDOverlap import SignupIDOverlap

urlpatterns = [
    # path('home/', HomeView.as_view()),
    path('test/', Test.as_view()),
    path('signup/', Signup.as_view()),
    path('login/',  Login.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/overlap/', SignupIDOverlap.as_view()),
] 