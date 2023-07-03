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
