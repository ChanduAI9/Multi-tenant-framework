from rest_framework import serializers
from .models import Project, Task, Comment, ActivityLog
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    completion_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_completion_percentage(self, obj):
        total_tasks = obj.tasks.count()
        if total_tasks == 0:
            return 0
        completed_tasks = obj.tasks.filter(todo__completed=True).count()
        return (completed_tasks / total_tasks) * 100

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
    def update(self,instance,validated_data):
        #updating existing user
        instance.username = validated_data.get('username',instance.username)
        instance.email=validated_data.get('email',instance.email)
        password=validated_data.get('password',None)

        if password:
            instance.set_password(password)
        instance.save()
        return instance
    