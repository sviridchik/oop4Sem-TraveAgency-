# Generated by Django 3.2.3 on 2021-05-24 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='Цена')),
                ('connected_historical_facts', models.TextField(verbose_name='Исторические события')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательности',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_products', models.PositiveIntegerField(default=0)),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена')),
                ('in_order', models.BooleanField(default=False)),
                ('for_anonymous_user', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Climate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.FloatField(max_length=2, verbose_name='влажность')),
                ('t', models.FloatField(verbose_name='Температура ')),
                ('amount_sunny_days', models.IntegerField(verbose_name='Количество солнечных дней в году')),
                ('v_wind', models.FloatField(verbose_name='Скорость ветра')),
                ('type', models.CharField(choices=[('приятный', (('умеренный', 'умеренный'), ('тропический', 'тропический'))), ('не самый приятный', (('полярный', 'полярный'), ('экваториальный', 'экваториальный')))], max_length=255)),
                ('pres', models.FloatField(verbose_name='Атмосферное давление')),
                ('recommendation', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'Климат',
                'verbose_name_plural': 'Климаты',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('tags', models.TextField(max_length=255, verbose_name='Теги')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('attractions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.attractions', verbose_name='Достопримечательности')),
                ('climate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.climate', verbose_name='Климат')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='Цена за сутки')),
                ('requirments', models.TextField(verbose_name='Требования')),
                ('risk_of_trauma', models.IntegerField(verbose_name='Вероятность получения травмы')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'Развлечение',
                'verbose_name_plural': 'Развлечения',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('family', models.TextField(choices=[('наиболее распространенные', (('Нигер – Конго', 'Нигер – Конго'), ('Австронезийский', 'Австронезийский'), ('Транс-новогвинейский', 'Транс-новогвинейский'), ('Сино-тибетский', 'Сино-тибетский'), ('Индоевропейский', 'Индоевропейский'), ('Австралийский', 'Австралийский'))), ('менее распространенные', (('Араваканский', 'Араваканский'), ('Манде', 'Манде '), ('Тупиан', 'Тупиан')))], max_length=255, verbose_name='семейство')),
                ('a_dial', models.IntegerField(verbose_name='Количество диалектов')),
                ('speed_lern', models.CharField(choices=[('fast', 'fast'), ('medium', 'medium'), ('slow', 'slow')], max_length=255, verbose_name='Скорость освоения')),
                ('users', models.IntegerField(verbose_name='Количество носителей')),
                ('price', models.FloatField(verbose_name='Цена за сутки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('alphabet', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='Med',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('av_price', models.FloatField(verbose_name='Средняя цена')),
                ('working_days', models.CharField(max_length=255, verbose_name='Дни работы')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='ссылка')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'Мед учреждение',
                'verbose_name_plural': 'Мед учреждения',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('idOrder', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('p', 'inprogress'), ('c', 'canceled'), ('clo', 'closed')], max_length=255)),
                ('price', models.FloatField(verbose_name='Общая стоимость')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='PromoCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, unique=True)),
                ('discount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Промокод',
                'verbose_name_plural': 'Промокоды',
            },
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, unique=True, verbose_name='Содержание')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'вопрос викторины',
                'verbose_name_plural': 'вопросы викторины',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('monoteism', models.BooleanField(verbose_name='Монотеизм')),
                ('neg_atitude', models.CharField(max_length=255, verbose_name='Недружелюбные')),
                ('fasting', models.BooleanField(verbose_name='Пост')),
                ('description', models.TextField(blank=True, default=None, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
            options={
                'verbose_name': 'Религия',
                'verbose_name_plural': 'Религии',
            },
        ),
        migrations.CreateModel(
            name='Translator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('definite', (('woman', 'woman'), ('man', 'man'))), ('indefinite', (('trans', 'trans'), ('other', 'other')))], max_length=100, verbose_name='Пол')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('price', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='Цена за час')),
                ('experience', models.IntegerField(verbose_name='Лет опыта')),
                ('languages', models.CharField(max_length=255, verbose_name='Языки')),
                ('recommendation', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='ссылка')),
            ],
            options={
                'verbose_name': 'Переводчик',
                'verbose_name_plural': 'Переводчики',
            },
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('necessary_vaccation', models.CharField(max_length=255, verbose_name='Необходитмве прививки')),
                ('phobias', models.CharField(max_length=255, verbose_name='фобии')),
                ('desiase', models.CharField(max_length=255, verbose_name='Заболевания')),
                ('medical_institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.med', verbose_name='Медицинское учреждение')),
            ],
            options={
                'verbose_name': 'Ограничение',
                'verbose_name_plural': 'Ограничения',
            },
        ),
        migrations.CreateModel(
            name='QuizAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255, verbose_name='Содержание')),
                ('is_right', models.BooleanField(verbose_name='Правильный')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quizquestion', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'ответ викторины',
                'verbose_name_plural': 'ответы викторины',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(to='main.QuizQuestion', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Викторина',
                'verbose_name_plural': 'Викторины',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('family_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(blank=True, choices=[('definite', (('w', 'woman'), ('m', 'man'))), ('indefinite', (('t', 'trans'), ('o', 'other')))], max_length=100, null=True, verbose_name='Пол')),
                ('email', models.CharField(default='', max_length=255, verbose_name='email')),
                ('amount_members', models.IntegerField(blank=True, null=True, verbose_name='количество членов семьи')),
                ('abilities', models.CharField(blank=True, default='', max_length=255, verbose_name='Навыки')),
                ('desease', models.CharField(blank=True, default='', max_length=255, verbose_name='Заболевания')),
                ('phobias', models.CharField(blank=True, default='', max_length=255, verbose_name='Фобия')),
                ('languages', models.CharField(blank=True, default='', max_length=255, verbose_name='Языки')),
                ('vaccition', models.CharField(blank=True, default='', max_length=255, verbose_name='Прививки')),
                ('phone', models.CharField(blank=True, default='', max_length=255, verbose_name='телефон')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Заказ')),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.quiz', verbose_name='Викторина')),
                ('quiz_answers', models.ManyToManyField(to='main.QuizAnswer', verbose_name='Ответы в викторине')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('idPacket', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('duration', models.PositiveIntegerField(verbose_name='Продолжительность в днях')),
                ('price', models.FloatField(verbose_name='Цена за сутки')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.country', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Пакет',
                'verbose_name_plural': 'Пакеты',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='packet',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.packet'),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=3, max_digits=9, verbose_name='Цена')),
                ('stars', models.IntegerField(verbose_name='Количество звезд')),
                ('food_options', models.TextField(verbose_name='варианты питания')),
                ('people_in_room', models.TextField(verbose_name='Сколько местные номера есть')),
                ('swimming_pool', models.BooleanField(verbose_name='Наличие бассейна')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('link', models.CharField(blank=True, max_length=255, verbose_name='ссылка')),
                ('entertainment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.entertainment', verbose_name='Развлечение')),
            ],
            options={
                'verbose_name': 'Отель',
                'verbose_name_plural': 'Отели',
            },
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.currency', verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='country',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.hotel', verbose_name='Отель'),
        ),
        migrations.AddField(
            model_name='country',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language', verbose_name='Язык'),
        ),
        migrations.AddField(
            model_name='country',
            name='religion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.religion', verbose_name='Религия'),
        ),
        migrations.AddField(
            model_name='country',
            name='restriction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.restriction', verbose_name='Ограничение'),
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('qty', models.PositiveIntegerField(default=1)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_products', to='main.cart', verbose_name='Корзина')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.person', verbose_name='Покупатель')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='packet',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='main.Packet'),
        ),
        migrations.AddField(
            model_name='cart',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.person', verbose_name='Владелец'),
        ),
    ]
