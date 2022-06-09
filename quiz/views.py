from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer
from .permissions import IsAdminOrReadOnly


class QuizList(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]    
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class QuestionList(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class CategoryList(generics.ListAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class QuizDetail(generics.RetrieveAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field = "id"

class QuestionDetail(generics.RetrieveAPIView):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = "id"

