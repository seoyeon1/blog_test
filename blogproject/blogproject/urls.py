from django.contrib import admin
from django.urls import path, include
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    
    path('blog/', include('blog.urls')),

    path('portfolio/', include('portfolio.urls')),
    # path('portfolio/', portfolio.views.portfolio, name='portfolio'), 
    #기존에는 이런 식으로 프로젝트 관련 url들을 관리했다면 이제는 include를 사용하여 각 앱별로 url을 관리할 수 있게 함.
    #프로젝트의 urls.py로 가서 include로 연결

    # account app도 추가 예정

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 위에 것과 같은 의미