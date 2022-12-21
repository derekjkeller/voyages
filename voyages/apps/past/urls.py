from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

import voyages.apps.static_content.views

urlpatterns = [
    url(r'^api/search_enslaved',
        voyages.apps.past.views.search_enslaved, name='search_enslaved'),
    url(r'^api/search_enslaver',
        voyages.apps.past.views.search_enslaver, name='search_enslaver'),
    url(r'^api/modern-countries',
        voyages.apps.past.views.get_modern_countries,
        name='modern-countries'),
    url(r'^api/language-groups',
        voyages.apps.past.views.get_language_groups,
        name='language-groups'),
    url(r'^database/(?P<dataset>[\w\-]+)',
        voyages.apps.past.views.enslaved_database,
        name='database'),
    url(r'^database',
        voyages.apps.past.views.enslaved_database,
        name='database'),
    url(r'^enslavement_relation/(?P<relation_pk>[\w\-]+)$',
        voyages.apps.past.views.get_enslavement_relation_info,
        name='enslavement_relation'),
    url(r'refresh_maps_cache',
        voyages.apps.past.views.refresh_maps_cache
        ),
    url(r'^enslavers_contribute/new$',
        voyages.apps.past.views.enslaver_contrib_new,
        name='enslaver_contribute_new'),
    url(r'^enslavers_contribute/delete/(?P<id>.*)',
        voyages.apps.past.views.enslaver_contrib_delete,
        name='enslaver_contribute_delete'),
    url(r'^enslavers_contribute/edit/(?P<id>.*)',
        voyages.apps.past.views.enslaver_contrib_edit,
        name='enslaver_contribute_edit'),
    url(r'^enslavers_contribute/split/(?P<id>.*)',
        voyages.apps.past.views.enslaver_contrib_split,
        name='enslaver_contribute_split'),
    url(r'^enslavers_contribute/merge/(?P<merge_a>.*)/(?P<merge_b>.*)',
        voyages.apps.past.views.enslaver_contrib_merge,
        name='enslaver_contribute_merge'),
     url(r'^enslavers$',
        TemplateView.as_view(template_name='past/enslavers.html'),
        name='enslavers'),
    url(r'^contribute/(?P<id>.*)',
        TemplateView.as_view(template_name='past/contribute.html'),
        name='contribute'),
    url(r'^enslaved_contribution',
        voyages.apps.past.views.enslaved_contribution),
    url(r'^store-audio/(?P<contrib_pk>[0-9]+)/'
        r'(?P<name_pk>[0-9]+)/(?P<token>.*)',
        voyages.apps.past.views.store_audio),
    url(r'enslaved-filtered-places',
        voyages.apps.past.views.get_enslaved_filtered_places,
        name='enslaved-filtered-places'),
    url(r'enslaver-filtered-places',
        voyages.apps.past.views.get_enslaver_filtered_places,
        name='enslaver-filtered-places'),
    url(r'get-enum/(enslaver-role)s',
        voyages.apps.past.views.get_enumeration,
        name='enslaver-roles-enum'),
    url(r'get-enum/(enslavement-relation-type)s',
        voyages.apps.past.views.get_enumeration,
        name='enslaver-roles-enum'),
]

# Remove any null URLs produced by disabled feature flags.
urlpatterns = [u for u in urlpatterns if u is not None]