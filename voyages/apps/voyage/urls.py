from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import RedirectView, TemplateView

import voyages.apps.static_content.views
import voyages.apps.voyage.search_views
import voyages.apps.voyage.views
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect

def redirect_to_blog_maps(_):
    return HttpResponsePermanentRedirect(reverse('blog:tag', args=['intro-maps']))

urlpatterns = [

    # flatpages
    url(r'^about',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^essays',
        TemplateView.as_view(template_name='essays.html'),
        name='essays'),
    url(r'^downloads',
        TemplateView.as_view(template_name='downloads.html'),
        name='downloads'),
    url(r'^maps$', redirect_to_blog_maps, name='maps'),
    url(r'^ship',
        TemplateView.as_view(template_name='ship.html'), name='ship'),
    url(r'^navire', TemplateView.as_view(template_name='navire.html'), name='navire'),
    url(r'^c(?P<chapternum>\w{2})_s(?P<sectionnum>\w{2})_p(?P<pagenum>\w{2})',
        voyages.apps.voyage.views.get_page,
        name='get-page'),
    url(r'^$',
        voyages.apps.static_content.views.get_static_content,
        {'group': 'Voyage'},
        name='index'),

    url(r'^reload-cache',
        voyages.apps.voyage.views.reload_cache,
        name='reload_cache'),
    url(r'^permalink',
        voyages.apps.voyage.views.get_permanent_link,
        name='permanent-link'),
    url(r'^contribute',
        RedirectView.as_view(url='/contribute'),
        name='submission-login'),
    url(r'^(?P<voyage_id>[0-9]+)/variables',
        voyages.apps.voyage.views.voyage_variables,
        name='voyage_variables'),
    url(r'^(?P<voyage_id>[0-9]+)/map',
        voyages.apps.voyage.views.voyage_map,
        name='voyage_map'),
    url(r'^(?P<voyage_id>[0-9]+)/images',
        voyages.apps.voyage.views.voyage_images,
        name='voyage_images'),
    url(r'^csv_stats_download',
        voyages.apps.voyage.views.csv_stats_download,
        name='csv_stats_download'),
    url(r'^database',
        TemplateView.as_view(template_name='database.html'),
        name='database'),
    url(r'var-options',
        voyages.apps.voyage.search_views.get_var_options,
        name='var-options'),
    url(r'filtered-places',
        voyages.apps.voyage.search_views.get_filtered_places,
        name='filtered-places'),
    url(r'save-query',
        voyages.apps.voyage.search_views.save_query,
        name='save-query'),
    url(r'get-saved-query/(?P<query_id>\w+)',
        voyages.apps.voyage.search_views.get_saved_query,
        name='get-saved-query'),
    url(r'^api/search',
        voyages.apps.voyage.search_views.ajax_search,
        name='search'),
    url(r'^api/download',
        voyages.apps.voyage.search_views.ajax_download,
        name='download'),
    url(r'get-all-sources',
        voyages.apps.voyage.search_views.get_all_sources,
        name='all-sources'),
    url(r'get-timelapse-regions',
        voyages.apps.voyage.search_views.get_timelapse_port_regions,
        name='get-timelapse-regions'),
    url(r'get-compiled-routes',
        voyages.apps.voyage.search_views.get_compiled_routes,
        name='get-compiled-routes')
]
