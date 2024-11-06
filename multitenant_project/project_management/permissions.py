from rest_framework import permissions

class IsAssignedUserOrProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow only the assigned user or the project owner to access/modify the task
        return request.user == obj.assigned_user or request.user == obj.project.owner
