from .model import PurchaseOrderItemsModel
from ..purchase_orders.model import PurchaseOrderModel
from flask import jsonify


class PurchaseOrdersItemsServices:
    def get_by_id():
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            purchase_orders = PurchaseOrderItemsModel.find_by_purchase_order_id(id)

            return [p.as_dict() for p in purchase_orders]

        return {"message": "Pedido {} não encontrado".format(id)}
