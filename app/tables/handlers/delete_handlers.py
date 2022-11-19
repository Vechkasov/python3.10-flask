from flask import render_template, flash, request, redirect, url_for
from app.tables import tb
from app.models import *
from app.tables.handlers.functions import push_notifications


@tb.route('/employees/delete/<int:id>', methods=["GET"])
def employees_table_delete(id):
    E = Employee.query.filter_by(id=id).first()

    try:
        A = Assignment.query.filter_by(employee=E)
        count = 0
        for item in A:
            count += 1
            db.session.delete(item)
            db.session.commit()

        db.session.delete(E)
        db.session.commit()

        title = f'Employee and {count} records from related tables successfully removed'
        flash(title)
        push_notifications(title, 'Employee', 'danger')
    except:
        title = 'Employee deletion error'
        flash(title)
        push_notifications(title, 'Employee', 'warning')
    return redirect(url_for('tables.employees_table_view'))


@tb.route('/jobs/delete/<int:id>', methods=["GET"])
def jobs_table_delete(id):
    J = Job.query.filter_by(id=id).first()

    try:
        A = Assignment.query.filter_by(job=J)
        count = 0
        for item in A:
            count += 1
            db.session.delete(item)
            db.session.commit()

        db.session.delete(J)
        db.session.commit()

        title = f'Job and {count} records from related tables successfully removed'
        flash(title)
        push_notifications(title, 'Job', 'danger')
    except:
        title = 'Job deletion error'
        flash(title)
        push_notifications(title, 'Job', 'warning')
    return redirect(url_for('tables.jobs_table_view'))


@tb.route('/assignments/delete/<int:id>', methods=["GET"])
def assignments_table_delete(id):
    A = Assignment.query.filter_by(id=id).first()

    try:
        db.session.delete(A)
        db.session.commit()

        title = 'Assignment successfully removed'
        flash(title)
        push_notifications(title, 'Assignment', 'danger')
    except:
        title = 'Assignment deletion error'
        flash(title)
        push_notifications(title, 'Assignment', 'warning')
    return redirect(url_for('tables.assignments_table_view'))


@tb.route('/sale_of_items/delete/<int:id>', methods=["GET"])
def sale_of_items_table_delete(id):
    pass


@tb.route('/items/delete/<int:id>', methods=["GET"])
def items_table_delete(id):
    pass


@tb.route('/supplies/delete/<int:id>', methods=["GET"])
def supplies_table_delete(id):
    pass


@tb.route('/providers/delete/<int:id>', methods=["GET"])
def providers_table_delete(id):
    pass


@tb.route('/catalogs/delete/<int:id>', methods=["GET"])
def catalogs_table_delete(id):
    pass


@tb.route('/manufacturers/delete/<int:id>', methods=["GET"])
def manufacturers_table_delete(id):
    pass


@tb.route('/groups/delete/<int:id>', methods=["GET"])
def groups_table_delete(id):
    pass
