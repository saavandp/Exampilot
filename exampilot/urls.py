"""
URL configuration for exampilot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Exams
from exam.views import AssesmentListCreateView
from exam.views import AssesmentRetrieveUpdateDeleteView

#Accounts
from accounts.views import AdminCreateUser
from accounts.views import StudentCreateView

#problem
from problems.views import QuestionCreateView
from problems.views import QuestionRetrieveUpdateDeleteView

#Submission
from evaluation.views import SubmissionStartView
from evaluation.views import SubmissionRetrieveView

#Answer
from evaluation.views import AnswerSubmitView,AnswerUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/assesments/',AssesmentListCreateView.as_view()),
    path('exam/assesments/<int:pk>/',AssesmentRetrieveUpdateDeleteView.as_view()),
    path('owner/register/',AdminCreateUser.as_view()),
    path('assesments/<int:pk>/question/',QuestionCreateView.as_view()),
    path('question/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view()),
    path('student/register/',StudentCreateView.as_view()),
    path('assesments/<int:pk>/submission/',SubmissionStartView.as_view()),
    path('submission/<int:pk>/answer/',AnswerSubmitView.as_view()),
    path('submission/<int:pk>/',SubmissionRetrieveView.as_view()),
    path('answer/<int:pk>/',AnswerUpdateView.as_view()),
]