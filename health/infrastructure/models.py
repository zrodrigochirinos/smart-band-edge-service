from peewee import AutoField, Model, CharField, FloatField, DateTimeField

from shared.infrastructure.database import db


class HealthRecord(Model):
    """
    ORM model for health_records table in the Health context.
    """
    id = AutoField()
    device_id = CharField()
    bpm = FloatField()
    created_at = DateTimeField()

    class Meta:
        database = db
        table_name = 'health_records'