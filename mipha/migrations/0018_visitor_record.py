# Generated by Django 3.0.1 on 2020-04-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipha', '0017_auto_20200412_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.CharField(max_length=50)),
                ('user_agent', models.CharField(max_length=200)),
                ('referer', models.CharField(max_length=50)),
            ],
        ),
    ]
