from .model import PurchaseOrderItemsModel
from ..purchase_orders.model import PurchaseOrderModel
from resources import PurchaseOrdersItems
from flask import jsonify


class PurchaseOrdersItemsServices:
    def find_by_purchase_order_id(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            purchase_orders = PurchaseOrderItemsModel.find_by_purchase_order_id(id)

            return [p.as_dict() for p in purchase_orders]

        return {"message": "Pedido {} não encontrado".format(id)}

    def create(self, **kwargs):
        purchase_orders = PurchaseOrderModel.find_by_id(kwargs["purchase_order_id"])
        if purchase_orders:
            purchase_orders_items = PurchaseOrderItemsModel(**kwargs)
            purchase_orders_items.save()

            return purchase_orders_items.as_dict()
        return jsonify(
            {"message": "Pedido {} não encontrado".format(kwargs["purchase_order_id"])}
        )
