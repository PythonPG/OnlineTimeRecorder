# Generated by Django 2.0.5 on 2018-06-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180610_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('name_sei', models.CharField(max_length=30)),
                ('name_namae', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='secret',
            field=models.BooleanField(default=False),
        ),
    ]
