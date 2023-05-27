# Generated by Django 4.2 on 2023-05-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='event_involved',
        ),
        migrations.RemoveField(
            model_name='person',
            name='event_involved',
        ),
        migrations.RemoveField(
            model_name='person',
            name='organization_involved',
        ),
        migrations.AddField(
            model_name='organization',
            name='event_involved',
            field=models.ManyToManyField(null=True, to='timeline.event'),
        ),
        migrations.AddField(
            model_name='person',
            name='event_involved',
            field=models.ManyToManyField(null=True, to='timeline.event'),
        ),
        migrations.AddField(
            model_name='person',
            name='organization_involved',
            field=models.ManyToManyField(null=True, to='timeline.organization'),
        ),
    ]
