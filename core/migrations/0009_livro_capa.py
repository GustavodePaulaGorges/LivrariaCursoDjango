# Generated by Django 4.1.1 on 2022-11-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_itenscompra"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="capa",
            field=models.CharField(
                default="https://www.maxicolor.com.br/wp-content/uploads/2019/11/placeholder-3x4-450x600.jpg",
                max_length=10000,
            ),
            preserve_default=False,
        ),
    ]
