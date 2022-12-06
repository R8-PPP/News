from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post


class Class_out_news_list (ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news_list.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = "Next news on Wednesday!"
        return context


class Class_out_news_detail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'