from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ProjectAssignment(models.Model):
    project = models.ForeignKey(Project, related_name='assignments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('project', 'user')

    def __str__(self):
        return f"{self.user.username} assigned to {self.project.name}"

