import requests
import config
from datetime import datetime

current_datetime = datetime.now()

formatted_date = current_datetime.strftime("%Y%m%d")



USERNAME = "jreespuff"


def create_user():
    pixela_user_endpoint = 'https://pixe.la/v1/users'
    user_params = {
        "token": config.token,
        "username": "jreespuff",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    user_request = requests.post(pixela_user_endpoint, json=user_params)
    print(user_request.text)


def create_graph(graph_id, graph_name, units):
    pixela_graph_endpoint = 'https://pixe.la/v1/users/jreespuff/graphs'
    header = {
        "X-USER-TOKEN": config.token
    }
    params = {
        "id": graph_id,
        "name": graph_name,
        "unit": units,
        "type": "int",
        "color": "ajisai",

    }
    graph_request = requests.post(pixela_graph_endpoint, json=params, headers=header)
    print(graph_request.text)


def post_to_graph():
    pixela_post_endpoint = 'https://pixe.la/v1/users/jreespuff/graphs/graph1'

    params = {
        "date":formatted_date,
        "quantity": "10",
    }
    header = {
        "X-USER-TOKEN": config.token
    }
    post_request = requests.post(pixela_post_endpoint, json=params, headers=header)
    print(post_request.text)


if __name__ == '__main__':
    post_to_graph()
    pass
