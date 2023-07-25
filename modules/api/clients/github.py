import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    def get_emojis(self):
        r = self.get_emojis_http_response()

        return r.json()

    def get_emojis_http_response(self):
        r = requests.get("https://api.github.com/emojis")

        return r

    def list_commits_http_response(self, owner, repo):
        r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")

        return r

    def list_commits(self, owner, repo):
        r = self.list_commits_http_response(owner, repo)

        return r.json()
