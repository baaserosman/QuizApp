from rest_framework import serializers
from .models import Question, Quiz, Category, Answer



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields ="__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("updated", "question_text", "difficulty", "date_created", "quiz", "answer", )


class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ("quiz_name", "created_date", "category", "question")


class CategorySerializer(serializers.ModelSerializer):
    quiz_set = QuizSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ("name", "quiz_set")