# Generated by Django 3.1.4 on 2021-02-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0007_auto_20201031_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
