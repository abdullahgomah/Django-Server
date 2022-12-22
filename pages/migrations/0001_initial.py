# Generated by Django 4.1.4 on 2022-12-20 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "facebook",
                    models.URLField(blank=True, null=True, verbose_name="رابط فيسبوك"),
                ),
                (
                    "twitter",
                    models.URLField(blank=True, null=True, verbose_name="رابط تويتر"),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True, null=True, verbose_name="رابط انستجرام"
                    ),
                ),
                (
                    "youtube",
                    models.URLField(blank=True, null=True, verbose_name="رابط يوتيوب"),
                ),
                ("date", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "معلومات التواصل",
                "verbose_name_plural": "معلومات التواصل",
            },
        ),
        migrations.CreateModel(
            name="Home",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "main_sentence",
                    models.CharField(max_length=150, verbose_name="الجملة الرئيسية"),
                ),
                (
                    "sub_sentence",
                    models.CharField(
                        max_length=250, verbose_name="الجملة الثانوية (الفرعية)"
                    ),
                ),
            ],
            options={
                "verbose_name": "الصفحة الرئيسية",
                "verbose_name_plural": "الصفحة الرئيسية",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="البريد الإلكتروني"),
                ),
                ("details", models.TextField(verbose_name="تفاصيل الرسالة")),
                ("date", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "رسالة",
                "verbose_name_plural": "الرسائل",
            },
        ),
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("details", models.TextField(verbose_name="اسم المصنف / المطبوعة")),
                ("date", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "ترشيرح",
                "verbose_name_plural": "الترشيحات",
            },
        ),
    ]
