# Generated by Django 2.1.1 on 2018-11-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20181111_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitytype',
            name='community_type',
            field=models.CharField(max_length=50, verbose_name='Community Type'),
        ),
    ]
