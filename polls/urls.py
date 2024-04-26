from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug>/', views.DetailView.as_view(), name='detail'),
    path('<choice_slug>/vote/', views.vote, name='vote'),
    path('<slug>/results/', views.ResultsView.as_view(), name='results'),
]