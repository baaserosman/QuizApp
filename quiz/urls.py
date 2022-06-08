from django.urls import path
from .views import CategoryList, QuestionDetail, QuestionList, QuizDetail, QuizList

urlpatterns = [    
    path("quiz/", QuizList.as_view()),
    path("question/", QuestionList.as_view()),
    path("category/", CategoryList.as_view()),
    path("quiz-detail/<int:id>", QuizDetail.as_view()),
    path("question-detail/<int:id>", QuestionDetail.as_view()),
]
