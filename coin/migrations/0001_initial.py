# Generated by Django 3.2.9 on 2021-11-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True, default=0)),
                ('rank', models.IntegerField(blank=True, default=0)),
                ('symbol', models.CharField(max_length=50)),
                ('image', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['rank'],
            },
        ),
    ]
