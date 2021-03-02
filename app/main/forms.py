from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Say something about you?', validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    pitch = TextAreaField('Pitch')
    category = SelectField('Pitch Category', choices =[
        ('pickup lines','pickup lines'),
        ('Elevator Pitch', 'Elevator Pitch'),
        ('Tech Quotes', 'Tech Quotes'),
        ('Playlists', 'Playlist'),
        ('Extensions', 'Extensions'),
        ('Trends', 'Trends')
        ])
    submit = SubmitField('Add pitch')

class CommentForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Add comment')