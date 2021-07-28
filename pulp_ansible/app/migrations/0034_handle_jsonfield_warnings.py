# Generated by Django 3.2.5 on 2021-07-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ansible', '0033_swap_distribution_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionimport',
            name='messages',
            field=models.JSONField(default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='contents',
            field=models.JSONField(default=list, editable=False),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='dependencies',
            field=models.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='docs_blob',
            field=models.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='files',
            field=models.JSONField(default=dict, editable=False),
        ),
        migrations.AlterField(
            model_name='collectionversion',
            name='manifest',
            field=models.JSONField(default=dict, editable=False),
        ),
    ]
