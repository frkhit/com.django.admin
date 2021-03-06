# -*- coding:utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django import forms
from django.contrib.auth.models import User
from django.forms.utils import ErrorList

from poll.models import Author


class AuthorForm(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(), min_length=3, max_length=20, label="用户名")
    password = forms.CharField(widget=forms.PasswordInput(), label="密码")
    password1 = forms.CharField(widget=forms.PasswordInput(), label="确认密码")

    class Meta:
        model = Author
        fields = "__all__"
        exclude = ("user",)

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, instance=None, use_required_attribute=None):
        if instance is not None and initial is None:
            initial = {"user_name": instance.user.username,
                       "password": instance.user.password,
                       "password1": instance.user.password}

        super(AuthorForm, self).__init__(data=data, files=files, auto_id=auto_id, prefix=prefix,
                                         initial=initial, error_class=error_class, label_suffix=label_suffix,
                                         empty_permitted=empty_permitted, instance=instance,
                                         use_required_attribute=use_required_attribute)

    def save(self, commit=True):
        return super(AuthorForm, self).save(commit=commit)

    def clean(self):
        result = super(AuthorForm, self).clean()
        user_name = result.get("user_name")
        password = result.get("password")
        password1 = result.get("password1")
        user = User.objects.filter(username=user_name).first()
        if user is None:
            assert password == password1
            user = User(username=user_name, password=password)
            user.save()
        else:
            assert user.password == password
        self.instance.user = user
        return result

    def is_valid(self):
        return super(AuthorForm, self).is_valid()
