from flask import render_template
from app.tables import tb
from app.models import *


@tb.route('/employees')
def employees_table_view():
    data = Employee.query.all()
    return render_template('tables/view/employees.html', title='Employees', data=data)


@tb.route('/jobs')
def jobs_table_view():
    data = Job.query.all()
    return render_template('tables/view/jobs.html', title='Jobs', data=data)


@tb.route('/assignments')
def assignments_table_view():
    data = Assignment.query.all()
    return render_template('tables/view/assignments.html', title='Assignment', data=data)


@tb.route('/sale_of_items')
def sale_of_items_table_view():
    data = Sale_of_item.query.all()
    return render_template('tables/view/sale_of_items.html', title='Sale of items', data=data)


@tb.route('/items')
def items_table_view():
    data = Item.query.all()
    return render_template('tables/view/items.html', title='Items', data=data)


@tb.route('/supplies')
def supplies_table_view():
    data = Supply.query.all()
    return render_template('tables/view/supplies.html', title='Supplies', data=data)


@tb.route('/providers')
def providers_table_view():
    data = Provider.query.all()
    return render_template('tables/view/providers.html', title='Providers', data=data)


@tb.route('/catalogs')
def catalogs_table_view():
    data = Catalog.query.all()
    return render_template('tables/view/catalogs.html', title='Catalogs', data=data)


@tb.route('/manufacturers')
def manufacturers_table_view():
    data = Manufacturer.query.all()
    return render_template('tables/view/manufacturers.html', title='Manufacturers', data=data)


@tb.route('/groups')
def groups_table_view():
    data = Group.query.all()
    return render_template('tables/view/groups.html', title='Groups', data=data)
