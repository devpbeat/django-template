from django.urls import include, path
from .views import LoginView, LogoutView, DashboardView

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("", DashboardView.as_view(), name='dashboard'),
    path("recetas/", include('recetas.urls'))
]
