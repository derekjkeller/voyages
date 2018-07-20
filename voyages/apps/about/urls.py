from django.conf.urls import url
from django.views.generic import TemplateView

import voyages.apps.static_content.views
import voyages.apps.about.views

urlpatterns = [
    url(r'^$', voyages.apps.static_content.views.get_static_content, {'group': 'About'}, name='index'),
    url(r'^history', TemplateView.as_view(template_name='about/history.html'), name='history'),
    url(r'^team', TemplateView.as_view(template_name='about/team.html'), name='team'),
    url(r'^data', TemplateView.as_view(template_name='about/data.html'), name='data'),
    url(r'^faq', TemplateView.as_view(template_name='about/faq.html'), name='faq'),
    url(r'^glossary', TemplateView.as_view(template_name='about/glossary.html'), name='glossary'),
    url(r'^legal', TemplateView.as_view(template_name='about/legal.html'), name='legal'),

    url(r'^acknowledgements',
        TemplateView.as_view(template_name='about/acknowledgements.html'), name='acknowledgements'),
    url(r'^origins', TemplateView.as_view(template_name='about/origins.html'), name='origins'),
    url(r'^contacts', TemplateView.as_view(template_name='about/contacts.html'), name='contacts'),
    url(r'^flatpage/index', voyages.apps.about.views.render_about_flatpage, {'flatpage_url': '/about/index/'}),
    url(r'^flatpage/history', voyages.apps.about.views.render_about_flatpage, {'flatpage_url': '/about/history/'}),
    url(r'^flatpage/team', voyages.apps.about.views.render_about_flatpage, {'flatpage_url': '/about/team/'}),
]
