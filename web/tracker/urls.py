from django.urls import path
from . import views

urlpatterns = [
    # /tracker/
    path('', views.index, name='index'),

    # /tracker/5
    path('<int:tx_id>/', views.detail, name='detail'),

    # /tracker/portfolio
    path('portfolio/', views.portfolio, name='portfolio')
]
