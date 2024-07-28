from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Группу'
        verbose_name_plural = 'Группы'
        db_table = 'Groups'

    def __str__(self):
        return self.name


class Voices(models.Model):
    voice1 = models.FileField(upload_to="media", null=True, blank=True)
    voice2 = models.FileField(upload_to="media", null=True, blank=True)
    voice3 = models.FileField(upload_to="media", null=True, blank=True)
    voice4 = models.FileField(upload_to="media", null=True, blank=True)
    voice5 = models.FileField(upload_to="media", null=True, blank=True)
    voice6 = models.FileField(upload_to="media", null=True, blank=True)
    voice7 = models.FileField(upload_to="media", null=True, blank=True)
    voice8 = models.FileField(upload_to="media", null=True, blank=True)
    voice9 = models.FileField(upload_to="media", null=True, blank=True)
    voice10 = models.FileField(upload_to="media", null=True, blank=True)

    class Meta:
        verbose_name = 'Голосовой'
        verbose_name_plural = 'Голосовые'
        db_table = 'Voices'

    def __str__(self):
        return f'{self.id:05}'


class Pills(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='pills_images', blank=True, null=True, verbose_name='Изображение')
    container = models.PositiveIntegerField(default=1, verbose_name='Бокс')

    class Meta:
        verbose_name = 'Медикамент'
        verbose_name_plural = 'Медикаменты'
        db_table = 'Pills'

    def __str__(self):
        return self.name


class Schedules(models.Model):
    pill = models.ForeignKey(to=Pills, on_delete=models.CASCADE, verbose_name='Медикамент')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    time1 = models.TimeField(default=None, verbose_name='1 прием')
    time2 = models.TimeField(default=None, verbose_name='2 прием')
    time3 = models.TimeField(default=None, verbose_name='3 прием')

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        db_table = 'Schedules'

    def __str__(self):
        return f'{self.pill} Количество: {self.quantity},' \
               f' время: {self.time1}, {self.time2}, {self.time3}'


class Patients(models.Model):
    group = models.ForeignKey(to=Groups, on_delete=models.CASCADE, verbose_name='Группа')
    first_name = models.CharField(max_length=30, verbose_name='Имя пациента')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия пациента')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')
    fingerPrint = models.CharField(max_length=5, blank=True, null=True, verbose_name='Номер отпечатка')
    phone = models.CharField(max_length=12, verbose_name='Телефон пациента')
    volume = models.CharField(max_length=3, verbose_name='Объем воды')
    voices = models.ForeignKey(to=Voices, on_delete=models.CASCADE, verbose_name='Голосовые')
    schedule = models.ManyToManyField(to=Schedules, verbose_name='Расписание')

    class Meta:
        verbose_name = 'Пациента'
        verbose_name_plural = 'Пациенты'
        db_table = 'Patients'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def display_id(self):
        return f'{self.id:05}'