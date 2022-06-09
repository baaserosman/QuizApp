# Generated by Django 4.0.4 on 2022-06-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_alter_question_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('d', 'Difficult'), ('n', 'Normal'), ('e', 'Easy')], max_length=10),
        ),
    ]
