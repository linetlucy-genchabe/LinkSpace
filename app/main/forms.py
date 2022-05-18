from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,SubmitField, SelectField,FileField)
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image_file = FileField( 'Picture',validators=[FileRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[DataRequired()])
    alias = StringField("Comment by")
    submit = SubmitField("Comment")
