from django.conf.urls import url
from.views import todo_model
from .views import index

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^app/',index)   # function based views
    #url(r'book_details',BookView.as_view())
]