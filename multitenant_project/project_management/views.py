from rest_framework import viewsets, filters
from .models import Project, Task, Comment, ActivityLog
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer, ActivityLogSerializer,UserRegistrationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Avg
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from datetime import timedelta
from rest_framework import status

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def analytics(self, request, pk=None):
        project = self.get_object()
        total_tasks = project.tasks.count()
        completed_tasks = project.tasks.filter(todo__completed=True).count()
        pending_tasks = total_tasks - completed_tasks
        overdue_tasks = project.tasks.filter(due_date__lt=timezone.now().date(), todo__completed=False).count()
    
    # Calculate average completion time in Python
        completed_tasks_with_time = project.tasks.filter(todo__completed=True, todo__completion_time__isnull=False)
        total_time = timedelta()

    # Calculate total time difference for completed tasks
        if completed_tasks_with_time.exists():  # Check if there are completed tasks with completion time
            for task in completed_tasks_with_time:
                if task.todo.completion_time and task.todo.created_at:
                    time_diff = task.todo.completion_time - task.todo.created_at
                    total_time += time_diff
        # Calculate the average time if there are completed tasks with time
            average_completion_time = total_time / completed_tasks_with_time.count()
        else:
            average_completion_time = None

        analytics = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "overdue_tasks": overdue_tasks,
        "average_completion_time": average_completion_time,
    }
        return Response(analytics)
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['todo__title']
    ordering_fields = ['due_date']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserRegistrationSerializer
    permission_classes=[IsAuthenticated]


