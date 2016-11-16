from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.forms import PostForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError


from .models import Question

# Create your views here.

@login_required
def index(request):
    latest_question_list = Question.objects.order_by('question_text').all()
    if request.method == 'GET':
        form = PostForm
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            count = 0
            questions = Question.objects.values()

            for i in range(len(questions)):
                answer = form.cleaned_data['question{0}'.format((i+1))]
                correct = questions[i]['correct']
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
