# from flask_wtf import FlaskForm
# from wtforms import StringField,SubmitField,PasswordField
# from wtforms.validators import DataRequired,Email,EqualTo
# from wtforms import ValidationError
# from flask_wtf.file import FileField, FileAllowed
# from flask_login import current_user 
# from Company.models import User
# from Company import db

# class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     password = PasswordField('Password',validators=[DataRequired()])
#     submit=SubmitField('Log In')

# class RegistrationForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match')])
#     pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
#     submit = SubmitField('Register')

#     def check_email(self,field):
#         if db.session.query(User).filter_by(email=field.data).first():
#             raise ValidationError('Your Email has been registered already!')
    
#     def check_username(self,field):
#         if db.session.query(User).filter_by(username=field.data).first():
#             raise ValidationError('Your Username has been registered already!')
        
# class UpdateUserForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired(),Email()])
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png','jpeg','JPG', 'PNG', 'JPEG'])])
#     submit = SubmitField('Update')

#     def check_email(self,field):
#         if db.session.query(User).filter_by(email=field.data).first():
#             raise ValidationError('Your Email has been registered already!')

#################################### CORRECTED CODE ################################################

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from  Company.models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
