from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AdminPasswordChangeForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.conf import settings
from django.views.generic import (ListView,
                                  UpdateView,
                                  CreateView,
                                  DetailView,
                                  DeleteView, FormView, )
from django.contrib.auth.views import LoginView, PasswordChangeView

from .forms import LoginUserForm, CarForm, MaintenanceForm, ClaimForm, ModelTechnicsForm, ModelMotorForm, \
    ModelTransmissionsForm, ModelDrivingBridgeForm, ModelControlledBridgeForm, TypeMaintenanceForm, TypeFaultForm, \
    RecoveryMethodForm, CustomUserCreationForm
from .models import Car, Claim, Maintenance, ModelTechnics, ModelMotor, References, ModelTransmissions, \
    ModelDrivingBridge, ModelControlledBridge, TypeMaintenance, TypeFault, RecoveryMethod
from .filters import (CarFilter,
                      MaintenanceFilter,
                      AllFilter,
                      ClaimFilter)
from .utils import FilterMixin


# view car -----------------------------------------------------------------
class CarList(ListView):
    model = Car
    template_name = 'polls/car/search_car.html'
    ordering = 'ship_date'
    context_object_name = 'cars'


class SearchCar(PermissionRequiredMixin, FilterMixin, CarList):
    permission_required = 'polls.view_car'

    def get_filter(self):
        return self.get_filter_user(CarFilter)


class SearchAllBlank(FilterMixin, CarList):
    template_name = 'polls/car_all_blank.html'

    def get_filter(self):
        return self.get_filter_user(AllFilter)


class SearchAll(FilterMixin, CarList):
    template_name = 'polls/car_all.html'

    def get_filter(self):
        return self.get_filter_user(AllFilter)


class CarDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'polls.view_car'
    model = Car
    template_name = 'polls/car/car_detail.html'
    context_object_name = 'car_detail'


class CarCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.add_car'
    template_name = 'polls/car/car_create.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy('search_car')


class CarUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.change_car'
    template_name = 'polls/car/car_create.html'
    form_class = CarForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Car.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('search_car')


class CarDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.delete_car'
    template_name = 'polls/car/car_delete.html'
    queryset = Car.objects.all()
    context_object_name = 'car_one'

    def get_success_url(self):
        return reverse_lazy('search_car')
# end view car ------------------------------------------------------------------------


# view maintenance -------------------------------------------------------------------
class MaintenanceList(PermissionRequiredMixin, ListView):
    permission_required = 'polls.view_maintenance'
    model = Maintenance
    template_name = 'polls/maintenance/maintenance.html'
    ordering = 'data_maintenance'
    context_object_name = 'maintenance'


class MaintenanceCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/maintenance/maintenance_create.html'
    form_class = MaintenanceForm
    permission_required = 'polls.add_maintenance'

    def get_success_url(self):
        return reverse_lazy('maintenance')


class MaintenanceUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/maintenance/maintenance_create.html'
    form_class = MaintenanceForm
    permission_required = 'polls.change_maintenance'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Maintenance.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('maintenance')


class MaintenanceDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/maintenance/maintenance_delete.html'
    queryset = Maintenance.objects.all()
    context_object_name = 'maintenance_one'
    permission_required = 'polls.delete_maintenance'

    def get_success_url(self):
        return reverse_lazy('maintenance')


class SearchMaintenance(FilterMixin, MaintenanceList):

    def get_filter(self):
        return self.get_filter_user(MaintenanceFilter)


class MaintenanceDetail(PermissionRequiredMixin, DetailView):
    model = Maintenance
    template_name = "polls/maintenance/maintenance_detail.html"
    context_object_name = "maintenance_one"
    permission_required = 'polls.view_maintenance'
# end view maintenance -------------------------------------------------------------------


# view claim -------------------------------------------------------------------
class ClaimList(PermissionRequiredMixin, ListView):
    model = Claim
    template_name = 'polls/claim/claim.html'
    ordering = 'data_rejection'
    context_object_name = 'claims'
    permission_required = 'polls.view_claim'


class SearchClaim(FilterMixin, ClaimList):

    def get_filter(self):
        return self.get_filter_user(ClaimFilter)


class ClaimDetail(PermissionRequiredMixin, DetailView):
    model = Claim
    template_name = "polls/claim/claim_detail.html"
    context_object_name = "claim_one"
    permission_required = 'polls.view_claim'


class ClaimCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/claim/claim_create.html'
    form_class = ClaimForm
    permission_required = 'polls.add_claim'

    def get_success_url(self):
        return reverse_lazy('claim')


class ClaimUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/claim/claim_create.html'
    form_class = ClaimForm
    permission_required = 'polls.change_claim'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Claim.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('claim')


class ClaimDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/claim/claim_delete.html'
    queryset = Claim.objects.all()
    context_object_name = 'claim_one'
    permission_required = 'polls.delete_claim'

    def get_success_url(self):
        return reverse_lazy('claim')
# end view claim -------------------------------------------------------------------


'''
    REFERENCES 
'''


class ReferencesList(PermissionRequiredMixin, ListView):
    model = References
    template_name = 'polls/references.html'
    context_object_name = 'refs'
    permission_required = 'polls.view_references'


# view model_technics -------------------------------------------------------------------
class ModelTechnicsList(PermissionRequiredMixin, ListView):
    model = ModelTechnics
    template_name = 'polls/model_technics/model_technics.html'
    ordering = 'pk'
    paginate_by = 5
    permission_required = 'polls.view_modeltechnics'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модели техники'
        return context


class ModelTechnicsDetail(PermissionRequiredMixin, DetailView):
    model = ModelTechnics
    template_name = "polls/model_technics/model_technics_detail.html"
    context_object_name = "model_technics_one"
    permission_required = 'polls.view_modeltechnics'


class ModelTechnicsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/model_technics/model_technics_create.html'
    form_class = ModelTechnicsForm
    permission_required = 'polls.add_modeltechnics'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модель техники'
        return context

    def get_success_url(self):
        return reverse_lazy('model_technics')


class ModelTechnicsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/model_technics/model_technics_create.html'
    form_class = ModelTechnicsForm
    permission_required = 'polls.change_modeltechnics'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'модель техники'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ModelTechnics.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('model_technics')


class ModelTechnicsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/model_technics/model_technics_delete.html'
    queryset = ModelTechnics.objects.all()
    permission_required = 'polls.delete_modeltechnics'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модель техники'
        return context

    def get_success_url(self):
        return reverse_lazy('model_technics')
# end view model_technics -------------------------------------------------------------------


# view model_motor -------------------------------------------------------------------
class ModelMotorList(PermissionRequiredMixin, ListView):
    model = ModelMotor
    template_name = 'polls/model_motor/model_motor.html'
    ordering = '-pk'
    paginate_by = 5
    permission_required = 'polls.view_modelmotor'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модели двигателя'
        return context


class ModelMotorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/model_motor/model_motor_create.html'
    form_class = ModelMotorForm
    permission_required = 'polls.add_modelmotor'

    def get_success_url(self):
        return reverse_lazy('model_motor')
    # permission_required = ('car.add_car')


class ModelMotorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/model_motor/model_motor_create.html'
    form_class = ModelMotorForm
    permission_required = 'polls.change_modelmotor'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'модель двигателя'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ModelMotor.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('model_motor')


class ModelMotorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/model_motor/model_motor_delete.html'
    queryset = ModelMotor.objects.all()
    permission_required = 'polls.delete_modelmotor'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модель двигателя'
        return context

    def get_success_url(self):
        return reverse_lazy('model_motor')
# end view model_motor -------------------------------------------------------------------


# view model_transmissions -------------------------------------------------------------------
class ModelTransmissionsList(PermissionRequiredMixin, ListView):
    model = ModelTransmissions
    template_name = 'polls/model_transmissions/model_transmissions.html'
    ordering = '-pk'
    paginate_by = 5
    permission_required = 'polls.view_modeltransmissions'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модели трансмиссии'
        return context


class ModelTransmissionsCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/model_transmissions/model_transmissions_create.html'
    form_class = ModelTransmissionsForm
    permission_required = 'polls.add_modeltransmissions'

    def get_success_url(self):
        return reverse_lazy('model_transmissions')


class ModelTransmissionsUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/model_transmissions/model_transmissions_create.html'
    form_class = ModelTransmissionsForm
    permission_required = 'polls.change_modeltransmissions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'модель трансмиссии'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ModelTransmissions.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('model_transmissions')


class ModelTransmissionsDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/model_transmissions/model_transmissions_delete.html'
    queryset = ModelTransmissions.objects.all()
    permission_required = 'polls.delete_modeltransmissions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модель трансмиссии'
        return context

    def get_success_url(self):
        return reverse_lazy('model_transmissions')
# end view model_transmissions -------------------------------------------------------------------


# view model_driving_bridge -------------------------------------------------------------------
class ModelDrivingBridgeList(PermissionRequiredMixin, ListView):
    model = ModelDrivingBridge
    template_name = 'polls/model_driving_bridge/model_driving_bridge.html'
    ordering = '-pk'
    paginate_by = 5
    permission_required = 'polls.view_modeldrivingbridge'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модели ведущего моста'
        return context


class ModelDrivingBridgeCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/model_driving_bridge/model_driving_bridge_create.html'
    form_class = ModelDrivingBridgeForm
    permission_required = 'polls.add_modeldrivingbridge'

    def get_success_url(self):
        return reverse_lazy('model_driving_bridge')


class ModelDrivingBridgeUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/model_driving_bridge/model_driving_bridge_create.html'
    form_class = ModelDrivingBridgeForm
    permission_required = 'polls.change_modeldrivingbridge'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'модель ведущего моста'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ModelDrivingBridge.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('model_driving_bridge')


class ModelDrivingBridgeDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/model_driving_bridge/model_driving_bridge_delete.html'
    queryset = ModelDrivingBridge.objects.all()
    permission_required = 'polls.delete_modeldrivingbridge'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модель ведущего моста'
        return context

    def get_success_url(self):
        return reverse_lazy('model_driving_bridge')
# end view model_driving_bridge -------------------------------------------------------------------


# view model_controlled_bridge -------------------------------------------------------------------
class ModelControlledBridgeList(PermissionRequiredMixin, ListView):
    model = ModelControlledBridge
    template_name = 'polls/model_controlled_bridge/model_controlled_bridge.html'
    ordering = '-pk'
    paginate_by = 5
    permission_required = 'polls.view_modelcontrolledbridge'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модели управляемого моста'
        return context


class ModelControlledBridgeCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/model_controlled_bridge/model_controlled_bridge_create.html'
    form_class = ModelControlledBridgeForm
    permission_required = 'polls.add_modelcontrolledbridge'

    def get_success_url(self):
        return reverse_lazy('model_controlled_bridge')
    # permission_required = ('car.add_car')


class ModelControlledBridgeUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/model_controlled_bridge/model_controlled_bridge_create.html'
    form_class = ModelControlledBridgeForm
    permission_required = 'polls.change_modelcontrolledbridge'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'модель управляемого моста'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return ModelControlledBridge.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('model_controlled_bridge')


class ModelControlledBridgeDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/model_controlled_bridge/model_controlled_bridge_delete.html'
    queryset = ModelControlledBridge.objects.all()
    permission_required = 'polls.delete_modelcontrolledbridge'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'модель управляемого моста'
        return context

    def get_success_url(self):
        return reverse_lazy('model_controlled_bridge')
# end view  model_controlled_bridge-------------------------------------------------------------------


# view type_maintenance -------------------------------------------------------------------
class TypeMaintenanceList(PermissionRequiredMixin, ListView):
    model = TypeMaintenance
    template_name = 'polls/type_maintenance/type_maintenance.html'
    ordering = '-pk'
    paginate_by = 5
    permission_required = 'polls.view_typemaintenance'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ТО'
        return context


class TypeMaintenanceCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/type_maintenance/type_maintenance_create.html'
    form_class = TypeMaintenanceForm
    permission_required = 'polls.add_typemaintenance'

    def get_success_url(self):
        return reverse_lazy('type_maintenance')


class TypeMaintenanceUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/type_maintenance/type_maintenance_create.html'
    form_class = TypeMaintenanceForm
    permission_required = 'polls.change_typemaintenance'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'ТО'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return TypeMaintenance.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('type_maintenance')


class TypeMaintenanceDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/type_maintenance/type_maintenance_delete.html'
    queryset = TypeMaintenance.objects.all()
    permission_required = 'polls.delete_typemaintenance'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ТО'
        return context

    def get_success_url(self):
        return reverse_lazy('type_maintenance')
# end view type_maintenance -------------------------------------------------------------------


# view type_fault -------------------------------------------------------------------
class TypeFaultList(PermissionRequiredMixin, ListView):
    model = TypeFault
    template_name = 'polls/type_fault/type_fault.html'
    ordering = '-pk'
    paginate_by = 5
    permission_required = 'polls.view_typefault'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'характер отказа'
        return context


class TypeFaultCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/type_fault/type_fault_create.html'
    form_class = TypeFaultForm
    permission_required = 'polls.add_typefault'

    def get_success_url(self):
        return reverse_lazy('type_fault')


class TypeFaultUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/type_fault/type_fault_create.html'
    form_class = TypeFaultForm
    permission_required = 'polls.change_typefault'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'характер отказа'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return TypeFault.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('type_fault')


class TypeFaultDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/type_fault/type_fault_delete.html'
    queryset = TypeFault.objects.all()
    permission_required = 'polls.delete_typefault'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'характер отказа'
        return context

    def get_success_url(self):
        return reverse_lazy('type_fault')
# end view type_fault -------------------------------------------------------------------


# view recovery_method -------------------------------------------------------------------
class RecoveryMethodList(PermissionRequiredMixin, ListView):
    model = RecoveryMethod
    template_name = 'polls/recovery_method/recovery_method.html'
    ordering = '-pk'
    paginate_by = 10
    permission_required = 'polls.view_recoverymethod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'способы восстановления'
        return context


class RecoveryMethodCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/recovery_method/recovery_method_create.html'
    form_class = RecoveryMethodForm
    permission_required = 'polls.add_recoverymethod'

    def get_success_url(self):
        return reverse_lazy('recovery_method')


class RecoveryMethodUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'polls/recovery_method/recovery_method_create.html'
    form_class = RecoveryMethodForm
    permission_required = 'polls.change_recoverymethod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        context['name'] = 'способ восстановления'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return RecoveryMethod.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('recovery_method')


class RecoveryMethodDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'polls/recovery_method/recovery_method_delete.html'
    queryset = RecoveryMethod.objects.all()
    permission_required = 'polls.delete_recoverymethod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'способ восстановления'
        return context

    def get_success_url(self):
        return reverse_lazy('recovery_method')
# end view recovery_method -------------------------------------------------------------------


class UserView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'polls/user/user.html'
    permission_required = 'auth.view_user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'пользователей'
        return context


class UserCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'polls/user/user_create.html'
    form_class = CustomUserCreationForm
    permission_required = 'auth.add_user'

    def get_success_url(self):
        return reverse_lazy('user_list')


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.change_user'
    template_name = 'polls/user/user_create.html'
    form_class = UserChangeForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'true'
        return context

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return User.objects.get(pk=id)

    def get_success_url(self):
        return reverse_lazy('user_list')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'polls/user/password.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'polls/login.html'

    def get_success_url(self):
        return reverse_lazy('search_car')


def logout_user(request):
    logout(request)
    return redirect('car_all_blank')
