from datetime import datetime
from app import db


class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    table = db.Column(db.String(64), nullable=False)
    color = db.Column(db.String(64), nullable=False)

    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Notifications {}>'.format(self.title)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(64), unique=True, nullable=False)
    salary = db.Column(db.Integer, index=True, nullable=False)

    assignments = db.relationship('Assignment', backref='job', lazy='dynamic')

    def __repr__(self):
        return '<Job {}>'.format(self.job_title)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    patronymic = db.Column(db.String(20), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, default=datetime.date(datetime.utcnow()))
    gender = db.Column(db.String(3), nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)

    assignments = db.relationship('Assignment', backref='employee', lazy='dynamic')
    sale_of_items = db.relationship('Sale_of_item', backref='employee', lazy='dynamic')

    def __repr__(self):
        return '<Employees {} {}>'.format(self.surname, self.name)


class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    appointment_date = db.Column(db.Date, default=datetime.date(datetime.utcnow()))

    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)

    def __repr__(self):
        return '<Assignment {}>'.format(self.appointment_date)


class Sale_of_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, primary_key=True, nullable=True)
    sum = db.Column(db.Integer, primary_key=True, nullable=True)
    date = db.Column(db.Date, default=datetime.utcnow)

    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)

    def __repr__(self):
        return '<Sale_of_item {} * {}>'.format(self.count, self.sum)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    count = db.Column(db.Integer, primary_key=True, nullable=True)
    price = db.Column(db.Integer, primary_key=True, nullable=True)

    sale_of_items = db.relationship('Sale_of_item', backref='item', lazy='dynamic')
    supplies = db.relationship('Supply', backref='item', lazy='dynamic')

    def __repr__(self):
        return '<Item {} * {}>'.format(self.count, self.price)


class Supply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    count = db.Column(db.Integer, primary_key=True, nullable=True)
    price = db.Column(db.Integer, primary_key=True, nullable=True)

    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=True)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'), nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=True)

    def __repr__(self):
        return '<Supply {} * {}>'.format(self.count, self.price)


class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.Integer, unique=True, nullable=False)

    supplies = db.relationship('Supply', backref='provider', lazy='dynamic')

    def __repr__(self):
        return '<Provider {}>'.format(self.address)


class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    supplies = db.relationship('Supply', backref='catalog', lazy='dynamic')

    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=True)

    def __repr__(self):
        return '<Catalog {}>'.format(self.name)


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(50), unique=True, nullable=False)

    catalogs = db.relationship('Catalog', backref='manufacturer', lazy='dynamic')

    def __repr__(self):
        return '<Manufacturer {}>'.format(self.name)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    catalogs = db.relationship('Catalog', backref='group', lazy='dynamic')

    def __repr__(self):
        return '<Catalog {}>'.format(self.name)
