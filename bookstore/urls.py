from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls'))
]
