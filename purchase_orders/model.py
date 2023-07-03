from db import db


class PurchaseOrderModel(db.Model):
    __tablename__ = "purchase_orders"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, description):
        self.description = description

    def as_dict(self):
        return {c.key: getattr(self, c.key) for c in self.__mapper__.column_attrs}

    @classmethod
    def find_all(cls):
        return cls.query.all()  # select * from purchase_order

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(
            id=_id
        ).first()  # select * from purchase_order where id = _id

    def save(self):
        db.session.add(self)
        db.session.commit()
