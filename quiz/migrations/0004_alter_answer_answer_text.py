# Generated by Django 4.0.4 on 2022-06-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_answer_question_alter_question_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(max_length=50),
        ),
    ]
