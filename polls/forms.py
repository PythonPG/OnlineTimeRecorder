from django import forms
from django.contrib.auth.forms import AuthenticationForm
import datetime
time_difference = datetime.timedelta(hours=9)

from .models import User, DemoUser

class NameField(forms.CharField):
    def is_zenkaku(self, input_data):
        if input_data != '石塚':
            return False
            
        return True

    @staticmethod 
    def parse_input(input_data):
        return input_data.strip()

    def clean(self, input_data):
        if self.is_zenkaku(input_data):
            cleaned_data = NameField.parse_input(input_data)
            return cleaned_data
        else:
             raise forms.ValidationError('名前が石塚ではありません')
   
class MyForm(forms.Form):
    current_time = datetime.datetime.now() + time_difference
    
    phone = forms.CharField(label=u'電話番号')
    date = forms.DateField(
        label=u'日付',
        input_formats=['%Y-%m-%d'],
        initial=datetime.date.today())
    password = forms.CharField(label=u'パスワード')
    name = NameField(label=u'氏名')
    job_start = forms.TimeField(
        label=u'出勤時間',
        input_formats=['%H:%M'],
        initial=current_time.strftime('%H:%M'))
    job_end = forms.TimeField(
        label=u'退社時間',
        input_formats=['%H:%M'],
        initial=current_time.strftime('%H:%M'))
    status = forms.CharField(label=u'状態')
  
class LoginForm(AuthenticationForm):
    """
    ログインフォーム
    """
    
class UserForm(forms.Form):
    phone = forms.CharField(label='電話番号', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    password = forms.CharField(label='パスワード', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name_sei = forms.CharField(label='性', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name_namae = forms.CharField(label='名', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        user_choices = [(0, ''),]
        default_user_list = {'1111111111': '鈴木太郎', '2222222222': '山下一郎', '3333333333': '山田花子'}
        phone_in_list = [k for k, v in default_user_list.items()]
        exist_user_list = User.objects.filter(phone__in=phone_in_list).values_list('phone', flat=True)
        for k, v in default_user_list.items():
            if k not in exist_user_list:
                user_choices.append((k, v))
        
        self.fields['user_choice'] = forms.ChoiceField(choices=user_choices)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError('Already exists phone.')
        return phone

class DemoUserForm(forms.Form):
    phone = forms.CharField(label='電話番号')
    password = forms.CharField(label='パスワード')
    name_sei = forms.CharField(label='性')
    name_namae = forms.CharField(label='名')
