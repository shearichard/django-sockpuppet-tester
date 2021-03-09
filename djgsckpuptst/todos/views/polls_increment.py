from django.views.generic.base import TemplateView


class PollsIncrementView(TemplateView):
    template_name = 'polls_increment.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = 0
        return context

pollsincrement = PollsIncrementView.as_view()
