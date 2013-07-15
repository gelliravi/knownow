from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from knownow.models import Knowledge



def index(request):
    latest_knowledge_list = Knowledge.objects.all()
    context = {'latest_knowledge_list': latest_knowledge_list}
    return render(request, 'knownow/index.html', context)

def detail(request, knowledge_id):
    aKnowledge = get_object_or_404(Knowledge, pk=knowledge_id)
    try:
        provided_content = request.POST['content']
    except (KeyError, Knowledge.DoesNotExist):
        # Redisplay the knowledge input form.
        return render(request, 'knownow/detail.html', {
            'knowledge': aKnowledge,
            'error_message': "You didn't enter content.",
        })
    else:
        newKnowledge = Knowledge(content=provided_content, referalKnowledge=aKnowledge)
        newKnowledge.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('knownow:detail', args=(newKnowledge.id,)))

def createFromScratch(request):
    try:
        provided_content = request.POST['content']
    except (KeyError, Knowledge.DoesNotExist):
        # Redisplay the knowledge input form.
        return render(request, 'knownow/index.html', {
            'error_message': "You didn't enter content.",
        })
    else:
        newKnowledge = Knowledge(content=provided_content)
        newKnowledge.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('knownow:detail', args=(newKnowledge.id,)))



