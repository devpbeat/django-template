from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import FormView, TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse_lazy

# Modelos para dashboard

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "base/login.html"
    success_url = reverse_lazy('dashboard')
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class LogoutView(RedirectView):
    url = reverse_lazy('login')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
    

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "base/dashboard.html"
    login_url = reverse_lazy('login')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
        
