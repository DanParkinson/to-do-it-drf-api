from .models import Task
from datetime import datetime

def filter_tasks_by_priority(queryset, request):
    '''
    filters task by priority
    '''
    priority = request.GET.get('priority')
    VALID_PRIORITIES = ['Low','Medium','High']

    if priority in VALID_PRIORITIES:
        queryset = queryset.filter(priority=priority)
    return queryset

def filter_tasks_by_status(queryset, request):
    '''
    filter tasks by status
    '''
    status = request.GET.get('status')
    STATUS_CHOICES = ['Pedning', 'In Progress', 'Completed', 'Overdue']

    if status in STATUS_CHOICES:
        queryset = queryset.filter(status=status)
    return queryset
