# Generated by Django 2.0.5 on 2018-07-15 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay2', '0004_auto_20180713_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('F', 'First PLayer Move'), ('D', 'Draw'), ('S', 'Second PLayer Move')], default='F', max_length=1),
        ),
    ]
