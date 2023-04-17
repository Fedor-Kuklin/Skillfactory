from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
import datetime

from django.urls import reverse


# справочники
class ModelTechnics(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model_technics_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модель техники'
        ordering = ['title', ]


class ModelMotor(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model_motor_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'
        ordering = ['title', ]


class ModelTransmissions(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model_transmissions_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссии'
        ordering = ['title', ]


class ModelDrivingBridge(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model_driving_bridge_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущего моста'
        ordering = ['title', ]


class ModelControlledBridge(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('model_controlled_bridge_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемого моста'
        ordering = ['title', ]


class TypeMaintenance(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type_maintenance_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Вид ТО'
        ordering = ['title', ]


class TypeFault(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type_fault_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Характер отказа'
        ordering = ['title', ]


class RecoveryMethod(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recovery_method_update', args=[str(self.id)])

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способы восстановления'
        ordering = ['title', ]


class ServiceCompany(models.Model):
    title = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              limit_choices_to=Q(groups__name='Service company'),
                              verbose_name='Логин')
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервисная компания'
        verbose_name_plural = 'Сервисные компании'
        ordering = ['name', ]


class Client(models.Model):
    title = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              limit_choices_to=Q(groups__name='Clients'),
                              verbose_name='Логин')
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, default='описания нет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['name', ]


class References(models.Model):
    ref = models.CharField(max_length=255,
                           unique=True,
                           verbose_name='Справочники')

    def __str__(self):
        return self.ref

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'


# модель машина
class Car(models.Model):
    factory_num_car = models.CharField(max_length=255,
                                       unique=True,
                                       verbose_name='Зав. № машины')
    model_technics = models.ForeignKey(ModelTechnics,
                                       on_delete=models.CASCADE,
                                       verbose_name='Модель техники')
    model_motor = models.ForeignKey(ModelMotor,
                                    on_delete=models.CASCADE,
                                    verbose_name='Модель двигателя')
    factory_num_motor = models.CharField(max_length=255,
                                         verbose_name='Зав. № двигателя')
    model_transmissions = models.ForeignKey(ModelTransmissions,
                                            on_delete=models.CASCADE,
                                            verbose_name='Модель трансмиссии')
    factory_num_transmissions = models.CharField(max_length=255,
                                                 verbose_name='Зав. № трансмиссии')
    model_driving_bridge = models.ForeignKey(ModelDrivingBridge,
                                             on_delete=models.CASCADE,
                                             verbose_name='Модель ведущего моста')
    factory_num_driving_bridge = models.CharField(max_length=255,
                                                  verbose_name='Зав. № ведущего моста')
    model_controlled_bridge = models.ForeignKey(ModelControlledBridge,
                                                on_delete=models.CASCADE,
                                                verbose_name='Модель управляемого моста')
    factory_num_controlled_bridge = models.CharField(max_length=255,
                                                     verbose_name='Зав. № управляемого моста')
    contract_num_data = models.CharField(max_length=255,
                                         verbose_name='Договор поставки №, дата')
    ship_date = models.DateField(auto_now=False,
                                 auto_now_add=False,
                                 verbose_name='Дата отгрузки с завода')
    consignee = models.CharField(max_length=255,
                                 verbose_name='Грузополучатель (конечный потребитель)')
    delivery_address = models.CharField(max_length=255,
                                        verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.CharField(max_length=255,
                                 verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               verbose_name='Клиент')
    service_company = models.ForeignKey(ServiceCompany,
                                        on_delete=models.CASCADE,
                                        verbose_name='Сервисная компания')

    def __str__(self):
        return self.factory_num_car

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['factory_num_car', ]


# модель техническое обслуживание
class Maintenance(models.Model):
    type_maintenance = models.ForeignKey(TypeMaintenance,
                                         on_delete=models.CASCADE,
                                         verbose_name='Вид ТО')
    data_maintenance = models.DateField(auto_now=False,
                                        auto_now_add=False,
                                        verbose_name='Дата проведения ТО')
    operating_time = models.IntegerField(verbose_name='Наработка, м/час')
    num_order = models.CharField(max_length=255,
                                 unique=True,
                                 verbose_name='№ заказ-наряда')
    data_order = models.DateField(auto_now=False,
                                  auto_now_add=False,
                                  verbose_name='Дата заказ-наряда')
    car = models.ForeignKey(Car,
                            on_delete=models.CASCADE,
                            verbose_name='Машина')
    service_company = models.ForeignKey(ServiceCompany,
                                        on_delete=models.CASCADE,
                                        verbose_name='Сервисная компания')

    def __str__(self):
        return self.type_maintenance.title

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Технические обслуживания'
        ordering = ['data_order', ]


# модель рекламации
class Claim(models.Model):
    data_rejection = models.DateTimeField(auto_now=False,
                                          auto_now_add=False,
                                          verbose_name='Дата заказ-наряда')
    operating_time = models.IntegerField(verbose_name='Наработка, м/час')
    node_failure = models.ForeignKey(TypeFault,
                                     on_delete=models.CASCADE,
                                     verbose_name='Узел отказа')
    description_failure = models.TextField(verbose_name='Описание отказа')
    recovery_method = models.ForeignKey(RecoveryMethod,
                                        on_delete=models.CASCADE,
                                        verbose_name='Способ восстановления')
    spare_parts = models.TextField(verbose_name='Используемые запасные части')
    data_restoration = models.DateTimeField(auto_now=False,
                                            auto_now_add=False,
                                            blank=True, null=True,
                                            verbose_name='Дата восстановления')
    downtime_technic = models.TextField(blank=True, null=True, verbose_name='Время простоя')
    car = models.ForeignKey(Car,
                            on_delete=models.CASCADE,
                            verbose_name='Машина')
    service_company = models.ForeignKey(ServiceCompany,
                                        on_delete=models.CASCADE,
                                        verbose_name='Сервисная компания')

    def __str__(self):
        self.downtime()
        return f'{self.data_rejection}'

    def downtime(self):
        if f'{self.data_restoration}' == 'None':
            claim_downtime = datetime.datetime.now() - self.data_rejection
        else:
            claim_downtime = self.data_restoration - self.data_rejection
        self.downtime_technic = claim_downtime.days
        self.save()

    class Meta:
        verbose_name = 'Рекламация'
        verbose_name_plural = 'Рекламации'
        ordering = ['data_rejection', ]
