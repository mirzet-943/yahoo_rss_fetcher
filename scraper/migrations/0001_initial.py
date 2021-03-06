# Generated by Django 3.2.9 on 2021-11-14 22:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=500)),
                ('pubDate', models.DateTimeField()),
                ('symbol', models.CharField(max_length=50)),
            ],
        ),
    ]
