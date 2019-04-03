# Generated by Django 2.1.7 on 2019-03-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_link', models.CharField(max_length=600, verbose_name='GitHub')),
                ('contact_link', models.CharField(max_length=600, verbose_name='Contato')),
                ('profile_photo', models.ImageField(blank=True, upload_to='', verbose_name='Foto de Perfil')),
            ],
            options={
                'verbose_name': 'Developer',
                'verbose_name_plural': 'Developers',
            },
        ),
    ]
