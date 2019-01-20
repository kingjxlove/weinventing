from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from jd_notebook.goods import views

router = SimpleRouter()
router.register(r'^info', views.NotebookView)

urlpatterns = [

]

urlpatterns += router.urls
