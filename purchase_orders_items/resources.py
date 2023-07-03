from flask import jsonify
from flask_restful import Resource, reqparse

purchase_orders = [
    {
        "id": 1,
        "description": "Pedido de compra 1",
        "items": [{"id": 1, "description": "Item do pedido 1", "price": 20.99}],
    }
]


class PurchaseOrdersItems(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("id", type=int, required=True, help="Informe um id valido")
    parser.add_argument(
        "description", type=str, required=True, help="Informe uma descrição"
    )
    parser.add_argument(
        "price", type=float, required=True, help="Informe um preço valido"
    )

    def get(self, id):
        for order in purchase_orders:
            if order["id"] == id:
                return jsonify(order["items"])

        return jsonify({"message": "Pedido {} não encontrado".format(id)})

    def post(self, id):
        req_data = PurchaseOrdersItems.parser.parse_args()

        obj = {
            "id": req_data["id"],
            "description": req_data["description"],
            "price": req_data["price"],
        }

        for order in purchase_orders:
            if order["id"] == id:
                order["items"].append(obj)
                return jsonify(order)

        return jsonify({"message": "Pedido {} não encontrado".format(id)})
