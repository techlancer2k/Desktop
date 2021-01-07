# Generated by Django 3.1 on 2020-08-17 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField()),
                ('department', models.CharField(max_length=2)),
                ('section', models.CharField(max_length=1)),
            ],
            options={
                'unique_together': {('batch', 'department', 'section')},
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=500)),
                ('option1', models.TextField(max_length=100)),
                ('option2', models.TextField(max_length=100)),
                ('option3', models.TextField(max_length=100)),
                ('option4', models.TextField(max_length=100)),
                ('option5', models.TextField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('classroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('subject_code', models.CharField(max_length=6)),
                ('classroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.classroom')),
            ],
            options={
                'unique_together': {('classroom_id', 'semester', 'subject_code')},
            },
        ),
        migrations.CreateModel(
            name='TimeTableFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
                ('classroom_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.classroom')),
            ],
            options={
                'unique_together': {('classroom_id', 'semester')},
            },
        ),
        migrations.CreateModel(
            name='SubmitAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('submission_timestamp', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
                ('assigned_assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.subject')),
            ],
            options={
                'unique_together': {('assigned_assignment_id', 'rollno')},
            },
        ),
        migrations.CreateModel(
            name='PollResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('response', models.IntegerField()),
                ('poll_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.poll')),
            ],
            options={
                'unique_together': {('rollno', 'poll_id')},
            },
        ),
        migrations.CreateModel(
            name='MaterialFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.subject')),
            ],
            options={
                'unique_together': {('subject_id', 'topic')},
            },
        ),
        migrations.CreateModel(
            name='AssignAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField()),
                ('file', models.FileField(upload_to='')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadApp.subject')),
            ],
            options={
                'unique_together': {('subject_id', 'topic')},
            },
        ),
    ]
