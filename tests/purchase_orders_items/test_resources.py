import json


def test_get_purchase_order_item(test_client):
    response = test_client.get("/purchase_orders/1/items")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["id"] == 1
    assert response.json[0]["description"] == "Item do pedido 1"
    assert response.json[0]["price"] == 20.99


def test_get_purchase_order_item_invalid_id(test_client):
    id = 29
    response = test_client.get("/purchase_orders/{}/items".format(id))

    assert response.status_code == 200
    assert response.json["message"] == "Pedido {} não encontrado".format(id)


def test_post_purchase_order_item(test_client):
    obj = {"id": 2, "description": "pedido de alguma coisa", "price": 20.99}
    response = test_client.post(
        "/purchase_orders/1/items",
        data=json.dumps(obj),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["description"] == "Pedido de compra 1"
    assert len(response.json["items"]) == 2
    assert response.json["items"][0]["id"] == 1
    assert response.json["items"][0]["description"] == "Item do pedido 1"
    assert response.json["items"][0]["price"] == 20.99
    assert response.json["items"][1]["id"] == 2
    assert response.json["items"][1]["description"] == "pedido de alguma coisa"
    assert response.json["items"][1]["price"] == 20.99


def test_post_purchase_order_item_invalid_id(test_client):
    obj = {"id": 2, "description": "pedido de alguma coisa", "price": 20.99}
    id = 29
    response = test_client.post(
        "/purchase_orders/{}/items".format(id),
        data=json.dumps(obj),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.json["message"] == "Pedido {} não encontrado".format(id)


def test_post_purchase_order_item_empty_id(test_client):
    obj = {"description": "pedido de alguma coisa", "price": 20.99}

    response = test_client.post(
        "/purchase_orders/1/items",
        data=json.dumps(obj),
        content_type="application/json",
    )

    assert response.status_code == 400
    assert response.json["message"]["id"] == "Informe um id valido"


def test_post_purchase_order_item_empty_description(test_client):
    obj = {"id": 2, "price": 20.99}

    response = test_client.post(
        "/purchase_orders/1/items",
        data=json.dumps(obj),
        content_type="application/json",
    )

    assert response.status_code == 400
    assert response.json["message"]["description"] == "Informe uma descrição"


def test_post_purchase_order_item_empty_price(test_client):
    obj = {"id": 2, "description": "pedido de alguma coisa"}

    response = test_client.post(
        "/purchase_orders/1/items",
        data=json.dumps(obj),
        content_type="application/json",
    )

    assert response.status_code == 400
    assert response.json["message"]["price"] == "Informe um preço valido"
