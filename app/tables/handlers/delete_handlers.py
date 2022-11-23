from flask import render_template, flash, request, redirect, url_for
from app.tables import tb
from app.models import *
from app.tables.handlers.functions import push_notifications


@tb.route('/employees/delete/<int:id>', methods=["GET"])
def employees_table_delete(id):
    E = Employee.query.filter_by(id=id).first()

    try:
        A = Assignment.query.filter_by(employee=E)
        S = Sale_of_item.query.filter_by(employee=E)

        count = 0
        for item in A:
            count += 1
            db.session.delete(item)
            db.session.commit()
        for item in S:
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
    S = Sale_of_item.query.filter_by(id=id).first()

    try:
        db.session.delete(S)
        db.session.commit()

        title = 'Sale of item successfully removed'
        flash(title)
        push_notifications(title, 'Sale of item', 'danger')
    except:
        title = 'Sale of item deletion error'
        flash(title)
        push_notifications(title, 'Sale of item', 'warning')
    return redirect(url_for('tables.sale_of_items_table_view'))


@tb.route('/items/delete/<int:id>', methods=["GET"])
def items_table_delete(id):
    I = Item.query.filter_by(id=id).first()

    try:
        Su = Supply.query.filter_by(item=I)
        Sa = Sale_of_item.query.filter_by(item=I)

        count = 0
        for item in Sa:
            count += 1
            db.session.delete(item)
            db.session.commit()
        for item in Su:
            count += 1
            db.session.delete(item)
            db.session.commit()

        db.session.delete(I)
        db.session.commit()

        title = f'Item and {count} records from related tables successfully removed'
        flash(title)
        push_notifications(title, 'Item', 'danger')
    except:
        title = 'Item deletion error'
        flash(title)
        push_notifications(title, 'Item', 'warning')
    return redirect(url_for('tables.items_table_view'))


@tb.route('/supplies/delete/<int:id>', methods=["GET"])
def supplies_table_delete(id):
    S = Supply.query.filter_by(id=id).first()

    try:
        db.session.delete(S)
        db.session.commit()

        title = 'Supply successfully removed'
        flash(title)
        push_notifications(title, 'Supply', 'danger')
    except:
        title = 'Supply deletion error'
        flash(title)
        push_notifications(title, 'Supply', 'warning')
    return redirect(url_for('tables.supplies_table_view'))


@tb.route('/providers/delete/<int:id>', methods=["GET"])
def providers_table_delete(id):
    P = Provider.query.filter_by(id=id).first()

    try:
        S = Supply.query.filter_by(provider=P)
        count = 0
        for item in S:
            count += 1
            db.session.delete(item)
            db.session.commit()

        db.session.delete(P)
        db.session.commit()

        title = f'Provider and {count} records from related tables successfully removed'
        flash(title)
        push_notifications(title, 'Provider', 'danger')
    except:
        title = 'Provider deletion error'
        flash(title)
        push_notifications(title, 'Provider', 'warning')
    return redirect(url_for('tables.providers_table_view'))


@tb.route('/catalogs/delete/<int:id>', methods=["GET"])
def catalogs_table_delete(id):
    C = Catalog.query.filter_by(id=id).first()
    try:
        S = Supply.query.filter_by(catalog=C)
        for item in S:
            db.session.delete(item)
            db.session.commit()

        db.session.delete(C)
        db.session.commit()

        title = 'Catalog successfully removed'
        flash(title)
        push_notifications(title, 'Catalog', 'danger')
    except:
        title = 'Catalog deletion error'
        flash(title)
        push_notifications(title, 'Catalog', 'warning')
    return redirect(url_for('tables.catalogs_table_view'))


@tb.route('/manufacturers/delete/<int:id>', methods=["GET"])
def manufacturers_table_delete(id):
    M = Manufacturer.query.filter_by(id=id).first()

    try:
        C = Catalog.query.filter_by(manufacturer=M)
        count = 0
        for item in C:
            count += 1
            db.session.delete(item)
            db.session.commit()

        db.session.delete(M)
        db.session.commit()

        title = f'Manufacturer and {count} records from related tables successfully removed'
        flash(title)
        push_notifications(title, 'Manufacturer', 'danger')
    except:
        title = 'Manufacturer deletion error'
        flash(title)
        push_notifications(title, 'Manufacturer', 'warning')
    return redirect(url_for('tables.manufacturers_table_view'))


@tb.route('/groups/delete/<int:id>', methods=["GET"])
def groups_table_delete(id):
    G = Group.query.filter_by(id=id).first()

    try:
        C = Catalog.query.filter_by(group=G)
        count = 0
        for item in C:
            count += 1
            db.session.delete(item)
            db.session.commit()

        db.session.delete(G)
        db.session.commit()

        title = f'Group and {count} records from related tables successfully removed'
        flash(title)
        push_notifications(title, 'Group', 'danger')
    except:
        title = 'Group deletion error'
        flash(title)
        push_notifications(title, 'Group', 'warning')
    return redirect(url_for('tables.groups_table_view'))
