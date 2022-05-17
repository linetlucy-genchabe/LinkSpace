from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,SubmitField, SelectField,FileField)
from wtforms.validators import DataRequired,FileRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = FileField( 'Picture',validators=[FileRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[DataRequired()])
    alias = StringField("Comment by")
    submit = SubmitField("Comment")
