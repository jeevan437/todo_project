from django.conf.urls import url,include
from.views import todo_model
from .views import index_view
from rest_framework import routers
from .viewsets import Todo_ViewSet

router = routers.DefaultRouter()

router.register('api', Todo_ViewSet)
urlpatterns = [

    #url(r'^app/',index_view)   # function based views
    url(r'^', include(router.urls))

]