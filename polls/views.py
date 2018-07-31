from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
import django
from .forms import MyForm, LoginForm, UserForm, DemoUserForm
from .models import User, DemoUser

def form_top(request):
   return render(request, 'form_top/form_top.html', {
      'form': form_save,
   }) 


class FormUserLogin(FormView):
   """
   ログイン
   """
   template_name = 'form_user_login/form_user_login.html'
   form_class = LoginForm
   
   def form_valid(self, form):
      login(self.request, form.get_user())
      return super().form_valid(form)

   def get_success_url(self):
      if self.request.user.secret:
         return reverse('form_secret')
      elif self.request.user.master:
         return reverse('form_user')
      else:
         return reverse('form_time')

class FormUser(FormView):
   """
   マスター
   """
   template_name = 'form_user/form_user.html'
   form_class = UserForm
   success_url = '.'

   def form_valid(self, form):
      phone = form.cleaned_data['phone']
      password = form.cleaned_data['password']
      name_sei = form.cleaned_data['name_sei']
      name_namae = form.cleaned_data['name_namae']
      User.objects.create_user(phone, password, name_sei, name_namae)
      return super().form_valid(form)

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['user_list'] = User.objects.all().order_by('id')
      return context

def del_user(request):
   id = request.GET.get('id')
   if id:
      User.objects.get(pk=id).delete()
   return JsonResponse({})

class FormSecret(FormView):
   """
   シークレット
   """
   template_name = 'form_secret/form_secret.html'
   form_class = DemoUserForm
   success_url = '.'

   def form_valid(self, form):
      DemoUser.objects.create(**form.cleaned_data)
      return super().form_valid(form)

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['user_list'] = DemoUser.objects.all().order_by('id')
      return context
   

def del_demo_user(request):
   id = request.GET.get('id')
   if id:
      DemoUser.objects.get(pk=id).delete()
   return JsonResponse({})
   
import datetime 
def form_time_login_function(request):
   return render(request, 'form_time_login/form_time_login.html', {
       'current_date': datetime.datetime.today().strftime('%Y年%m月%d日')
   })

import datetime
def form_time(request):
   return render(request, 'form_time/form_time.html', {
      'current_date': datetime.datetime.today().strftime('%Y年%m月%d日'),
      'current_time': datetime.datetime.today().strftime('%H:%M')
   })

def form_user_save(request):
   request_dictonary = dict(request.POST)
   print(request_dictonary) 
   return redirect('form_user')
   
def search(request):
   phone_number = dict(request.GET)['query'][0]
   result_list = []
   # for row in SyainData.objects.filter(phone=phone_number):
   #    result_list.append(row)
   return render(request, 'polls/form.html', {
      'message': u'検索結果は{}件です'.format(len(result_list)),
      'form': MyForm(),
      'search_result': result_list
   })
   
def form_save(request):
   fmrm = MyForm(request.POST)
   if form.is_valid():
      ret_dict = dict(request.POST)
      # syain = SyainData(
      #       phone=ret_dict['phone'][0],
      #       date=ret_dict['date'][0],
      #       password=ret_dict['password'][0],
      #       name=ret_dict['name'][0],
      #       job_start=ret_dict['job_start'][0],
      #       job_end=ret_dict['job_end'][0],
      #       status=ret_dict['status'][0],
      # )
      # syain.save()
      message = u'登録が完了しました'
   else:
      message = u'登録に失敗しました'
   return render(request, 'polls/form.html', {
      'message': message,
      'form': MyForm(),
   }) 
   
   
#   <button type='submit' name='action' value='send'>
   
