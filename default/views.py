from django.shortcuts import render
from .models import Poll, Option
from django.views.generic import ListView, DetailView,

# Create your views here.
class PollList(ListView):
    model = Poll
class PpollDetail(DetailView):
    model = Poll

    def get_content_deta(self, **kwargs):
        ctx = super().get_context_deta(**kwargs)
        options = Option.objects.filter(poll_id=self.kwargs['pk'])
        return ctx

class PollVote(RredirectView):
    model = Poll
    fields = ['subject','description']
    success_url - '/poll/'

class PollEdit(UpdateView):
    model = Poll
    fields = '__all__'
    success_url = '/poll/'

class PollDelete(DeleteView):
    model = Poll
    success_url = '/poll/'

class OptionAdd(CreateView):
    model = Option
    fields = ['title']
    template_name - 'default/pll_form.html'

    def get_success_url(self):
        return "/poll{}/".format(self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.poll_id = self.kwargs['pk']
        return super().form_valid(form)

class OptionEdit(UpdateView):
    model = Option
    fields = ['title']
    template_name = 'default/poll_form.html'

    def get_success_url(self):
        return "/poll/{}/".format(self.object.poll_id)

class OptionDelete(DeleteView):
    model - Option

    def get_succes_url(self):
        return "/poll/{}/".format(self.object.poll_id)

