# Generated by Django 3.2.7 on 2021-09-17 09:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_alter_repo_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Repo',
            new_name='Repository',
        ),
    ]
