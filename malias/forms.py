from django import forms
from .models import Category, Delivery, Customer, Contact, Country, City, District, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control contact__section-input'
    }))


class RegisterForm(UserCreationForm):
    username = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name')


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ('phone', 'country', 'city', 'district', 'street', 'home', 'flat', 'comment', 'delivery_method',
                  'payment_method')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control contact__section-input'}),
            'country': forms.Select(attrs={'class': 'form-control contact__section-input'}),
            'city': forms.Select(attrs={'class': 'form-control contact__section-input'}),
            'district': forms.Select(attrs={'class': 'form-control contact__section-input'}),
            'street': forms.TextInput(attrs={'class': 'form-control contact__section-input'}),
            'home': forms.TextInput(attrs={'class': 'form-control contact__section-input'}),
            'flat': forms.TextInput(attrs={'class': 'form-control contact__section-input'}),
            'comment': forms.Textarea(attrs={'class': 'form-control contact__section-input'}),
            'payment_method': forms.RadioSelect(attrs={'class': 'contact__section-radio'}),
            'delivery_method': forms.RadioSelect(attrs={'class': 'contact__section-radio'})
        }


class EditUserForm(forms.ModelForm):
    username = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    old_password = forms.CharField(required=False, min_length=8, label='Старый пароль',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control contact__section-input'}))

    new_password = forms.CharField(required=False, min_length=8, label='Новый пароль',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control contact__section-input'}))

    confirm_password = forms.CharField(required=False, min_length=8, label='Подтвердите пароль',
                                       widget=forms.PasswordInput(attrs={'class': 'form-control contact__section-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'old_password', 'new_password', 'confirm_password')


class EditCustomerForm(forms.ModelForm):
    phone = forms.CharField(required=False, label=False, widget=forms.TelInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    country = forms.ModelChoiceField(required=False, queryset=Country.objects.all(), label=False,
                                     widget=forms.Select(attrs={
                                         'class': 'form-control contact__section-input'
                                     }))

    city = forms.ModelChoiceField(required=False, queryset=City.objects.all(), label=False, widget=forms.Select(attrs={
        'class': 'form-control contact__section-input'
    }))

    district = forms.ModelChoiceField(required=False, queryset=District.objects.all(), label=False,
                                      widget=forms.Select(attrs={
                                          'class': 'form-control contact__section-input'
                                      }))

    street = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    house = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    flat = forms.CharField(required=False, label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    class Meta:
        model = Customer
        fields = ['phone', 'country', 'city', 'district', 'street', 'house', 'flat']


class ContactForm(forms.ModelForm):
    name = forms.CharField(label=False, widget=forms.TextInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    phone = forms.CharField(label=False, widget=forms.TelInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    email = forms.EmailField(label=False, widget=forms.EmailInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    text = forms.CharField(required=False, label=False, widget=forms.Textarea(attrs={
        'class': 'form-control contact__section-input'
    }))

    file = forms.FileField(required=False, label='Attach file', widget=forms.FileInput(attrs={
        'class': 'form-control contact__section-input'
    }))

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'text', 'file')


class CommentForm(forms.ModelForm):
    text = forms.CharField(label='Leave a comment', widget=forms.Textarea(attrs={
        'class': 'form-control contact__section-input',
        'style': 'height: 100px; width: 600px; background-color: rgb(217 217 217) !important;'
    }))

    def clean_text(self):
        data = self.cleaned_data['text']
        if len(data) > 500:
            raise forms.ValidationError("Comment cannot exceed 500 characters !!!")
        return data

    class Meta:
        model = Comment
        fields = ('text',)
