# Generated by Django 2.2.1 on 2019-05-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img_link', models.CharField(max_length=5000)),
                ('web_link', models.CharField(max_length=5000)),
            ],
        ),
    ]
