from django.conf.urls import url,include
from.views import todo_model
from .views import index_view
from rest_framework import routers
from .viewsets import Todo_ViewSet,DetailsView

router = routers.DefaultRouter()

router.register('api', Todo_ViewSet)
urlpatterns = [

    #url(r'^app/',index_view)   # function based views
    url(r'^', include(router.urls)),
    #url(r'^todo_list/(?P<pk>[0-9]+)/$',DetailsView.as_view()),

]
