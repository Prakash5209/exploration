# Generated by Django 4.2.6 on 2023-10-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_formset', '0002_alter_articlemodel_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='ArticleModel',
        ),
    ]
