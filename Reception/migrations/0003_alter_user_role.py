# Generated by Django 3.2.4 on 2021-07-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reception', '0002_auto_20210703_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Role',
            field=models.CharField(default='Reception Admin', max_length=50),
        ),
    ]
