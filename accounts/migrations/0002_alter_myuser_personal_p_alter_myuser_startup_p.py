# Generated by Django 4.2.4 on 2023-09-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='personal_P',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='startup_P',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
