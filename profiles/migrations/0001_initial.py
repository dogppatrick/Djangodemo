# Generated by Django 3.2.4 on 2021-06-17 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('context', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
