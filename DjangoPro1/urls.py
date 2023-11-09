from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('petapp/', include('petapp.urls')), # 将petapp/urls.py中的url添加到总的url中
    path('', RedirectView.as_view(url='petapp/home/')), # 自动跳转到petapp/home/页面
]
