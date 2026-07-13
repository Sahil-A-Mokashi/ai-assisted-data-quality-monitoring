from database import db
from datetime import datetime


class Dataset(db.Model):
    __tablename__ = "datasets"

    dataset_id = db.Column(db.Integer, primary_key=True)

    dataset_name = db.Column(db.String(200), nullable=False)

    organisation = db.Column(db.String(200), nullable=False)

    source_system = db.Column(db.String(100))

    domain = db.Column(db.String(100))

    uploaded_by = db.Column(db.String(100))

    upload_date = db.Column(db.DateTime, default=datetime.utcnow)

    total_rows = db.Column(db.Integer, default=0)

    total_columns = db.Column(db.Integer, default=0)

    quality_score = db.Column(db.Float, default=0)

    predicted_risk = db.Column(db.String(20), default="Unknown")

    status = db.Column(db.String(30), default="Pending")

    notes = db.Column(db.Text)

    def to_dict(self):
        return {
            "dataset_id": self.dataset_id,
            "dataset_name": self.dataset_name,
            "organisation": self.organisation,
            "source_system": self.source_system,
            "domain": self.domain,
            "uploaded_by": self.uploaded_by,
            "upload_date": self.upload_date.isoformat() if self.upload_date else None,
            "total_rows": self.total_rows,
            "total_columns": self.total_columns,
            "quality_score": self.quality_score,
            "predicted_risk": self.predicted_risk,
            "status": self.status,
            "notes": self.notes,
        }