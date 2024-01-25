import requests


def create_user():
    pixela_user_endpoint = 'https://pixe.la/v1/users'
    user_params = {
        "token": "adsfhaAHdf",
        "username": "jreespuff",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    user_request = requests.post(pixela_user_endpoint, json=user_params)
    print(user_request.text)


if __name__ == '__main__':
    create_user()
