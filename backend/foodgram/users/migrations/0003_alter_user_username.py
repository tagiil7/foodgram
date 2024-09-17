# Generated by Django 3.2.3 on 2024-09-02 00:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator(message='Недопустимый никнейм', regex='^[\\w.@+-]')], verbose_name='Уникальный юзернейм'),
        ),
    ]