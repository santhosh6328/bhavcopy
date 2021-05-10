from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import all_data

urlpatterns = {
    path('', all_data, name="items"),
}
urlpatterns = format_suffix_patterns(urlpatterns)
