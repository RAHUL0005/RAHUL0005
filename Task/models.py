from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)

    due_date = models.DateField()
    priority = models.CharField(max_length=20, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    status = models.CharField(max_length=20, choices=[('to_do', 'To Do'), ('in_progress', 'In Progress'), ('completed', 'Completed')])
    description = models.TextField()
    image=models.ImageField(null=True, default='placeholder.png',upload_to='images/')

    def delete_task(self):
        self.delete()

class register(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=200)
