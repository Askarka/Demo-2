from django.urls import path

# from .views import index, by_rubric, BbCreateView
from blog.views import flow

urlpatterns = [
    # path('add/', BbCreateView.as_view(), name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    # path('', index, name='index'),
    path('flow/', flow, name='flow')
]
