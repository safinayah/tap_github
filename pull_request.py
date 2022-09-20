import json
import requests
# body={
# "title":"Amazing new feature",
# "body":"Please pull these awesome changes in!",
# "head":"octocat:new-feature",
# "base":"master"
# }



def read_config():
    with open("config.json", 'r') as f:
        data_conf = json.load(f)

    return data_conf





def get_pull_requests(data):
    _url = "https://api.github.com/repos/{}/{}/pulls".format(data['Owner_name'],data['repo_name'])
    print(_url)
    _headers = {
        # "post": "/repos/amerknane/ameerkn/ameerkn/pulls",
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(data),

    }
    response = requests.get(_url, _headers)

    return response.json()


if __name__ == '__main__':
    data = read_config()
    response = get_pull_requests(data)
    print(response)
