from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, DateField, FieldList
from wtforms.validators import DataRequired, Length, NumberRange


class JobForm(FlaskForm):
    job_title = StringField('Job title', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired(), NumberRange(min=0, max=1000000)])

    submit = SubmitField('Add')


class EmployeeForm(FlaskForm):
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    patronymic = StringField('Patronymic', validators=[DataRequired()])

    date_of_birth = DateField('Date of birth', validators=[DataRequired()])
    phone_number = IntegerField('Phone number', validators=[DataRequired(), NumberRange(min=1000000, max=1000000000000)])

    gender = SelectField('Gender', choices=[('m', 'man'), ('w', 'woman')], default='m')

    submit = SubmitField('Add')

 
class AssignmentForm(FlaskForm):
    appointment_date = DateField('Date', validators=[DataRequired()])

    job = SelectField('Job', choices=[], validators=[DataRequired()])
    employee = SelectField('Employee', choices=[], validators=[DataRequired()])

    submit = SubmitField('Add')


class SaleForm(FlaskForm):
    count = IntegerField('Count', validators=[DataRequired(), NumberRange(min=0, max=1000000)])
    sum = IntegerField('Sum', validators=[DataRequired(), NumberRange(min=0, max=1000000)])

    date = DateField('Date', validators=[DataRequired()])

    item = SelectField('Item', choices=[], validators=[DataRequired()])
    employee = SelectField('Employee', choices=[], validators=[DataRequired()])

    submit = SubmitField('Add')


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    count = IntegerField('Count', validators=[DataRequired(), NumberRange(min=0, max=1000000)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0, max=1000000)])

    submit = SubmitField('Add')


class SupplyForm(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])

    count = IntegerField('Count', validators=[DataRequired(), NumberRange(min=0, max=1000000)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0, max=1000000)])

    item = SelectField('Item', choices=[], validators=[DataRequired()])
    provider = SelectField('Provider', choices=[], validators=[DataRequired()])
    catalog = SelectField('Catalog', choices=[], validators=[DataRequired()])

    submit = SubmitField('Add')


class ProviderForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    phone_number = IntegerField('Phone number', validators=[DataRequired(), NumberRange(min=1000000, max=1000000000000)])

    submit = SubmitField('Add')


class CatalogForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    manufacturer = SelectField('Manufacturer', choices=[], validators=[DataRequired()])
    group = SelectField('Group', choices=[], validators=[DataRequired()])

    submit = SubmitField('Add')


class ManufacturerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])

    submit = SubmitField('Add')


class GroupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    submit = SubmitField('Add')
