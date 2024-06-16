import public.models as models

def notification_context(request):
    user = request.user
    context_data = dict()
    if user.is_authenticated:
        if user.role == 512:
            notifications = models.AccessRequest.objects.filter(approver_user=user, showed=False).count()
            context_data['notification_count'] = notifications
            return context_data
        else:
            pass
    return context_data