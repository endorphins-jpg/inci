# Generated by Django 5.0.6 on 2024-06-16 22:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_plataforma_usuarios'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ferramenta',
            name='usuarios',
            field=models.ManyToManyField(related_name='ferramentas', to=settings.AUTH_USER_MODEL),
        ),
    ]