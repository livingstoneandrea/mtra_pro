# Generated by Django 3.0.3 on 2020-10-30 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Preference',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='education_level',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='employment_detail',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='file_upload',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Education_level',
        ),
        migrations.DeleteModel(
            name='Employment_detail',
        ),
        migrations.DeleteModel(
            name='File_uploaded',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]