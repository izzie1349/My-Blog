from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView, name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_update'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_delete'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),

    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approval, name='comment_approval'),
    url(r'comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
