# Generated by Django 3.0.1 on 2020-04-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipha', '0020_visitor_record_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor_record',
            name='path',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
