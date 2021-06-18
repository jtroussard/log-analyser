from analyser_app import db

class ErxLog(db.Model):
    log_id = db.Column(db.Integer, primary_key=True)
    log_hash = db.Column(db.String, nullable=False, unique=True)
    log_stack_strace = db.Column(db.String)