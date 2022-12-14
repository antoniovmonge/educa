# Generated by Django 3.2.15 on 2022-10-13 10:41

from django.db import migrations
import educa.courses.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_content_file_image_text_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=educa.courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=educa.courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
