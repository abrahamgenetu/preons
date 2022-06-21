from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TutorialSeries, TutorialCategory, Tutorial


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CategoryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TutorialCategory
        fields = ( 'category_summary', 'tutorial_category',)


class SeriesForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=TutorialCategory.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(SeriesForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = TutorialCategory.objects.all()

    class Meta:
        model = TutorialSeries
        fields = ( 'tutorial_series','series_summary','tutorial_category',)


class TutorForm(forms.ModelForm):
    series = forms.ModelChoiceField(queryset=TutorialSeries.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TutorForm, self).__init__(*args, **kwargs)
        self.fields['series'].queryset = TutorialSeries.objects.all()

    class Meta:
        model = Tutorial
        fields = ('title', 'content_first', 'content_second', 'content_third', 'tutorial_series', 'tutorial_image')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', ]
