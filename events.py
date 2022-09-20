import json
import requests

with open("config.json", 'r') as file:
    pre = file.readlines()
token = pre["access_token"]
owner = pre["owner_name"]
repo = pre["repository_name"]



def get_events(token, owner, repo):
    url = 'https://api.github.com/repos/{}/{}/issues/events'.format('emtaness99', 'test')
    header = {"Accept": "application/vnd.github+json",
              "Authorization": "Bearer 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",
              }
    response = requests.get(url, header)
    return response
