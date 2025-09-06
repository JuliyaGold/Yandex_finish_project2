import sender_stand_request
import data

def test_track_order():
    create_order = sender_stand_request.post_new_order(data.order_body)
    assert create_order.status_code in (200,201)

    create_json = create_order.json()
    assert "track" in create_json
    track = create_json["track"]

    track_order = sender_stand_request.get_track_order(track)
    assert track_order.status_code == 200