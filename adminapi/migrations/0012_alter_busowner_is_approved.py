# Generated by Django 4.2.5 on 2024-03-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0011_alter_busowner_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busowner',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]