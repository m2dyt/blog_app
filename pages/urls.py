from django.urls import path
from blog.views import AboutView, RulesView  # Импорт из blog, или перемести в pages.views
app_name = 'pages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('rules/', RulesView.as_view(), name='rules'),
]
