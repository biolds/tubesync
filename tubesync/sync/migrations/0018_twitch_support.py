# Generated by Django 3.2.18 on 2023-03-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sync', '0017_alter_source_sponsorblock_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='last_crawl',
            field=models.DateTimeField(blank=True, db_index=True, help_text='Date and time the metadata of the media was last crawled', null=True, verbose_name='last crawl'),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_type',
            field=models.CharField(choices=[('c', 'YouTube channel'), ('i', 'YouTube channel by ID'), ('p', 'YouTube playlist'), ('t', 'Twitch channel')], db_index=True, default='c', help_text='Source type', max_length=1, verbose_name='source type'),
        ),
    ]