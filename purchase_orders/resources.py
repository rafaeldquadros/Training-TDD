from flask_restful import Resource, reqparse
from .services import PurchaseOrdersServices
from flask_jwt_extended import jwt_required


class PurchaseOrders(Resource):
    __service__ = PurchaseOrdersServices()

    parser = reqparse.RequestParser()
    parser.add_argument(
        "description", type=str, required=True, help="Informe uma descrição"
    )
    parser.add_argument(
        "quantity", type=int, required=True, help="Informe uma quantidade"
    )

    @jwt_required()
    def get(self):
        return self.__service__.find_all()

    @jwt_required()
    def post(self):
        data = PurchaseOrders.parser.parse_args()

        return self.__service__.create(**data)


class PurchaseOrdersById(Resource):
    __service__ = PurchaseOrdersServices()

    @jwt_required()
    def get(self, id):
        return self.__service__.find_by_id(id)
