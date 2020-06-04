from django_messages.models import inbox_count_for, Message
from django.conf import settings


def inbox(request):
    if request.user.is_authenticated():
        return {'messages_inbox_count': inbox_count_for(request.user)}
    else:
        return {}


def recent_messages(request):
    if request.user.is_authenticated():
        limit = getattr(settings, 'MESSAGES_RECENT_LIMIT', 10)
        return {
            'messages_recent': Message.objects.inbox_for(request.user)[:limit]
        }
    return {}
