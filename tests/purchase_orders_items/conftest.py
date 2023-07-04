import pytest
from db import db
from purchase_orders_items.model import PurchaseOrderItemsModel
from purchase_orders.model import PurchaseOrderModel


@pytest.fixture()
def seed_db():
    po = PurchaseOrderModel("Purchase Order Teste")
    db.session.add(po)
    db.session.commit()

    poi = PurchaseOrderItemsModel("item 1", 10.39, po.id)
    db.session.add(poi)
    db.session.commit()

    yield {"purchase_order": po, "items": poi}


@pytest.fixture(scope="function", autouse=True)
def clear_db():
    db.session.query(PurchaseOrderItemsModel).delete()
    db.session.query(PurchaseOrderModel).delete()
    db.session.commit()
