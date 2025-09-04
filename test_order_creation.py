import data
from sender_samokat_request import post_new_order, get_order_by_track


# Косик Юлия, 34-я когорта — Финальный проект. Инженер по тестированию плюс
def test_create_order_and_get_by_track():
    response = post_new_order(data.new_order_body)
    assert response.status_code == 201

    track_number = response.json()["track"]
    get_response = get_order_by_track(track_number)
    assert get_response.status_code == 200
