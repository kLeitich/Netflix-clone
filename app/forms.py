from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['email'].widget.attrs.update({
        "required":"",
        "name":"username",
        "id":"name",
        "type":"text",
        "placeholder":"Email",
        "class":"form-input"
      })
      self.fields['password1'].widget.attrs.update({
        "required":"",
        "name":"password1",
        "id":"password1",
        "type":"password",
        "placeholder":"Password",
        "class":"form-input"
      })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']