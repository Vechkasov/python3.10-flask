from app import app, db
from app.models import Job


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Job': Job}


if __name__ == '__main__':
    app.run(debug=True)
