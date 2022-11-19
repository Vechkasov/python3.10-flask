from flask import render_template, redirect, url_for, flash, request
from app.tables import tb
from app.models import *
from app.tables.forms import *
from app.tables.handlers.functions import push_notifications


@tb.route('/employees/add', methods=["POST", "GET"])
def employees_table_add():
    form = EmployeeForm()

    if form.validate_on_submit():
        surname = request.form['surname']
        name = request.form['name']
        patronymic = request.form['patronymic']
        date_of_birth = request.form['date_of_birth']
        phone_number = request.form['phone_number']
        gender = request.form['gender']
        date = datetime.strptime(date_of_birth, "%Y-%m-%d").date()

        E = Employee(surname=surname, name=name, patronymic=patronymic,
                     date_of_birth=date, phone_number=phone_number,
                     gender=gender)
        try:
            db.session.add(E)
            db.session.commit()

            title = 'New employee created successfully'
            flash(title)
            push_notifications(title, 'Employee', 'success')
            return redirect(url_for('tables.employees_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating employee'
            flash(title)
            push_notifications(title, 'Employee', 'warning')
    return render_template('tables/add/employees.html', title='Add employee', form=form)


@tb.route('/jobs/add', methods=["POST", "GET"])
def jobs_table_add():
    form = JobForm()

    if form.validate_on_submit():
        job_title = request.form['job_title']
        salary = request.form['salary']

        E = Job(job_title=job_title, salary=salary)
        try:
            db.session.add(E)
            db.session.commit()

            title = 'New job created successfully'
            flash(title)
            push_notifications(title, 'Job', 'success')
            return redirect(url_for('tables.jobs_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating job'
            flash(title)
            push_notifications(title, 'Job', 'warning')
    return render_template('tables/add/jobs.html', title='Add job', form=form)


@tb.route('/assignments/add', methods=["POST", "GET"])
def assignments_table_add():
    form = AssignmentForm()

    jobs = [[item.id, item.job_title] for item in Job.query.all()]
    employees = [[item.id, item.surname + " " + item.name] for item in Employee.query.all()]

    form.job.choices = jobs
    form.employee.choices = employees

    if len(jobs) == 0 or len(employees) == 0:
        title = 'Add one job for creating assignment' if len(jobs) == 0 \
            else 'Add one employee for creating assignment'
        flash(title)
        push_notifications(title, 'Assignments', 'warning')
        return redirect(url_for('tables.assignments_table_view'))

    if form.validate_on_submit():
        appointment_date = request.form['appointment_date']
        date = datetime.strptime(appointment_date, "%Y-%m-%d").date()

        job = request.form['job']
        employee = request.form['employee']

        A = Assignment(appointment_date=date, employee_id=employee, job_id=job)
        try:
            db.session.add(A)
            db.session.commit()

            title = 'New assignment created successfully'
            flash(title)
            push_notifications(title, 'Assignment', 'success')
            return redirect(url_for('tables.assignments_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating assignment'
            flash(title)
            push_notifications(title, 'Assignment', 'warning')
    return render_template('tables/add/assignments.html', title='Add assignment', form=form)


@tb.route('/sale_of_items/add', methods=["POST", "GET"])
def sale_of_items_table_add():
    form = SaleForm()

    items = [[item.id, item.name] for item in Item.query.all()]
    employees = [[item.id, item.surname + " " + item.name] for item in Employee.query.all()]

    form.item.choices = items
    form.employee.choices = employees

    if len(items) == 0 or len(employees) == 0:
        title = 'Add one item for creating sale of items' if len(items) == 0 \
            else 'Add one employee for creating sale of items'
        flash(title)
        push_notifications(title, 'Sale of item', 'warning')
        return redirect(url_for('tables.sale_of_items_table_view'))

    if form.validate_on_submit():
        count = request.form['count']
        sum = request.form['sum']
        date = datetime.strptime(request.form['date'], "%Y-%m-%d").date()

        item = request.form['item']
        employee = request.form['employee']

        S = Sale_of_item(count=count, sum=sum, date=date, item_id=item, employee_id=employee)
        try:
            db.session.add(S)
            db.session.commit()

            title = 'New sale of item created successfully'
            flash(title)
            push_notifications(title, 'Sale of item', 'success')
            return redirect(url_for('tables.sale_of_items_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating sale of item'
            flash(title)
            push_notifications(title, 'Sale of item', 'warning')
    return render_template('tables/add/sale_of_items.html', title='Add sale of items', form=form)


@tb.route('/items/add', methods=["POST", "GET"])
def items_table_add():
    form = ItemForm()

    if form.validate_on_submit():
        name = request.form['name']
        count = request.form['count']
        price = request.form['price']

        I = Item(name=name, count=count, price=price)
        try:
            db.session.add(I)
            db.session.commit()

            title = 'New item created successfully'
            flash(title)
            push_notifications(title, 'Item', 'success')
            return redirect(url_for('tables.items_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating item'
            flash(title)
            push_notifications(title, 'Item', 'warning')
    return render_template('tables/add/items.html', title='Add item', form=form)


@tb.route('/supplies/add', methods=["POST", "GET"])
def supplies_table_add():
    form = SupplyForm()

    items = [[item.id, item.name] for item in Item.query.all()]
    providers = [[item.id, item.address] for item in Provider.query.all()]
    catalogs = [[item.id, item.name] for item in Catalog.query.all()]

    form.item.choices = items
    form.provider.choices = providers
    form.catalog.choices = catalogs

    if len(items) == 0 or len(providers) == 0 or len(catalogs) == 0:
        title = 'Add one item for creating supply' if len(items) == 0 \
            else 'Add one provider for creating supply' if len(providers) == 0 \
            else 'Add one catalog for creating supply'

        flash(title)
        push_notifications(title, 'Supply', 'warning')
        return redirect(url_for('tables.supplies_table_view'))

    if form.validate_on_submit():
        count = request.form['count']
        price = request.form['price']
        date = datetime.strptime(request.form['date'], "%Y-%m-%d").date()

        item = request.form['item']
        provider = request.form['provider']
        catalog = request.form['catalog']

        S = Supply(count=count, price=price, date=date, item_id=item,
                   catalog_id=catalog, provider_id=provider)
        try:
            db.session.add(S)
            db.session.commit()

            title = 'New supply created successfully'
            flash(title)
            push_notifications(title, 'Supply', 'success')
            return redirect(url_for('tables.supplies_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating supply'
            flash(title)
            push_notifications(title, 'Supply', 'warning')
    return render_template('tables/add/supplies.html', title='Add supply', form=form)


@tb.route('/providers/add', methods=["POST", "GET"])
def providers_table_add():
    form = ProviderForm()

    if form.validate_on_submit():
        address = request.form['address']
        phone_number = request.form['phone_number']

        P = Provider(address=address, phone_number=phone_number)
        try:
            db.session.add(P)
            db.session.commit()

            title = 'New provider created successfully'
            flash(title)
            push_notifications(title, 'Provider', 'success')
            return redirect(url_for('tables.providers_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating provider'
            flash(title)
            push_notifications(title, 'Provider', 'warning')
    return render_template('tables/add/providers.html', title='Add provider', form=form)


@tb.route('/catalogs/add', methods=["POST", "GET"])
def catalogs_table_add():
    form = CatalogForm()

    manufacturers = [[item.id, item.name] for item in Manufacturer.query.all()]
    groups = [[item.id, item.name] for item in Group.query.all()]

    form.manufacturer.choices = manufacturers
    form.group.choices = groups

    if len(manufacturers) == 0 or len(groups) == 0:
        title = 'Add one manufacturer for creating catalog' if len(manufacturers) == 0 \
            else 'Add one group for creating catalogs'
        flash(title)
        push_notifications(title, 'Catalog', 'warning')
        return redirect(url_for('tables.catalogs_table_view'))

    if form.validate_on_submit():
        name = request.form['name']
        manufacturer = request.form['manufacturer']
        group = request.form['group']

        C = Catalog(name=name, manufacturer_id=manufacturer, group_id=group)
        try:
            db.session.add(C)
            db.session.commit()

            title = 'New catalog created successfully'
            flash(title)
            push_notifications(title, 'Catalog', 'success')
            return redirect(url_for('tables.catalogs_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating catalog'
            flash(title)
            push_notifications(title, 'Catalog', 'warning')
    return render_template('tables/add/catalogs.html', title='Add catalog', form=form)


@tb.route('/manufacturers/add', methods=["POST", "GET"])
def manufacturers_table_add():
    form = ManufacturerForm()

    if form.validate_on_submit():
        name = request.form['name']
        country = request.form['country']

        M = Manufacturer(name=name, country=country)
        try:
            db.session.add(M)
            db.session.commit()

            title = 'New manufacturer created successfully'
            flash(title)
            push_notifications(title, 'Manufacturer', 'success')
            return redirect(url_for('tables.manufacturers_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating manufacturer'
            flash(title)
            push_notifications(title, 'Manufacturer', 'warning')
    return render_template('tables/add/manufacturers.html', title='Add manufacturer', form=form)


@tb.route('/groups/add', methods=["POST", "GET"])
def groups_table_add():
    form = GroupForm()

    if form.validate_on_submit():
        name = request.form['name']

        G = Group(name=name)
        try:
            db.session.add(G)
            db.session.commit()

            title = 'New group created successfully'
            flash(title)
            push_notifications(title, 'Group', 'success')
            return redirect(url_for('tables.groups_table_view'))
        except:
            db.session.rollback()
            title = 'Error creating group'
            flash(title)
            push_notifications(title, 'Group', 'warning')
    return render_template('tables/add/groups.html', title='Add group', form=form)
