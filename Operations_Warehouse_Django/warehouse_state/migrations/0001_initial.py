# Generated by Django 4.1 on 2022-09-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessingError',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Topic', models.CharField(db_index=True, max_length=255)),
                ('About', models.CharField(db_index=True, max_length=255)),
                ('ProcessingNode', models.CharField(max_length=64)),
                ('ProcessingApplication', models.CharField(db_index=True, max_length=64)),
                ('ProcessingFunction', models.CharField(max_length=64, null=True)),
                ('ErrorTime', models.DateTimeField(db_index=True)),
                ('ErrorCode', models.CharField(max_length=64)),
                ('ErrorMessage', models.CharField(max_length=4096, null=True)),
                ('Reference1', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingStatus',
            fields=[
                ('ID', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Topic', models.CharField(db_index=True, max_length=255)),
                ('About', models.CharField(db_index=True, max_length=255)),
                ('ProcessingNode', models.CharField(max_length=64)),
                ('ProcessingApplication', models.CharField(max_length=64)),
                ('ProcessingFunction', models.CharField(max_length=64, null=True)),
                ('ProcessingStart', models.DateTimeField()),
                ('ProcessingEnd', models.DateTimeField(null=True)),
                ('ProcessingCode', models.CharField(max_length=64, null=True)),
                ('ProcessingMessage', models.CharField(max_length=4096, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublisherInfo',
            fields=[
                ('ID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('ResourceID', models.CharField(db_index=True, max_length=40)),
                ('Type', models.CharField(max_length=32)),
                ('Version', models.CharField(max_length=32)),
                ('Hostname', models.CharField(max_length=64)),
                ('Location', models.CharField(max_length=64, null=True)),
                ('EntityJSON', models.JSONField()),
                ('CreationTime', models.DateTimeField()),
                ('RecentHistory', models.CharField(max_length=1024)),
            ],
        ),
    ]