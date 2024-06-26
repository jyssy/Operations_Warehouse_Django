# Generated by Django 4.1.13 on 2024-04-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fieldofscience',
            name='fos_source',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='fieldofscience',
            name='nsf_directorage_abbrev',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='fieldofscience',
            name='nsf_directorage_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='fieldofscience',
            name='nsf_directorate_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fieldofscience',
            name='parent_field_of_science_desc',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='fieldofscience',
            name='parent_fos_nsf_abbrev',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='fieldofscience',
            name='parent_fos_nsf_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fieldofscience',
            name='field_of_science_desc',
            field=models.CharField(max_length=80),
        ),
    ]
