"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Maps any urls starting with catalog
    # to be handled by the catalog app
    url('catalog/', include('catalog.urls')),

    #Maps the root URL and redirect to /catalog/
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),

    #Add Django site authentication urls (for login, logout, password management)
    url(r'^accounts/', include('django.contrib.auth.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
