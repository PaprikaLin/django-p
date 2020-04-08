# Generated by Django 3.0.1 on 2020-04-08 22:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mipha', '0008_auto_20200408_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('comment_type', models.BooleanField()),
                ('user', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
