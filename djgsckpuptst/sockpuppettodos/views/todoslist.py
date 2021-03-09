from django.views.generic.base import TemplateView


class TodoslistView(TemplateView):
    template_name = 'todoslist.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = 0
        return context
