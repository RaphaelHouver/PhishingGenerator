# Generated by Django 4.2.7 on 2023-11-26 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_rename_mailenvoi_fakeemail_mail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campagne',
            name='password_mailEnvoi',
        ),
        
    ]
