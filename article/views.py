from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from article.models import Article
from article.serializers import ArticleSerializer, RegisterSerializer
from .permissions import NotAuthenticated, IsSubscriber, IsAuthor, IsAuthorOwner
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [NotAuthenticated,]


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.role == 'FW':
                return Article.objects.all()
        return Article.objects.filter(is_public=True)


class PrivateDetailView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = ArticleSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.role == 'FW':
                return Article.objects.all()
        return Article.objects.filter(is_public=True)

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAuthorOwner, IsAuthor]
