import pytest
from db import db
from purchase_orders.model import PurchaseOrderModel
from purchase_orders_items.model import PurchaseOrderItemsModel


@pytest.fixture()
def seed_db():
    po = PurchaseOrderModel("Purchase Order Teste", 50)
    db.session.add(po)
    db.session.commit()

    yield po


@pytest.fixture(scope="function", autouse=True)
def clear_db(request):
    if "nocleardb" in request.keywords:
        return
    db.session.query(PurchaseOrderItemsModel).delete()
    db.session.query(PurchaseOrderModel).delete()
    db.session.commit()
