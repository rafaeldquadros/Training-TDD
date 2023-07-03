from flask import Flask, jsonify
from flask_restful import Api, Resource
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(PurchaseOrders, "/purchase_orders")
    api.add_resource(PurchaseOrdersById, "/purchase_orders/<int:id>")
    api.add_resource(PurchaseOrdersItems, "/purchase_orders/<int:id>/items")

    return app
