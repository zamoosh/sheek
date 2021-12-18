"""sheek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt import views as jwt_views
from .views import *

schema_view = get_schema_view(
    openapi.Info(
        title="sheek API",
        default_version='v1',
        description="This api uses for Application.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@vidone.org"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/client/', include('client.apiurls')),
    path('', index, name='index'),
    path('accounts/', include('client.urls')),
    path('state/', include('state.urls')),
    path('jobs/', include('projects.urls')),
]
