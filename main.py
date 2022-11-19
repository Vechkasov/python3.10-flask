from app import app, db
from app.models import *


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Job': Job,
        'Notifications': Notifications,
        'Employee': Employee,
        'Assignment': Assignment,
        'Sale_of_item': Sale_of_item,
        'Item': Item,
        'Supply': Supply,
        'Provider': Provider,
        'Catalog': Catalog,
        'Manufacturer': Manufacturer
    }


if __name__ == '__main__':
    app.run(debug=True)
