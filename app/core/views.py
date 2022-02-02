from django.shortcuts import get_object_or_404
import auth2
from rest_framework import status, generics
from rest_framework.response import Response
from core.serializers import TodoSerializer
from core.models import Todo
from auth2.models import User

import jwt

class TodoView(generics.ListAPIView,generics.CreateAPIView,generics.DestroyAPIView,generics.UpdateAPIView):
    serializer_class=TodoSerializer
    queryset = Todo.objects.all()
    secret_key = 'django-insecure-=%myj1ctr1-vakd0ga#e5frd==2-i)d_8=vl(i)-1hadgy^^%c'

    def update(self,request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            payload = jwt.decode(token, self.secret_key)
            # user = User.objects.filter(username=payload['username'])[0]
            request.data['user_id'] = payload['id']
            todo = get_object_or_404(Todo, id = request.data['id'])
            if todo.user_id != payload['id']:
                raise Exception()
        except:
            return Response({'Error': "Invalid Token"}, status="400")
        
        todo_serializer = self.serializer_class(todo, data=request.data ,read_only=False, allow_null=True,partial=True) 
        if todo_serializer.is_valid(raise_exception=True): 
            todo_serializer.save()
            return Response(todo_serializer.data, status="200")
            # return Response({'Completed': "Updated item"}, status="200")
        return Response({'Sorry': "Could not updated data "}, status="400")

    def post(self, request, *args, **kwargs):    
        try:
            token = request.GET.get('token')
            print('AAAAAAAAAAAAAA')
            print(token)
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            print('BBBBBBBBBBBBB')
            print(payload)
            # user = User.objects.filter(username=payload['username'])[0]
            print('CCCCCCCCCCCCC')
            # print(user)
            request.data['user_id'] = payload['id']
        except:
            return Response({'Error': "Invalid Token"}, status="400")

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)
        # return self.create(request, *args, **kwargs)
        return Response({'ERROR': "COULD not created todo"}, status="401")

    def delete(self,request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            payload = jwt.decode(token, self.secret_key)
            # user = User.objects.filter(username=payload['username'])[0]
            request.data['user_id'] = payload['id']
            todo = get_object_or_404(Todo, id = request.data['id'])
            if todo.user_id != payload['id']:
                raise Exception()
        except:
            return Response({'Error': "Invalid Token"}, status="400")

        title = todo.title
        id = todo.id
        todo.delete()
        return Response({'Completed': f"Deleted item is {id} {title}"}, status="202")

    def get_queryset(self):
        try:
            token = self.request.GET.get('token')
            payload = jwt.decode(token, self.secret_key)
            # user = User.objects.filter(username=payload['username'])[0]
            self.request.data['user_id'] = payload['id']
        except:
            return Response({'Error': "Invalid Token"}, status="400")

        queryset = super().get_queryset()
        # todo_id = self.request.GET.get('id')
        user_id = self.request.data['user_id']
        if user_id:
            try:
                queryset = Todo.objects.filter(user_id = user_id)
                if len(queryset)==0:
                    raise Exception()
            except:
                queryset = get_object_or_404(Todo, user_id = user_id)
        return queryset