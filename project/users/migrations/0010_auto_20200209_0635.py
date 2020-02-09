# Generated by Django 3.0.3 on 2020-02-09 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_projects_link'),
        ('users', '0009_auto_20200209_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='contributor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='projects.projects'),
        ),
    ]
