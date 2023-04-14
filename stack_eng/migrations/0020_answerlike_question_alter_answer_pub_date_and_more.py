# Generated by Django 4.2 on 2023-04-13 21:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stack_eng', '0019_alter_answer_pub_date_alter_answerlike_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerlike',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stack_eng.question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 55, 23, 530603)),
        ),
        migrations.AlterField(
            model_name='answerlike',
            name='like_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 55, 23, 533485)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 55, 23, 531677)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 55, 23, 528970)),
        ),
        migrations.AlterField(
            model_name='questionlike',
            name='like_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 55, 23, 532915)),
        ),
    ]