from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

post_router = DefaultRouter()
post_router.register('post', views.PostViewSet)

rate_router = DefaultRouter()
rate_router.register('rate', views.RatePostApiView)

urlpatterns = [
    path('',include(post_router.urls)),

    path('post/<int:post_id>/comment/', views.CommentCreateApiView.as_view()),
    path('post/<int:post_id>/comment/<int:pk>/', views.CommentRetrieveUpdateDestroyApiView.as_view()),

    path('post/<int:post_id>/', include(rate_router.urls))

]
