from flask import jsonify
from flask_restful import Resource, reqparse
from .model import PurchaseOrderItemsModel
from purchase_orders.model import PurchaseOrderModel


class PurchaseOrdersItems(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "description", type=str, required=True, help="Informe uma descrição"
    )
    parser.add_argument(
        "price", type=float, required=True, help="Informe um preço valido"
    )

    def get(self, id):
        purchase_order = PurchaseOrderModel.find_by_id(id)
        if purchase_order:
            purchase_orders = PurchaseOrderItemsModel.find_by_purchase_order_id(id)

            return [p.as_dict() for p in purchase_orders]

        return {"message": "Pedido {} não encontrado".format(id)}

    def post(self, id):
        purchase_orders = PurchaseOrderModel.find_by_id(id)
        if purchase_orders:
            data = PurchaseOrdersItems.parser.parse_args()
            data["purchase_order_id"] = id

            purchase_orders_items = PurchaseOrderItemsModel(**data)
            purchase_orders_items.save()

            return purchase_orders_items.as_dict()
        return jsonify({"message": "Pedido {} não encontrado".format(id)})
