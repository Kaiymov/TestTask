from django.urls import path

from article.views import (ArticleListView, ArticleCreateView,
                           ArticleUpdateDeleteView, PrivateDetailView)

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<int:id>/', PrivateDetailView.as_view()),
    path('create/', ArticleCreateView.as_view()),
    path('update-delete/<int:id>/', ArticleUpdateDeleteView.as_view()),

]
