# Generated by Django 5.0.2 on 2024-07-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_message_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='voice',
            field=models.FileField(blank=True, null=True, upload_to='voice_messages/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
