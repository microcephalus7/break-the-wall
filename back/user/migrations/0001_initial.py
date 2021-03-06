# Generated by Django 3.2.6 on 2021-08-27 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128)),
                ('password', models.EmailField(max_length=50)),
                ('pubDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('username', models.TextField(max_length=20, null=True)),
                ('phoneNumber', models.TextField(max_length=12, null=True)),
                ('male', models.BooleanField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.account')),
            ],
        ),
    ]
