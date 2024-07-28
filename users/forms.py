from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from users.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите ваше имя пользователя'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'form-control',
                                          'placeholder': 'Введите ваш пароль'})
    )

    class Meta:
        model = User
        fields: list[str] = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "role",
            "username",
            "email",
            "telegram",
            "password1",
            "password2",
        )

    role = forms.ChoiceField(
        label='Роль',
        choices=(('1', 'Пользователь'),
                 ('2', 'Мед работник'),
                 ('3', 'Пациент')
                 ),

        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        )
    )

    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    username = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите вашу фамилию",
            }
        )
    )
    telegram = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "https://t.me/user",
            }
        )
    )
    email = forms.CharField(
        label='Почта',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email *youremail@example.com",
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Подтвердите ваш пароль",
            }
        )
    )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "role",
            "first_name",
            "username",
            "email",
            "telegram",
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя",
            }
        )
    )
    role = forms.ChoiceField(
        label='Роль',
        choices=(('1', 'Пользователь'),
                 ('2', 'Мед работник')
                 ),

        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        )
    )
    telegram = forms.CharField(
        label='Телеграм',
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "placeholder": "https://t.me/user",
            }
        )
    )
    username = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            }
        )
    )
    email = forms.CharField(
        label='Почта',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш email youremail@example.com",
            }
        ),
    )