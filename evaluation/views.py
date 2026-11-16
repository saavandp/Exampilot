from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response
from rest_framework import serializers
# Create your views here.
from exam.models import Assesment
from evaluation.models import Submission,Question,Answer
from evaluation.serializers import SubmissionSerializer,AnswerSerializer
from datetime import datetime

class SubmissionStartView(APIView):


    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]


    def post(self,request,pk=None):

        assesment_id = pk

        assesment_object = get_object_or_404(Assesment,id = assesment_id)

        student = request.user

        instance = Submission.objects.create(assessment=assesment_object,student=student)

        serializer_instance = SubmissionSerializer(instance)

        return Response(serializer_instance.data)




class AnswerSubmitView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,pk=None):

        submission_id = pk

        submission_object = get_object_or_404(Submission,id=submission_id)

        form_data = request.data

        serializer_instance = AnswerSerializer(data=form_data)

        question_id = form_data.get("question")

        question_object = Question.objects.filter(id=question_id,assesment=submission_object.assessment)

        if not question_object:

            raise serializers.ValidationError("Question:Question is not in assesment")

        if serializer_instance.is_valid():

            serializer_instance.save(submission=submission_object)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class SubmissionRetrieveView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        submission_object = get_object_or_404(Submission,id=pk)

        serializer_instance = SubmissionSerializer(submission_object)

        return Response(serializer_instance.data)


class AnswerUpdateView(APIView): 

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def patch(self,request,pk=None): #Partial updation

        answer_object = get_object_or_404(Answer, id=pk)

        form_data = request.data

        serializer_instance = AnswerSerializer(data=form_data,instance=answer_object,partial=True)

        if serializer_instance.is_valid():

            serializer_instance.save(evaluated_at=datetime.now())

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)