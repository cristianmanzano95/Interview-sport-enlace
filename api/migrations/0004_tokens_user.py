# Generated by Django 3.2.4 on 2021-06-20 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_users_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokens',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
    ]
