from app.models import *
from datetime import datetime


def push_notifications(text, table, color):

    N = Notifications(title=text, table=table, color=color,date=datetime.utcnow())
    db.session.add(N)

    # Overflow check
    if Notifications.query.count() > 8:
        N = Notifications.query.order_by(Notifications.date.asc()).all()
        db.session.delete(N[0])

    db.session.commit()
