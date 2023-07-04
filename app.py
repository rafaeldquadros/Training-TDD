from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems
from users.resources import UserCreation, UserLogin
from flask_jwt_extended.exceptions import NoAuthorizationError
from db import db
import os


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.environ["SECRET_KEY"]

    db.init_app(app)

    jwt = JWTManager(app)

    @jwt.unauthorized_loader(NoAuthorizationError)
    def handle_unauthorized_error(reason):
        response = jsonify({"error": "Unauthorized", "reason": reason})
        response.status_code = 401  # Unauthorized
        return response

    Migrate(app, db)

    api.add_resource(PurchaseOrders, "/purchase_orders")
    api.add_resource(PurchaseOrdersById, "/purchase_orders/<int:id>")
    api.add_resource(PurchaseOrdersItems, "/purchase_orders/<int:id>/items")
    api.add_resource(UserCreation, "/users")
    api.add_resource(UserLogin, "/login")

    # @jwt.invalid_token_loader
    # def invalid_jwt(err):
    #     return ({"message": "Token de acesso invalido"}, 401)

    def create_tables():
        db.create_all()

    return app
