from django.conf.urls.static import static
from django.urls import path

# from .views import index, by_rubric, BbCreateView
from blog.views import flow
from true_life import settings

urlpatterns = [
    # path('add/', BbCreateView.as_view(), name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    # path('', index, name='index'),
    path('flow/', flow, name='flow')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


