from flask import Flask, jsonify
from flask_restful import Api, Resource
from purchase_orders.resources import PurchaseOrders, PurchaseOrdersById
from purchase_orders_items.resources import PurchaseOrdersItems
from db import db
import mysql.connector


# def create_mysql_connection():
#     connection = mysql.connector.connect(
#         host="localhost",  # host do MySQL
#         user="root",  # nome de usuário do MySQL
#         password="1234",  # senha do MySQL
#         database="udemy_api",  # nome do banco de dados que você deseja conectar
#     )
#     return connection


def create_app():
    # connection = create_mysql_connection()  # criar conexão com o MySQL

    app = Flask(__name__)
    api = Api(app)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mysql+mysqlconnector://root:1234@localhost/udemy_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api.add_resource(PurchaseOrders, "/purchase_orders")
    api.add_resource(PurchaseOrdersById, "/purchase_orders/<int:id>")
    api.add_resource(PurchaseOrdersItems, "/purchase_orders/<int:id>/items")

    def create_tables():
        db.create_all()

    return app
