# Generated by Django 3.1.7 on 2021-03-06 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(blank=True, max_length=20, null=True, verbose_name='Task')),
                ('what_to_do', models.CharField(blank=True, max_length=255, null=True, verbose_name='What to do')),
                ('comments', models.CharField(blank=True, max_length=255, null=True, verbose_name='Comments')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(verbose_name='Created')),
                ('due_on', models.DateField(verbose_name='Due on')),
                ('owner', models.CharField(blank=True, max_length=50, null=True, verbose_name='Owner')),
                ('mark', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mark')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.task', verbose_name='Task')),
            ],
            options={
                'verbose_name': 'TODO',
                'verbose_name_plural': 'TODOS',
                'ordering': ['due_on'],
            },
        ),
    ]
