from django.urls import path
from . import views
# detailView는 모델명_detail.html 을 템플릿으로 인지
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    #path('<int:pk>/', views.single_post_pages),
]