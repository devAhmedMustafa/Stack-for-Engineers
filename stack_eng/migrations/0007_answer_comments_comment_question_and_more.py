# Generated by Django 4.2 on 2023-04-13 11:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stack_eng', '0006_alter_answer_pub_date_alter_comment_pub_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='comments',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='stack_eng.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='answer',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 13, 11, 8, 754398)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 13, 11, 8, 756913)),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 13, 11, 8, 750865)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
