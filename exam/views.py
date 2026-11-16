from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,ListAPIView,CreateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication,permissions
# Create your views here.

from exam.models import Assesment
from exam.serializer import AssesmentSerializer

from datetime import datetime,time,timedelta



class AssesmentListCreateView(ListAPIView,CreateAPIView):

    authentication_classes = [authentication.BasicAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = AssesmentSerializer

    queryset = Assesment.objects.all()



    def post(self,request):
    
            form_data = request.data
    
            serializer_instance = AssesmentSerializer(data=form_data)

            if serializer_instance.is_valid():

                 cleaned_data = serializer_instance.validated_data

                 exam_date = cleaned_data.get("exam_date")

                 start_time = cleaned_data.get("start_time")

                 duration = cleaned_data.get("duration")

                 end_date_time = datetime.combine(exam_date,start_time)+timedelta(hours=duration)

                 end_time = end_date_time.time()

                 serializer_instance.save(end_time=end_time)

                 return Response(serializer_instance.data,status=status.HTTP_200_OK)

            else:

                 return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



class AssesmentRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

     authentication_classes = [authentication.BasicAuthentication]

     permission_classes = [permissions.IsAdminUser]

     serializer_class = AssesmentSerializer

     queryset = Assesment.objects.all()



     def put(self,request,pk=None):

          instance = get_object_or_404(Assesment,id=pk)

          form_data = request.data

          serilalizer_instance = AssesmentSerializer(data=form_data,instance=instance)

          if serilalizer_instance.is_valid():

               cleaned_data = serilalizer_instance.validated_data

               exam_date = cleaned_data.get("exam_date")

               start_time = cleaned_data.get("start_time")

               duration = cleaned_data.get("duration")

               end_date_time = datetime.combine(exam_date,start_time)+timedelta(hours=duration)

               end_time = end_date_time.time()

               cleaned_data["end_time"] = end_time

               serilalizer_instance.save()

               return Response(serilalizer_instance.data,status=status.HTTP_200_OK)

          else:

               return Response(serilalizer_instance.errors,status=status.HTTP_400_BAD_REQUEST)