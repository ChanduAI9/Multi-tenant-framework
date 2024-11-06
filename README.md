# Multi-tenant-framework

## Overview
This Django REST Framework project provides a multi-tenant architecture with PostgreSQL. The application includes two main apps for managing tasks and projects, along with full user management capabilities.

## Functionality Overview

### 1. User Management
Allows users to register, retrieve, update, and delete their accounts.

| Endpoint                  | Method | Description                          |
|---------------------------|--------|--------------------------------------|
| `/api/register/`          | POST   | Register a new user                  |
| `/api/users/`             | GET    | List all users (authenticated)       |
| `/api/users/{id}/`        | GET    | Retrieve a specific user             |
| `/api/users/{id}/`        | PUT    | Update a user's details              |
| `/api/users/{id}/`        | DELETE | Delete a user                        |

### 2. Todo Management
Provides basic CRUD operations for managing to-do items.

| Endpoint                  | Method | Description                          |
|---------------------------|--------|--------------------------------------|
| `/api/todos/`             | POST   | Create a new to-do item              |
| `/api/todos/`             | GET    | List all to-do items                 |
| `/api/todos/{id}/`        | GET    | Retrieve a specific to-do item       |
| `/api/todos/{id}/`        | PUT    | Update a specific to-do item         |
| `/api/todos/{id}/`        | DELETE | Delete a specific to-do item         |

### 3. Project Management
Manages projects and their associated tasks.

| Endpoint                  | Method | Description                          |
|---------------------------|--------|--------------------------------------|
| `/api/projects/`          | POST   | Create a new project                 |
| `/api/projects/`          | GET    | List all projects                    |
| `/api/projects/{id}/`     | GET    | Retrieve details of a project        |
| `/api/projects/{id}/`     | PUT    | Update project details               |
| `/api/projects/{id}/`     | DELETE | Delete a project                     |
| `/api/projects/{id}/analytics/` | GET | Retrieve project analytics       |

### 4. Task Management
Enables CRUD operations on tasks associated with projects.

| Endpoint                  | Method | Description                          |
|---------------------------|--------|--------------------------------------|
| `/api/tasks/`             | POST   | Create a task under a project        |
| `/api/tasks/`             | GET    | List all tasks                       |
| `/api/tasks/{id}/`        | GET    | Retrieve details of a specific task  |
| `/api/tasks/{id}/`        | PUT    | Update task details                  |
| `/api/tasks/{id}/`        | DELETE | Delete a task                        |
| `/api/tasks/due_today/`   | GET    | List all tasks due today             |
| `/api/tasks/overdue/`     | GET    | List all overdue tasks               |

### 5. Comment and Activity Log
Allows users to add comments to tasks and view activity logs.

| Endpoint                          | Method | Description                        |
|-----------------------------------|--------|------------------------------------|
| `/api/tasks/{task_id}/comments/`  | POST   | Add a comment to a task            |
| `/api/tasks/{task_id}/comments/`  | GET    | List comments for a task           |
| `/api/tasks/{task_id}/comments/{id}/` | DELETE | Delete a specific comment     |
| `/api/activity_logs/`             | GET    | List all activity logs             |
| `/api/activity_logs/{id}/`        | GET    | Retrieve details of an activity log|


