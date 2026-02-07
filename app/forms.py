# Form definitions for Hotel Management System

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField, TimeField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from app.models import Team, Room

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=50)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=120)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class RoomForm(FlaskForm):
    name = StringField('Room Name', validators=[InputRequired(), Length(max=100)])
    capacity = IntegerField('Capacity', validators=[InputRequired()])
    equipment = StringField('Equipment', validators=[Length(max=200)])
    submit = SubmitField('Submit')

class MeetingForm(FlaskForm):
    title = StringField('Meeting Title', validators=[InputRequired(), Length(max=200)])
    date = DateField('Date', validators=[InputRequired()])
    start_time = TimeField('Start Time', validators=[InputRequired()])
    end_time = TimeField('End Time', validators=[InputRequired()])
    description = TextAreaField('Description')
    room = SelectField('Room', coerce=int, validators=[InputRequired()])
    team = SelectField('Team', coerce=int, validators=[InputRequired()])
    submit = SubmitField('Submit')
    
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        self.room.choices = [(room.id, room.name) for room in Room.query.all()]
        self.team.choices = [(team.id, team.name) for team in Team.query.all()]

class TeamForm(FlaskForm):
    name = StringField('Team Name', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')