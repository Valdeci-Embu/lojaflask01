from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    firstname = StringField('Nome', [validators.Length(min=4, max=25)])
    lastname = StringField('Sobrenome', [validators.Length(min=4, max=25)])
    username = StringField('Usuário', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirma Senha')
   
    