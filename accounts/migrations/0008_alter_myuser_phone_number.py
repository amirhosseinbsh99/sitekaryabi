# Generated by Django 4.2.4 on 2023-11-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_myuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
