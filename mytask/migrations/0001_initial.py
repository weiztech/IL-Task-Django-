# Generated by Django 3.2.12 on 2022-03-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('distance', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
