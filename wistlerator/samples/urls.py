from django.urls import path

from . import views

urlpatterns = [
    # sample
    path("", views.index, name="index"),
    path('sample/', views.index_sample, name="index_sample"),
    path('sample/<int:sample_id>/', views.detail_sample, name='detail_sample'),
    path('sample/create/', views.create_sample, name='create_sample'),
    # category
    path('category/', views.index_category, name="index_category"),
    path('category/<int:category_id>/', views.detail_category, name='detail_category'),
    path('category/create/', views.create_category, name='create_category'),
]
