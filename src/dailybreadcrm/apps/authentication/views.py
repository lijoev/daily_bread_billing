from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import TemplateView
# from .forms import SignUpForm, LoginForm, ProfileForm, \
#     UpdateUserForm, PasswordReset, IagreeForm, ForgotPassword
# from .models import Profile
from django.contrib import messages
from django.shortcuts import render_to_response

import logging
from django.conf import settings

LOG = logging.getLogger('dailyBread.%s' % __name__)

# Create your views here.


class LoginView(TemplateView):
    """
    Login view
    """
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        LOG.error(settings.STATIC_ROOT)
        return render(request, self.template_name)


    def post(self, request):
        pass


class HomeView(TemplateView):
    """
    Home view handling class after successfull login
    """
    def get(self, request, *args, **kwargs):
        pass