from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from event_management_system_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_events, name='category_events'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('event-chart/', views.event_chart, name='event_chart'),
    path('get-events/', views.get_events, name='get_events'),
    # path('profile/', views.profile, name='profile'),  # Uncomment and add profile view if it exists
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
