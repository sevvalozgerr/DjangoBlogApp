# Generated by Django 5.0.2 on 2024-02-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tag_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
