from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from goods import views

router = SimpleRouter()
router.register(r'^info', views.NotebookView)

urlpatterns = [
    url(r'^goods_info/', views.index, name='index')
]

urlpatterns += router.urls
