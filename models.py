from database import db
from datetime import datetime


class Dataset(db.Model):
    __tablename__ = "datasets"

    dataset_id = db.Column(db.Integer, primary_key=True)

    dataset_name = db.Column(db.String(200), nullable=False)

    organisation = db.Column(db.String(200), nullable=False)

    source_system = db.Column(db.String(100))

    domain = db.Column(db.String(100))

    file_name = db.Column(db.String(255))

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
            "file_name": self.file_name,
            "uploaded_by": self.uploaded_by,
            "upload_date": self.upload_date.isoformat() if self.upload_date else None,
            "total_rows": self.total_rows,
            "total_columns": self.total_columns,
            "quality_score": self.quality_score,
            "predicted_risk": self.predicted_risk,
            "status": self.status,
            "notes": self.notes,
        }

class QualityMetrics(db.Model):
    __tablename__ = "quality_metrics"

    metric_id = db.Column(db.Integer, primary_key=True)

    dataset_id = db.Column(
        db.Integer,
        db.ForeignKey("datasets.dataset_id"),
        nullable=False
    )

    # Profiling Metrics
    missing_values = db.Column(db.Integer, default=0)
    duplicate_rows = db.Column(db.Integer, default=0)
    null_percentage = db.Column(db.Float, default=0)

    completeness_score = db.Column(db.Float, default=0)
    consistency_score = db.Column(db.Float, default=0)

    # AI Results
    anomaly_probability = db.Column(db.Float, default=0.0)
    anomaly_status = db.Column(db.String(20), default="Pending")

    # Future Improvements
    report_path = db.Column(db.String(500))
    corrected_dataset_path = db.Column(db.String(500))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    dataset = db.relationship(
        "Dataset",
        backref=db.backref("quality_metrics", lazy=True)
    )

    def to_dict(self):
        return {
            "metric_id": self.metric_id,
            "dataset_id": self.dataset_id,
            "missing_values": self.missing_values,
            "duplicate_rows": self.duplicate_rows,
            "null_percentage": self.null_percentage,
            "completeness_score": self.completeness_score,
            "consistency_score": self.consistency_score,
            "anomaly_probability": self.anomaly_probability,
            "anomaly_status": self.anomaly_status,
            "report_path": self.report_path,
            "corrected_dataset_path": self.corrected_dataset_path,
            "created_at": self.created_at.isoformat()
        }