"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    #views.py에서 만든 home함수를 내보내줘야하므로 url.py에 path를 지정해줌.
    
    path('blog/<int:blog_id>/', blog.views.detail, name='detail'),
    #<type:name> : path-converter//지정한 converter type의 name변수를 view 함수로 넘김.
    #게시글(객체)마다 detail이 필요하기 때문에 게시글마다 id 값을 받아 url을 생성해 보여줌.

    path('blog/new/', blog.views.new, name='new'),
    path('blog/create', blog.views.create, name='create'),
    #path는 단순히 html page를 불러올 때만 사용하는 게 아닌 함수를 불러올 때도 사용가능.(path수!= page수)
    #.html에서 create함수를 호출하면 views.py에서 만든 create함수를 내보내주려 path를 지정해줌.

    path('blog.edit/<int:blog_id>', blog.views.edit, name='edit'),
    #path-converter를 이용.(int type의 id 값을 view 함수로 넘김.)

    path('blog.delete/<int:blog_id>', blog.views.delete, name='delete'),


    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)