# Generated by Django 4.2.15 on 2024-08-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=60)),
                ('institution', models.CharField(max_length=50)),
                ('duration_from', models.CharField(max_length=20)),
                ('duration_to', models.CharField(max_length=20)),
                ('about_qualification', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=60)),
                ('duration_from', models.CharField(max_length=20)),
                ('duration_to', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=70)),
                ('experience_summary', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='personalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('profile', models.CharField(max_length=60)),
                ('about_you', models.CharField(max_length=800)),
                ('profile_photo', models.ImageField(upload_to='profile_photo')),
                ('background_image', models.ImageField(upload_to='background_image')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.CharField(max_length=200)),
                ('project_image', models.ImageField(upload_to='project_image')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='socialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter', models.CharField(max_length=200)),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
            ],
        ),
    ]
