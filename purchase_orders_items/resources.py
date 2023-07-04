from flask import jsonify
from flask_restful import Resource, reqparse
from .model import PurchaseOrderItemsModel
from purchase_orders.model import PurchaseOrderModel
from .services import PurchaseOrdersItemsServices


class PurchaseOrdersItems(Resource):
    __service__ = PurchaseOrdersItemsServices()

    parser = reqparse.RequestParser()
    parser.add_argument(
        "description", type=str, required=True, help="Informe uma descrição"
    )
    parser.add_argument(
        "price", type=float, required=True, help="Informe um preço valido"
    )
    parser.add_argument(
        "quantity", type=int, required=True, help="Informe uma quantidade valida"
    )

    def get(self, id):
        return self.__service__.find_by_purchase_order_id(id)

    def post(self, id):
        data = PurchaseOrdersItems.parser.parse_args()
        data["purchase_order_id"] = id

        return self.__service__.create(**data)
