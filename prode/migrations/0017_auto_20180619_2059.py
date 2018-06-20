# Generated by Django 2.0.4 on 2018-06-19 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prode', '0016_auto_20180619_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='match',
        ),
        migrations.AddField(
            model_name='match',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prode.Competition'),
        ),
    ]
