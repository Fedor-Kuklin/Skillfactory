
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, Textarea, DateTimeField, ModelChoiceField, DateField
from .models import (Car,
                     Maintenance,
                     Claim,
                     ModelTechnics,
                     ModelTransmissions,
                     ModelMotor,
                     ModelDrivingBridge,
                     ModelControlledBridge,
                     TypeMaintenance,
                     TypeFault,
                     RecoveryMethod,
                     Client,
                     ServiceCompany,
                     )


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class CarForm(ModelForm):
    factory_num_car = CharField(max_length=255,
                                empty_value='Без названия',
                                label='Зав. № машины')
    model_technics = ModelChoiceField(queryset=ModelTechnics.objects.all(),
                                      label='Модель техники')
    model_motor = ModelChoiceField(queryset=ModelMotor.objects.all(),
                                   label='Модель двигателя'
                                   )
    factory_num_motor = CharField(max_length=255,
                                  empty_value='Без названия',
                                  label='Зав. № двигателя')
    model_transmissions = ModelChoiceField(queryset=ModelTransmissions.objects.all(),
                                           label='Модель трансмиссии')
    factory_num_transmissions = CharField(max_length=255,
                                          empty_value='Без названия',
                                          label='Зав. № трансмиссии')
    model_driving_bridge = ModelChoiceField(queryset=ModelDrivingBridge.objects.all(),
                                            label='Модель ведущего моста')
    factory_num_driving_bridge = CharField(max_length=255,
                                           empty_value='Без названия',
                                           label='Зав. № ведущего моста')
    model_controlled_bridge = ModelChoiceField(queryset=ModelControlledBridge.objects.all(),
                                               label='Модель управляемого моста')
    factory_num_controlled_bridge = CharField(max_length=255,
                                              empty_value='Без названия',
                                              label='Зав. № управляемого моста')
    contract_num_data = CharField(max_length=255,
                                  empty_value='Без названия',
                                  label='Договор поставки №, дата')
    ship_date = DateTimeField(label='Дата отгрузки с завода',
                              widget=forms.TextInput(attrs={'placeholder': 'формат: дд.мм.гггг'}))
    consignee = CharField(max_length=255,
                          empty_value='Без названия',
                          label='Грузополучатель (конечный потребитель)')
    delivery_address = CharField(max_length=255,
                                 empty_value='Без названия',
                                 label='Адрес поставки (эксплуатации)')
    equipment = CharField(max_length=255,
                          empty_value='Без названия',
                          label='Комплектация (доп. опции)')
    client = ModelChoiceField(queryset=Client.objects.all(),
                              label='Клиент')
    service_company = ModelChoiceField(queryset=ServiceCompany.objects.all(),
                                       label='Сервисная компания')

    class Meta:
        model = Car
        fields = ('factory_num_car',
                  'model_technics',
                  'model_motor',
                  'factory_num_motor',
                  'model_transmissions',
                  'factory_num_transmissions',
                  'model_driving_bridge',
                  'factory_num_driving_bridge',
                  'model_controlled_bridge',
                  'factory_num_controlled_bridge',
                  'contract_num_data',
                  'ship_date',
                  'consignee',
                  'delivery_address',
                  'equipment',
                  'client',
                  'service_company',
                  )


class MaintenanceForm(ModelForm):
    type_maintenance = ModelChoiceField(queryset=TypeMaintenance.objects.all(),
                                        label='Вид ТО')
    data_maintenance = DateTimeField(label='Дата проведения ТО',
                                     widget=forms.TextInput(attrs={'placeholder': 'формат: дд.мм.гггг'}))
    operating_time = CharField(max_length=255,
                               empty_value='Без названия',
                               label='Наработка, м/час')
    num_order = CharField(max_length=255,
                          empty_value='Без названия',
                          label='№ заказ-наряда')
    data_order = DateField(label='Дата заказ-наряда')
    car = ModelChoiceField(queryset=Car.objects.all(),
                           label='Машина')
    service_company = ModelChoiceField(queryset=ServiceCompany.objects.all(),
                                       label='Сервисная компания')

    class Meta:
        model = Maintenance
        fields = (
            'type_maintenance',
            'data_maintenance',
            'operating_time',
            'num_order',
            'data_order',
            'car',
            'service_company',
        )


class ClaimForm(ModelForm):
    data_rejection = DateTimeField(label='Дата заказ-наряда',
                                   widget=forms.TextInput(attrs={'placeholder': 'гггг-мм-дд чч:мм:сс'}))
    operating_time = CharField(max_length=255,
                               empty_value='Без названия',
                               label='Наработка, м/час')
    node_failure = ModelChoiceField(queryset=TypeFault.objects.all(),
                                    label='Узел отказа')
    description_failure = CharField(max_length=255,
                                    empty_value='Без названия',
                                    label='Описание отказа')
    recovery_method = ModelChoiceField(queryset=RecoveryMethod.objects.all(),
                                       label='Способ восстановления')
    spare_parts = CharField(max_length=255,
                            empty_value='Используемые запасные части',
                            label='№ заказ-наряда')
    data_restoration = DateTimeField(label='Дата восстановления',
                                     widget=forms.TextInput(attrs={'placeholder': 'гггг-мм-дд чч:мм:сс'}))
    downtime_technic = CharField(max_length=255,
                                 empty_value='Без названия',
                                 label='Время простоя')
    car = ModelChoiceField(queryset=Car.objects.all(),
                           label='Машина')
    service_company = ModelChoiceField(queryset=ServiceCompany.objects.all(),
                                       label='Сервисная компания')

    class Meta:
        model = Claim
        fields = (
            'data_rejection',
            'operating_time',
            'node_failure',
            'description_failure',
            'recovery_method',
            'spare_parts',
            'data_restoration',
            'downtime_technic',
            'car',
            'service_company',
        )


class ModelTechnicsForm(ModelForm):
    title = CharField(max_length=255,
                               empty_value='Без названия',
                               label='Название')
    description = CharField(max_length=255,
                               empty_value='Без названия',
                               label='Описание',
                               widget=forms.Textarea(),
                            )

    class Meta:
        model = ModelTechnics
        fields = ('title',
                  'description',
        )


class ModelMotorForm(ModelForm):
    title = CharField(max_length=255,
                      empty_value='Без названия',
                      label='Название')
    description = CharField(max_length=255,
                            empty_value='Без названия',
                            label='Описание',
                            widget=forms.Textarea(),
                            )

    class Meta:
        model = ModelMotor
        fields = ('title',
                  'description',
        )


class ModelTransmissionsForm(ModelForm):
    title = CharField(max_length=255,
                      empty_value='Без названия',
                      label='Название')
    description = CharField(max_length=255,
                            empty_value='Без названия',
                            label='Описание',
                            widget=forms.Textarea(),
                            )

    class Meta:
        model = ModelTransmissions
        fields = ('title',
                  'description',
        )


class ModelDrivingBridgeForm(ModelForm):
    title = CharField(max_length=255,
                      empty_value='Без названия',
                      label='Название')
    description = CharField(max_length=255,
                            empty_value='Без названия',
                            label='Описание',
                            widget=forms.Textarea(),
                            )

    class Meta:
        model = ModelDrivingBridge
        fields = ('title',
                  'description',
        )


class ModelControlledBridgeForm(ModelForm):
    title = CharField(max_length=255,
                      empty_value='Без названия',
                      label='Название')
    description = CharField(max_length=255,
                            empty_value='Без названия',
                            label='Описание',
                            widget=forms.Textarea(),
                            )

    class Meta:
        model = ModelControlledBridge
        fields = ('title',
                  'description',
        )


class TypeMaintenanceForm(ModelForm):
    title = CharField(max_length=255,
                      empty_value='Без названия',
                      label='Название')
    description = CharField(max_length=255,
                            empty_value='Без названия',
                            label='Описание',
                            widget=forms.Textarea(),
                            )

    class Meta:
        model = TypeMaintenance
        fields = ('title',
                  'description',
        )


class TypeFaultForm(ModelForm):
    title = CharField(max_length=255,
                      empty_value='Без названия',
                      label='Название')
    description = CharField(max_length=255,
                            empty_value='Без названия',
                            label='Описание',
                            widget=forms.Textarea(),
                            )

    class Meta:
        model = TypeFault
        fields = ('title',
                  'description',
        )


class RecoveryMethodForm(ModelForm):
    title = CharField(max_length=255,
                      empty_value='Без названия',
                      label='Название')
    description = CharField(max_length=255,
                            empty_value='Без названия',
                            label='Описание',
                            widget=forms.Textarea(),
                            )

    class Meta:
        model = RecoveryMethod
        fields = ('title',
                  'description',
        )


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', min_length=5, max_length=150)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name',)



