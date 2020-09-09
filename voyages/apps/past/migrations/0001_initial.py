# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-09-09 17:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('voyage', '0014_auto_20200909_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltEthnicityName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AltLanguageGroupName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enslaved',
            fields=[
                ('enslaved_id', models.IntegerField(primary_key=True, serialize=False)),
                ('documented_name', models.CharField(blank=True, max_length=25)),
                ('name_first', models.CharField(blank=True, max_length=25, null=True)),
                ('name_second', models.CharField(blank=True, max_length=25, null=True)),
                ('name_third', models.CharField(blank=True, max_length=25, null=True)),
                ('age', models.IntegerField(null=True)),
                ('is_adult', models.NullBooleanField()),
                ('gender', models.IntegerField(null=True)),
                ('height', models.FloatField(null=True, verbose_name=b'Height in inches')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedContribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('contributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('enslaved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.Enslaved')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedContributionLanguageEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('contribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslavedContribution')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedContributionNameEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('contribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslavedContribution')),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=3)),
                ('recordings_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EnslavedSourceConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_order', models.IntegerField()),
                ('text_ref', models.CharField(blank=True, max_length=255)),
                ('enslaved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources_conn', to='past.Enslaved')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.VoyageSources')),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Enslaver alias',
            },
        ),
        migrations.CreateModel(
            name='EnslaverIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_alias', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(null=True)),
                ('birth_month', models.IntegerField(null=True)),
                ('birth_day', models.IntegerField(null=True)),
                ('birth_place', models.CharField(max_length=255, null=True)),
                ('death_year', models.IntegerField(null=True)),
                ('death_month', models.IntegerField(null=True)),
                ('death_day', models.IntegerField(null=True)),
                ('death_place', models.CharField(max_length=255, null=True)),
                ('father_name', models.CharField(max_length=255, null=True)),
                ('father_occupation', models.CharField(max_length=255, null=True)),
                ('mother_name', models.CharField(max_length=255, null=True)),
                ('first_spouse_name', models.CharField(max_length=255, null=True)),
                ('first_marriage_date', models.CharField(max_length=12, null=True)),
                ('second_spouse_name', models.CharField(max_length=255, null=True)),
                ('second_marriage_date', models.CharField(max_length=12, null=True)),
                ('probate_date', models.CharField(max_length=12, null=True)),
                ('will_value_pounds', models.CharField(max_length=12, null=True)),
                ('will_value_dollars', models.CharField(max_length=12, null=True)),
                ('will_court', models.CharField(max_length=12, null=True)),
            ],
            options={
                'verbose_name': 'Enslaver unique identity and personal info',
            },
        ),
        migrations.CreateModel(
            name='EnslaverIdentitySourceConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_order', models.IntegerField()),
                ('text_ref', models.CharField(blank=True, max_length=255)),
                ('identity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslaverIdentity')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='voyage.VoyageSources')),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverMerger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_alias', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(null=True)),
                ('birth_month', models.IntegerField(null=True)),
                ('birth_day', models.IntegerField(null=True)),
                ('birth_place', models.CharField(max_length=255, null=True)),
                ('death_year', models.IntegerField(null=True)),
                ('death_month', models.IntegerField(null=True)),
                ('death_day', models.IntegerField(null=True)),
                ('death_place', models.CharField(max_length=255, null=True)),
                ('father_name', models.CharField(max_length=255, null=True)),
                ('father_occupation', models.CharField(max_length=255, null=True)),
                ('mother_name', models.CharField(max_length=255, null=True)),
                ('first_spouse_name', models.CharField(max_length=255, null=True)),
                ('first_marriage_date', models.CharField(max_length=12, null=True)),
                ('second_spouse_name', models.CharField(max_length=255, null=True)),
                ('second_marriage_date', models.CharField(max_length=12, null=True)),
                ('probate_date', models.CharField(max_length=12, null=True)),
                ('will_value_pounds', models.CharField(max_length=12, null=True)),
                ('will_value_dollars', models.CharField(max_length=12, null=True)),
                ('will_court', models.CharField(max_length=12, null=True)),
                ('comments', models.CharField(max_length=1024)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnslaverMergerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enslaver_identity_id', models.IntegerField()),
                ('merger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslaverMerger')),
            ],
        ),
        migrations.CreateModel(
            name='EnslaverVoyageConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField()),
                ('order', models.IntegerField(null=True)),
                ('enslaver_alias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslaverAlias')),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.Voyage')),
            ],
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LanguageGroup',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name=b'Longitude of point')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name=b'Latitude of point')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModernCountry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name=b'Longitude of Country')),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10, verbose_name=b'Latitude of Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegisterCountry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='languagegroup',
            name='modern_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language_groups', to='past.ModernCountry'),
        ),
        migrations.AddField(
            model_name='ethnicity',
            name='language_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ethnicities', to='past.LanguageGroup'),
        ),
        migrations.AddField(
            model_name='enslaveralias',
            name='identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='past.EnslaverIdentity'),
        ),
        migrations.AlterUniqueTogether(
            name='enslavedname',
            unique_together=set([('name', 'language')]),
        ),
        migrations.AddField(
            model_name='enslavedcontributionlanguageentry',
            name='ethnicity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.Ethnicity'),
        ),
        migrations.AddField(
            model_name='enslavedcontributionlanguageentry',
            name='language_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.LanguageGroup'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='ethnicity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.Ethnicity'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='language_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.LanguageGroup'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='post_disembark_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voyage.Place'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='register_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='past.RegisterCountry'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='sources',
            field=models.ManyToManyField(related_name='_enslaved_sources_+', through='past.EnslavedSourceConnection', to='voyage.VoyageSources'),
        ),
        migrations.AddField(
            model_name='enslaved',
            name='voyage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voyage.Voyage'),
        ),
        migrations.AddField(
            model_name='altlanguagegroupname',
            name='language_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alt_names', to='past.LanguageGroup'),
        ),
        migrations.AddField(
            model_name='altethnicityname',
            name='ethnicity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alt_names', to='past.Ethnicity'),
        ),
        # Make sure that accented letters are considered different in indices and searches.
        migrations.RunSQL(['ALTER TABLE `past_enslavedname` CHANGE COLUMN `name` `name` VARCHAR(255) CHARACTER SET \'utf8mb4\' COLLATE \'utf8mb4_bin\' NOT NULL;'], reverse_sql=migrations.RunSQL.noop),
    ]
