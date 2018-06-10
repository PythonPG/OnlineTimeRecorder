from django.shortcuts import render, redirect
import django
from .forms import MyForm
#from .models import SyainData

def form_top(request):
   return render(request, 'form_top/form_top.html', {
      'form': form_save,
   }) 

import datetime
def form_user_login_function(request):
   return render(request, 'form_user_login/form_user_login.html', {
       'current_date': (datetime.datetime.today() +  datetime.timedelta(hours=9)).strftime('%Y年%m月%d日')
   })

import datetime 
def form_time_login_function(request):
   return render(request, 'form_time_login/form_time_login.html', {
       'current_date': (datetime.datetime.today() +  datetime.timedelta(hours=9)).strftime('%Y年%m月%d日')
   })

import datetime
def form_user(request):
   return render(request, 'form_user/form_user.html', {
       'current_date': (datetime.datetime.today() +  datetime.timedelta(hours=9)).strftime('%Y年%m月%d日')
   })
   
import datetime
def form_time(request):
   return render(request, 'form_time/form_time.html', {
      'current_date': (datetime.datetime.today() +  datetime.timedelta(hours=9)).strftime('%Y年%m月%d日'),
      'current_time': (datetime.datetime.today() +  datetime.timedelta(hours=9)).strftime('%H:%M')
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
   
