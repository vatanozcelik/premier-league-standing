from core.models import League


def context_pro(request):
    leagues = League.objects.all()
    context = {
        'leagues': leagues
    }
    return context
