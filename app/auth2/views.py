from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status, generics
from rest_framework.response import Response
from auth2.models import User
from auth2.serializers import UserSerializer
# Create your views here.
import jwt 


class RegisterAPIView(generics.ListAPIView,generics.CreateAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    secret_key = 'django-insecure-=%myj1ctr1-vakd0ga#e5frd==2-i)d_8=vl(i)-1hadgy^^%c'

    def update(self,request, *args, **kwargs):
        try:
            user = User.objects.filter(username=request.data['username'], password = request.data['current_password'])[0]
            print(user)
            del request.data['current_password']
            print(user)
            user_serializer = self.serializer_class(user, data=request.data ,read_only=False, allow_null=True,partial=True) 
            if user_serializer.is_valid(raise_exception=True): 
                user_serializer.save()
            return Response(f'Updated item: {user_serializer.data}', status="200")
        except:
            return Response({'Sorry': "Could not updated data "}, status="400")

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, *args, **kwargs):
        try:
            user = User.objects.filter(username = request.data['username'], password = request.data['password'] )[0]
            username = user.username
            id = user.id
            user.delete()
            return Response({'Completed': f"Deleted item is {id} {username}"}, status="202")
        except:
            return Response({'Error': "Invalid username or password"}, status="400")



class LoginAPIView(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if username and password:
            user = User.objects.filter(username=username, password= password)
            print(user)
            if len(user) > 0:
                secret_key = 'django-insecure-=%myj1ctr1-vakd0ga#e5frd==2-i)d_8=vl(i)-1hadgy^^%c'
                token = jwt.encode({'id':user[0].id,'username':request.data['username'], 'password': request.data['password']}, secret_key, 'HS256').decode('utf-8')
                return Response(f'id:{user[0].id}, token:=>  {token}  <=', status="200")
        return Response('LOGIN ERROR', status=status.HTTP_400_BAD_REQUEST)
