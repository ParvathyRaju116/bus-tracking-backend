# Generated by Django 4.2.5 on 2024-04-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0016_alter_busstopdetail_busstop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stop',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
