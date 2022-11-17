from rest_framework.views import APIView
from .models import Employe
from .serializer import Employe_serilaizer
from rest_framework.response import Response
from rest_framework import status

class Employe_Api(APIView):
    def get(self, request,pk):
        try:
            emp = Employe.objects.get(id=pk)
            emp_serializer = Employe_serilaizer(emp)
            return Response(emp_serializer.data)
        except:
            emp = Employe.objects.all()
            emp_serializer = Employe_serilaizer(emp,many=True)
            return Response(emp_serializer.data)

    def post(self,request):
        postman_data = request.data

        if request.method == "POST":
            emp_serializer = Employe_serilaizer(data=postman_data)

            if emp_serializer.is_valid():
                emp_serializer.save()
                return Response(emp_serializer.data, status=status.HTTP_201_CREATED)
            return Response(emp_serializer.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        postman_data = request.data

        if request.method == 'PUT':
            emp = Employe.objects.get(id=pk)
            emp_serializer = Employe_serilaizer(emp, data=postman_data)

            if emp_serializer.is_valid():
                emp_serializer.save()
                return Response(emp_serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('bad reqqquest')

    def patch(self,request,pk):
        postman_data = request.data

        if request.method == 'PATCH':
            stu = Employe.objects.get(id=pk)
            stu_serializer = Employe_serilaizer(stu, data=postman_data, partial=True)

            if stu_serializer.is_valid():
                stu_serializer.save()
                return Response(stu_serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(stu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('bad reqqquest')

    def delete(self,request,pk):
        idd = pk
        stu = Employe.objects.get(id=idd)
        stu.delete()
        return Response('data delete ho gaya,,,,,')

