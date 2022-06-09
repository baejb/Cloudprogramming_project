from django.urls import path
from . import views
# detailView는 모델명_detail.html 을 템플릿으로 인지
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/' ,views.categories_page),
    path('tag/<str:slug>/', views.show_tag_posts),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('<int:pk>/addcomment/', views.add_comment),
    #path('<int:pk>/', views.single_post_pages),
]