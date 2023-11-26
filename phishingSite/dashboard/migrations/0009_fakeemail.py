# Generated by Django 4.2.7 on 2023-11-26 16:46

import dashboard.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_campagne_id_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='fakeEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailEnvoi', models.EmailField(max_length=254)),
                ('password_mailEnvoi', dashboard.fields.HashField(editable=False, max_length=64)),
            ],
        ),
    ]
