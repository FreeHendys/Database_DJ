"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import InputRequired, ValidationError
from flask_wtf import FlaskForm


class Length(object):
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        if not message:
            message = 'Field must be between %i and %i characters long.' % (
                min, max)
        self.message = message

    def __call__(self, form, field):
        l = field.data and len(field.data) or 0
        if l < self.min or self.max != -1 and l > self.max:
            raise ValidationError(self.message)


length = Length


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    title = StringField("Title",
                        validators=[InputRequired()])
    description = StringField("Description",
                              validators={length(
                                  max=150,
                                  message="Field must be less than 150 characters")})


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("Title",
                        validators=[InputRequired()])
    artist = StringField("Artist",
                         validators=[InputRequired()])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
