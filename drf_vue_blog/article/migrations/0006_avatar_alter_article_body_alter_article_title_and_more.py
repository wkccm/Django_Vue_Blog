# Generated by Django 4.0.4 on 2022-05-05 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_tag_article_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(upload_to='avatar/%Y%m%d')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='article', to='article.avatar'),
        ),
    ]
