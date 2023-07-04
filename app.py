from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems
from db import db
import os


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.environ["SECRET_KEY"]

    jwt = JWTManager(app)
    db.init_app(app)

    Migrate(app, db)

    api.add_resource(PurchaseOrders, "/purchase_orders")
    api.add_resource(PurchaseOrdersById, "/purchase_orders/<int:id>")
    api.add_resource(PurchaseOrdersItems, "/purchase_orders/<int:id>/items")

    def create_tables():
        db.create_all()

    return app
