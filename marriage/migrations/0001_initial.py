# Generated by Django 3.0.1 on 2019-12-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=50)),
                ('guest_role', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=500)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
