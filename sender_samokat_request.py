import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_URL,
                         json=body,
                         headers=data.headers)


def get_order_by_track(track_number):
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER_URL,
                        params={"t": track_number},
                        headers=data.headers)
