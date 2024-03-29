# Generated by Django 3.0.7 on 2020-06-08 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle_num', models.IntegerField()),
                ('tittle', models.CharField(max_length=50)),
                ('submissions_solving_count', models.IntegerField(db_column='Submissions_Solving_count')),
                ('submissions_solving', models.CharField(db_column='Submissions_Solving', max_length=15)),
                ('users_solving_count', models.IntegerField(db_column='Users_Solving_count')),
                ('users_solving', models.CharField(db_column='Users_Solving', max_length=15)),
                ('pdf_link', models.TextField()),
                ('text', models.TextField()),
                ('description', models.TextField()),
                ('input', models.TextField(db_column='Input')),
                ('output', models.TextField(db_column='Output')),
                ('sample_input', models.TextField(db_column='Sample_Input')),
                ('sample_output', models.TextField(db_column='Sample_output')),
            ],
            options={
                'db_table': 'cpe',
                'managed': False,
            },
        ),
    ]
