from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, QuestionSerializer, QuizSerializer


class QuizList(generics.ListAPIView):    
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class QuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class QuizDetail(generics.RetrieveAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    lookup_field = "id"

class QuestionDetail(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    lookup_field = "id"

