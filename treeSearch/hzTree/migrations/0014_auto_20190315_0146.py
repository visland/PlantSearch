# Generated by Django 3.0.dev20190216065628 on 2019-03-15 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hzTree', '0013_auto_20190314_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tree',
            old_name='biename',
            new_name='alternative_name',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='kname',
            new_name='family_name',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='ldname',
            new_name='genus_name',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='sname',
            new_name='latin_name',
        ),
        migrations.RenameField(
            model_name='tree',
            old_name='zname',
            new_name='species_name',
        ),
    ]
