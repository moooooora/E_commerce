# Generated by Django 5.0.1 on 2024-02-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('ratio', models.FloatField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupones',
            },
        ),
    ]