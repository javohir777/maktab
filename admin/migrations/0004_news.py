# Generated by Django 3.2.6 on 2021-08-14 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_contest'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('imageUrl', models.TextField()),
                ('description', models.TextField()),
                ('info', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
