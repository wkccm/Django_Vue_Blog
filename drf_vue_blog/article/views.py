
from article.models import Article
from article.permissions import IsAdminUserOrReadOnly
from rest_framework import viewsets
from article.serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from article.models import Category
from article.serializers import CategorySerializer, CategoryDetailSerializer
from article.models import Tag
from article.serializers import TagSerializer
from article.serializers import ArticleDetailSerializer
from article.models import Avatar
from article.serializers import AvatarSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]