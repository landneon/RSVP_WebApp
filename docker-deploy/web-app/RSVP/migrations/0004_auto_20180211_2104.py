# Generated by Django 2.0.2 on 2018-02-12 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSVP', '0003_auto_20180211_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Multi', 'Multiple Choice Question'), ('Free', 'Free Text Question')], max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='roleType',
            field=models.CharField(choices=[('owner', 'owner'), ('guest', 'guest'), ('vendor', 'vendor')], max_length=100),
        ),
    ]
