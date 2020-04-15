# Generated by Django 3.0.1 on 2020-04-12 00:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mipha', '0013_auto_20200411_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mipha.Post')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
