# Generated by Django 5.0.7 on 2024-11-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.IntegerField()),
                ('projects', models.IntegerField()),
                ('HoursOfSupport', models.IntegerField()),
                ('workers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('profile_photo', models.ImageField(upload_to='profiles')),
            ],
        ),
    ]