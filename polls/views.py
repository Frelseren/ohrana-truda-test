from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from polls.forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError


from .models import Question

# Create your views here.

@login_required
def index(request):
    latest_question_list = Question.objects.all()
    if request.method == 'GET':
        form = PostForm
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            count = 0
            questions = Question.objects.values()

            for i in range(1,3):
                answer = form.cleaned_data['question%s' % i]
                correct = questions[i-1]['correct']
                if answer == correct:
                    count += 1
            
            result = count/len(questions)*100

            user = request.user
            subject = 'Test - Ohrana Truda - %s' % user
            from_email = 'ohranatruda@herokuapp.com'
            message = "Itogoviy ball studenta '{0} {1}' sostavlyaet '{2}'%".format(user.first_name, user.last_name, result)

            try:
                send_mail(subject, message, from_email, ['verkhoshintsev@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            return redirect('thanks')
    context = {'latest_question_list': latest_question_list, 'form': form}
    return render(request, 'index.html', context)

def thanks(request):
    logout(request)
    return render(request, 'thanks.html')