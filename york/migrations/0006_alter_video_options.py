# Generated by Django 5.1.6 on 2025-03-03 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('york', '0005_alter_video_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-title']},
        ),
    ]
