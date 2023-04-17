

class FilterMixin:
    def get_filter_user(self, fil):
        return fil(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *args, **kwargs):
        context = {** super().get_context_data(*args, **kwargs),
                'filter': self.get_filter(),
                }
        return context
