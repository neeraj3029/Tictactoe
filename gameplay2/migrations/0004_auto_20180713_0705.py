# Generated by Django 2.0.5 on 2018-07-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay2', '0003_auto_20180711_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('S', 'Second PLayer Move'), ('D', 'Draw'), ('F', 'First PLayer Move')], default='F', max_length=1),
        ),
    ]
