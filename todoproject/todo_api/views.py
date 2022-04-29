from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, generics
from knox.models import AuthToken
from .models import TodoTask, Category
from .serializers import *


# Register/Signup User ApiView
class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Login/Sign in for User ApiView
class LoginApiView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginApiView, self).post(request, format=None)


# Listing all tasks
class TodoListApiView(APIView):
    # to check if the user is authenticated to see the list of the todo tasks
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        tasks = TodoTask.objects.all().order_by('id')
        tasks_serializer = TodoTaskSerializer(tasks, many=True)

        return Response(tasks_serializer.data, status=status.HTTP_200_OK)


# Listing all categories
class CategoryListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all().order_by('id')
        categories_serializer = CategorySerializer(categories, many=True)

        return Response(categories_serializer.data, status=status.HTTP_200_OK)


# Viewing the details of a specific task
class TodoTaskDetailsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        task = TodoTask.objects.filter(id=pk)
        task_serializer = TodoTaskSerializer(task, many=True)
        return Response(task_serializer.data, status=status.HTTP_200_OK)


# Viewing the tasks for a specific category
class CategoryTasksApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        tasks = TodoTask.objects.filter(category=pk)
        print('tasks for category:', tasks)
        task_serializer = TodoTaskSerializer(instance=tasks, many=True)
        return Response(task_serializer.data, status=status.HTTP_200_OK)


# Create/Add a category
class CreateCategoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = {
            'title': request.data.get('title'),
        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Edit/Update a category
class EditCategoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# Delete/Remove a category
class DeleteCategoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        category = Category.objects.get(id=pk)
        category.delete()
        return Response("Category deleted successfully.")


# Create/Add a task
class CreateTodoTaskApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'due_date': request.data.get('due_date'),
            'category': request.data.get('category'),
            'tags': request.data.get('tags')
        }
        serializer = TodoTaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Edit/Update a task
class EditTodoTaskApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        task = TodoTask.objects.get(id=pk)
        serializer = TodoTaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# Delete/Remove a task
class DeleteTaskApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        task = TodoTask.objects.get(id=pk)
        task.delete()
        return Response("Task deleted successfully.")
