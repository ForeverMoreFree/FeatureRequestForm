from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,IntegerField,DateField,
                     TextAreaField,SubmitField,HiddenField)
from wtforms.validators import DataRequired


# Form is created with wtforms and is sent to "add_feature" and read by jinja
class FeatureRequestForm(FlaskForm):

    title = StringField('Title of Feature:', validators=[DataRequired()])
    description = StringField('Descrition of Feature Request:', validators=[DataRequired()])
    client = SelectField('Choose the client:',
                         choices=[('Client A', 'Client A'), ('Client B', 'Client B'),
                                  ('Client C', 'Client C')], validators=[DataRequired()])
    client_priority = SelectField('Choose the feature priority',
                                  choices=[('1', 'Priority 1'), ('2', 'Priority 2'),
                                           ('3', 'Priority 3'), ('4', 'Priority 4'),
                                           ('5', 'Priority 5'), ('6', 'Priority 6'),
                                           ('7', 'Priority 7'), ('8', 'Priority 8'),
                                           ('9', 'Priority 9'), ('10', 'Priority 10')],
                                           validators=[DataRequired()])
    ## Will dynamically change the priority listings based on database results in future version.
    target_date = StringField("Select a Target Date (Format of mm/dd/yyyy)", validators=[DataRequired()])
    product_area = SelectField('Product area',
                               choices=[('Policies', 'Policies'), ('Billing', 'Billing'),
                                        ('Claims', 'Claims'), ('Reports', 'Reports')], validators=[DataRequired()])
    submit = SubmitField('Submit Request')

