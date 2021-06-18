from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, ValidationError
from analyser_app.models import ErxLog

class SearchReport(FlaskForm):
    search_input = StringField()

class UploadLogForm(FlaskForm):
    file = FileField(validators=[DataRequired(), FileAllowed(['log', 'txt'])])
    submit = SubmitField("Upload")