# Generated by Django 2.1 on 2018-09-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypartner',
            name='address_line2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]