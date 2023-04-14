# Generated by Django 4.2 on 2023-04-13 21:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stack_eng', '0017_alter_answer_pub_date_alter_comment_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 51, 38, 397768)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 51, 38, 398281)),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 51, 38, 391129)),
        ),
        migrations.AlterField(
            model_name='questionlike',
            name='like_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 51, 38, 398281)),
        ),
        migrations.CreateModel(
            name='AnswerLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(default=datetime.datetime(2023, 4, 13, 23, 51, 38, 398281))),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stack_eng.answer')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('answer', 'liked_by')},
            },
        ),
    ]
