from django.conf.urls import url
from API import views

# thanks to
# https://stackoverflow.com/questions/43304923/typeerror-at-admin-set-object-is-not-reversible-and-argument-to-reverse-m?noredirect=1&lq=1
urlpatterns = [
    url(r'^contributions$', views.all_contributions, name='All Contributions'),
    url(r'^projects/tag$', views.projects_with_tag, name='All Projects'),
    url(r'^contribution$', views.contribution, name='One Contribution'),
    url(r'^projects$', views.all_projects, name='All Projects'),
    url(r'^project$', views.project, name='One Project'),
    url(r'^tags$', views.all_tags, name='All Tags'),
    url(r'^tag$', views.tag, name='One Tag'),
]
