# Generated by Django 5.0.2 on 2024-02-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comments_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
