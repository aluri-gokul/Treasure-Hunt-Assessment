# Generated by Django 4.2 on 2023-04-14 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_users_scoreandtime_delete_scoreandtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='scoreAndTime',
        ),
        migrations.CreateModel(
            name='ScoreAndTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cl1Scr', models.IntegerField(default=0, null=True)),
                ('cl1Tym', models.IntegerField(default=0, null=True)),
                ('cl2Scr', models.IntegerField(default=0, null=True)),
                ('cl2Tym', models.IntegerField(default=0, null=True)),
                ('cl3Scr', models.IntegerField(default=0, null=True)),
                ('cl3Tym', models.IntegerField(default=0, null=True)),
                ('cl4Scr', models.IntegerField(default=0, null=True)),
                ('cl4Tym', models.IntegerField(default=0, null=True)),
                ('cl5Scr', models.IntegerField(default=0, null=True)),
                ('cl5Tym', models.IntegerField(default=0, null=True)),
                ('cl6Scr', models.IntegerField(default=0, null=True)),
                ('cl6Tym', models.IntegerField(default=0, null=True)),
                ('cl7Scr', models.IntegerField(default=0, null=True)),
                ('cl7Tym', models.IntegerField(default=0, null=True)),
                ('cl8Scr', models.IntegerField(default=0, null=True)),
                ('cl8Tym', models.IntegerField(default=0, null=True)),
                ('cl9Scr', models.IntegerField(default=0, null=True)),
                ('cl9Tym', models.IntegerField(default=0, null=True)),
                ('cl0Scr', models.IntegerField(default=0, null=True)),
                ('cl0Tym', models.IntegerField(default=0, null=True)),
                ('userEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.users')),
            ],
        ),
    ]
