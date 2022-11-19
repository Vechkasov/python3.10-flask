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

            title = 'New employee added successfully'
            flash(title)
            push_notifications(title, 'Employee', 'success')
            return redirect(url_for('tables.employees_table_view'))
        except:
            title = 'Error adding employee'
            flash(title)
            push_notifications(title, 'Employee', 'warning')
    return render_template('tables/add/employees.html', title='Employees', form=form)


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

            title = 'New job added successfully'
            flash(title)
            push_notifications(title, 'Job', 'success')
            return redirect(url_for('tables.jobs_table_view'))
        except:
            title = 'Error adding job'
            flash(title)
            push_notifications(title, 'Job', 'warning')
    return render_template('tables/add/jobs.html', title='Jobs', form=form)


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

            title = 'New assignment added successfully'
            flash(title)
            push_notifications(title, 'Assignment', 'success')
            return redirect(url_for('tables.assignments_table_view'))
        except:
            title = 'Error adding assignment'
            flash(title)
            push_notifications(title, 'Assignment', 'warning')
    return render_template('tables/add/assignments.html', title='Assignment', form=form)


@tb.route('/sale_of_items/add', methods=["POST", "GET"])
def sale_of_items_table_add():
    return "hello"


@tb.route('/items/add', methods=["POST", "GET"])
def items_table_add():
    return "hello"


@tb.route('/supplies/add', methods=["POST", "GET"])
def supplies_table_add():
    return "hello"


@tb.route('/providers/add', methods=["POST", "GET"])
def providers_table_add():
    return "hello"


@tb.route('/catalogs/add', methods=["POST", "GET"])
def catalogs_table_add():
    return "hello"


@tb.route('/manufacturers/add', methods=["POST", "GET"])
def manufacturers_table_add():
    return "hello"


@tb.route('/groups/add', methods=["POST", "GET"])
def groups_table_add():
    return "hello"
