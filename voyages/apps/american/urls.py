from django.conf.urls import url
from django.views.generic import TemplateView

import voyages.apps.static_content.views

urlpatterns = [
    # url(r'^$', voyages.apps.static_content.views.get_static_content, {'group': 'About'}, name='index'),
    # url(r'^$', TemplateView.as_view(template_name='american/about.html'), name='about'),
    url(r'^about', TemplateView.as_view(template_name='american/about.html'), name='about'),
    url(r'^essays', TemplateView.as_view(template_name='american/essays.html'), name='essays'),
    url(r'^downloads', TemplateView.as_view(template_name='american/downloads.html'), name='downloads'),
    url(r'^database', TemplateView.as_view(template_name='american/database.html'), name='database')]
