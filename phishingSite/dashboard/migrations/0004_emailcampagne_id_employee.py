# Generated by Django 4.2.7 on 2023-11-26 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_campagne_id_entreprise_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcampagne',
            name='id_employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee'),
            preserve_default=False,
        ),
    ]