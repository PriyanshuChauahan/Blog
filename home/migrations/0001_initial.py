# Generated by Django 4.1.7 on 2023-03-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('content', models.TextField()),
            ],
        ),
    ]
