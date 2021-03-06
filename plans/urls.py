from django.urls import path
from .views import list_plans, plan_details, section_details, activity_details

app_name = 'plans'

urlpatterns = [
    path('', list_plans, name='plans-list'),
    path('<slug>/', plan_details, name='plan-details'),
    path('<plan_slug>/<int:section_number>', section_details, name='section-details'),
    path('<plan_slug>/<int:section_number>/<int:activity_number>/', activity_details, name='activity-details'),
]