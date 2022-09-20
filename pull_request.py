import json

_url = "https://api.github.com/repos/amerknane/ameerkn/pulls"

_headers = {
    # "post": "/repos/amerknane/ameerkn/ameerkn/pulls",
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer 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",

}
# _d={
# "title":"Amazing new feature",
# "body":"Please pull these awesome changes in!",
# "head":"octocat:new-feature",
# "base":"master"
# }
import requests


response = requests.get(_url,_headers)
print(response.json())
