from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from graphsocial.models import Person

def index(request):
    person_list = Person.objects.all()
    context = {'person_list': person_list}
    return render(request, 'graphsocial/index.html', context)

def createFromScratch(request):
    try:
        provided_name = request.POST['name']
    except (KeyError, Person.DoesNotExist):
        # Redisplay the knowledge input form.
        return render(request, 'graphsocial/index.html', {
            'error_message': "You didn't enter a name.",
        })
    else:
        newPerson = Person(name=provided_name)
        newPerson.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('graphsocial:index'))

