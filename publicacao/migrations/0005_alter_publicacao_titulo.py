# Generated by Django 4.1.1 on 2022-09-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacao', '0004_alter_publicacao_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
    ]
