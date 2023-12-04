# Generated by Django 4.2.7 on 2023-12-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.CharField(blank=True, max_length=80, null=True)),
                ('phone', models.CharField(blank=True, max_length=80, null=True)),
                ('department', models.CharField(blank=True, max_length=80, null=True)),
                ('title', models.CharField(blank=True, max_length=80, null=True)),
                ('body', models.TextField(blank=True, max_length=80, null=True)),
                ('track_code', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]