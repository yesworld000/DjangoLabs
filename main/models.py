from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateField(verbose_name='Created')
    due_on = models.DateField(verbose_name='Due on')
    owner = models.CharField(max_length=50, null=True, blank=True, verbose_name='Owner')
    mark = models.CharField(max_length=50, null=True, blank=True, verbose_name='Mark')

    class Meta:
        ordering = ['due_on']
        verbose_name = 'TODO'
        verbose_name_plural = 'TODOS'
        
    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Task(models.Model):
    task = models.CharField(max_length=20, null=True, blank=True, verbose_name='Task')
    what_to_do = models.CharField(max_length=255, null=True, blank=True, verbose_name='What to do')
    comments = models.CharField(max_length=255, null=True, blank=True, verbose_name='Comments')
    lists = models.ForeignKey(Todo, on_delete=models.CASCADE, null=True, default=3, related_name="tasks")

    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task + self.what_to_do

    def to_json(self):
        return {
            'id': self.id,
            'task': self.task,
            'what_to_do': self.what_to_do,
            'comments': self.comments,
        }