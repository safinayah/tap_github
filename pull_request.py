import json

# body={
# "title":"Amazing new feature",
# "body":"Please pull these awesome changes in!",
# "head":"octocat:new-feature",
# "base":"master"
# }
import requests

def read_config():
    with open("config.json", 'r') as f:
        data_conf = f.readlines()
    return data_conf


_headers = {
        # "post": "/repos/amerknane/ameerkn/ameerkn/pulls",
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",

    }
def get_pull_requests(data):
    _url = "https://api.github.com/repos/{}/{}/pulls".format(data['access_token'],data['repo_name'])


    response = requests.get(_url, _headers)

    return response

if __name__ == '__main__':
    data=read_config()
    get_pull_requests(data)



