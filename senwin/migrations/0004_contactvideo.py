# Generated by Django 5.0.1 on 2024-12-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senwin', '0003_senwinprojectpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactvideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_video', models.FileField(upload_to='contact_videos/')),
            ],
        ),
    ]
