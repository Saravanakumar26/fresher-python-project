# Generated by Django 5.0.1 on 2024-02-14 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('qualification', models.CharField(max_length=20)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('objective', models.TextField()),
            ],
        ),
    ]
