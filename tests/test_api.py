from app.api import app

def test_successful():
    client = app.test_client()
    response = client.post('/price', json={"price": 990, "coupon": "SALES10"})
    assert response.status_code == 200
    #assert response.get_json() == { "message": "CUPON SALES 10", "Final_price": 1060.29 }


def test_failure():
    client = app.test_client()
    response = client.post('/price', json={"price": "990", "coupon": "SALES10"})
    assert response.status_code == 500
    #assert response.get_json() == {"message": "CUPON SALES 10"}
