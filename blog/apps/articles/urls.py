from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = []

router = DefaultRouter()
router.register(r'articles',views.ArticleInfoViewSet)
urlpatterns += router.urls