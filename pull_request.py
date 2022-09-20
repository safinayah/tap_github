import json

# body={
# "title":"Amazing new feature",
# "body":"Please pull these awesome changes in!",
# "head":"octocat:new-feature",
# "base":"master"
# }
import requests

with open("config.json", 'r') as f:
    data_conf = f.readlines()
token = data_conf["access_token"]
owner_name = data_conf["Owner_name"]
repo_name = data_conf["repo_name"]



def get_pull_requests(token, owner_name, repo_name):
    _url = "https://api.github.com/repos/{}/{}/pulls".format(owner_name, repo_name)

    _headers = {
        # "post": "/repos/amerknane/ameerkn/ameerkn/pulls",
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(token),

    }
    response = requests.get(_url, _headers)
    return response
