from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import LivrosUltimoAnoView
from .views import LivrosEstatisticasView

router = DefaultRouter()
router .register(r'autores', AutorViewSet)
router .register(r'livros', LivroViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('biblioteca.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('livros/ultimo-ano/', LivrosUltimoAnoView.as_view(), name='livros_ultimo_ano'),
    path('livros/estatisticas/', LivrosEstatisticasView.as_view(), name='livros_estatisticas'),
]

