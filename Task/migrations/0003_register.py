# Generated by Django 4.2.10 on 2024-03-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_task_image_alter_task_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
