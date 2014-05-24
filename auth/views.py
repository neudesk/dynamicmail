from django.contrib.auth import authenticate, login, logout, forms
from django.shortcuts import redirect, HttpResponseRedirect, render_to_response
from django.template import RequestContext

def login_user(request):
    context = {'form': forms.AuthenticationForm()}
    if request.user.is_authenticated():
        redirect('/panel/')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/panel/')
            context['error'] = 'Your account is temporarily unavailable, Please contact admin.'
        else:
            context['error'] = 'Incorrect Username or Password.'
    return render_to_response('auth/login.djhtml', context,
                              context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')