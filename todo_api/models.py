from django.db import models

# class models which represents a task with title and completion status
class Task(models.Model):
    # title will be charfield (strings with max length of 200)
    title = models.CharField(max_length=200)
    # completed status will be true or false (boolean)
    completed = models.BooleanField(default=False)

    # to show the title as text
    def __str__(self):
        return self.title