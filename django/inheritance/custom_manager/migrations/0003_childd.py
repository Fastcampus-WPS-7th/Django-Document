# Generated by Django 2.0.2 on 2018-02-09 06:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('custom_manager', '0002_childc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('extra_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
