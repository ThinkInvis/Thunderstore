# Generated by Django 2.1.2 on 2019-05-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0002_modify_meta"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dynamichtml",
            old_name="head_content",
            new_name="content",
        ),
        migrations.RemoveField(
            model_name="dynamichtml",
            name="body_content",
        ),
        migrations.AddField(
            model_name="dynamichtml",
            name="placement",
            field=models.CharField(
                choices=[
                    ("html_head", "html_head"),
                    ("html_body_beginning", "html_body_beginning"),
                    ("content_beginning", "content_beginning"),
                    ("content_end", "content_end"),
                ],
                db_index=True,
                default="html_head",
                max_length=256,
            ),
            preserve_default=False,
        ),
    ]
