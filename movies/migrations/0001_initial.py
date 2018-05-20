# Generated by Django 2.0.5 on 2018-05-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('release_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('aliases', models.CharField(blank=True, max_length=500)),
                ('acted', models.ManyToManyField(blank=True, related_name='actors', to='movies.Movie')),
                ('directed', models.ManyToManyField(blank=True, related_name='directors', to='movies.Movie')),
                ('produced', models.ManyToManyField(blank=True, related_name='producers', to='movies.Movie')),
            ],
        ),
    ]
