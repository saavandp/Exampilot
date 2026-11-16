from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
# Create your views here.
from exam.models import Assesment
from problems.models import Question

from problems.serializers import QuestionSerializer

class QuestionCreateView(APIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        assesment_object = get_object_or_404(Assesment,id=pk)

        form_data = request.data

        serializer_instance = QuestionSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(assesment=assesment_object)

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class QuestionRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class = QuestionSerializer

    queryset = Question.objects.all()

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]
    