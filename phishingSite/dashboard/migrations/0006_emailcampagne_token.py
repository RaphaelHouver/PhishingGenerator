# Generated by Django 4.2.7 on 2023-11-26 12:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_campagne_id_entreprise_emailcampagne_id_campagne_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcampagne',
            name='token',
            field=models.CharField(default=0, max_length=6, validators=[django.core.validators.MaxLengthValidator(limit_value=6)]),
            preserve_default=False,
        ),
    ]
