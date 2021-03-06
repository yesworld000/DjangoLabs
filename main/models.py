from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=20, null=True, blank=True, verbose_name='Task')
    what_to_do = models.CharField(max_length=255, null=True, blank=True, verbose_name='What to do')
    comments = models.CharField(max_length=255, null=True, blank=True, verbose_name='Comments')

    class Meta:
        verbose_name_plural = 'Tasks'


class Todo(models.Model):
    task = models.ForeignKey(Task, on_delete=models.RESTRICT, verbose_name='Task')
    created = models.DateField(verbose_name='Created')
    due_on = models.DateField(verbose_name='Due on')
    owner = models.CharField(max_length=50, null=True, blank=True, verbose_name='Owner')
    mark = models.CharField(max_length=50, null=True, blank=True, verbose_name='Mark')

    class Meta:
        ordering = ['due_on']
        verbose_name = 'TODO'
        verbose_name_plural = 'TODOS'
