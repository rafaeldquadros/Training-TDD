from .model import PurchaseOrderModel
from flask import jsonify
from .exceptions import QuantityException


class PurchaseOrdersServices:
    def _check_quantity(self, quantity):
        if quantity < 50 or quantity > 150:
            raise QuantityException("A quantidade deve ser entre 50 e 150 itens")

    def find_all(self):
        purchase_order = PurchaseOrderModel.find_all()
        return [p.as_dict() for p in purchase_order]

    def create(self, **kwargs):
        self._check_quantity(kwargs["quantity"])
        purchase_order = PurchaseOrderModel(**kwargs)
        purchase_order.save()

        return purchase_order.as_dict()

    def find_by_id(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            return purchase_order.as_dict()

        return jsonify({"message": "Pedido {} não encontrado".format(id)})
