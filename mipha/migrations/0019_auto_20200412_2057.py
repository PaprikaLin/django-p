# Generated by Django 3.0.1 on 2020-04-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipha', '0018_visitor_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor_record',
            name='referer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]