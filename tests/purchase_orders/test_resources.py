import json


def test_get_purchase_orders(test_client):
    response = test_client.get("/purchase_orders")
    print(response)
    assert response.status_code == 200
    assert response.json[0]["id"] == 1
    assert response.json[0]["description"] == "Pedido de compra 1"
    assert len(response.json[0]["items"]) == 1
    assert response.json[0]["items"][0]["id"] == 1
    assert response.json[0]["items"][0]["description"] == "Item do pedido 1"
    assert response.json[0]["items"][0]["price"] == 20.99


def test_post_purchase_orders(test_client):
    obj = {"id": 2, "description": "Purchase order id 2"}

    response = test_client.post(
        "/purchase_orders", data=json.dumps(obj), content_type="application/json"
    )

    assert response.status_code == 200
    assert response.json["id"] == 2
    assert response.json["description"] == "Purchase order id 2"
    assert len(response.json["items"]) == 0
