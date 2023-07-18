
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import SignUpForm

# Create your views here.
class SignInView(LoginView):
    template_name = 'signin.html'
    next_page = reverse_lazy('products:home')
    redirect_authenticated_user = True
class signOutView(LogoutView):
    next_page = reverse_lazy('products:home')

class signUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('products:home') 