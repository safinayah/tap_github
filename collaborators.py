import json
import requests


def get_config():
    with open("config.json", "r") as file:
        data = json.load(file)
        return data


def get_collaborators(data):
    _url = "https://api.github.com/repos/{}/{}/collaborators".format(data['owner_name'], data['repo_name'])

    _headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(data['access_token'])
    }
    response = requests.get(url=_url, headers=_headers)
    return response


if __name__ == '__main__':
    configs = get_config()
    response = get_collaborators(configs)
    print(response.json())
