import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("olhafedak")

    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    print(r)

    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergiibutenko_repo_non_exist")

    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")

    assert r["total_count"] != 0


@pytest.mark.api
def test_get_emojis_status_code(github_api):
    r = github_api.get_emojis_http_response()

    assert r.status_code == 200


@pytest.mark.api
def test_emojis_contains_1st_place_medal(github_api):
    r = github_api.get_emojis()

    assert "1st_place_medal" in r


@pytest.mark.api
def test_get_emojis_proper_url(github_api):
    r = github_api.get_emojis()

    assert (
        r["1st_place_medal"]
        == "https://github.githubassets.com/images/icons/emoji/unicode/1f947.png?v8"
    )


@pytest.mark.api
def test_list_commits_status_code(github_api):
    r = github_api.list_commits_http_response("Oltsya", "QAAuto2.0")

    assert r.status_code == 200


@pytest.mark.api
def test_list_commits_check_existence(github_api):
    r = github_api.list_commits("Oltsya", "QAAuto2.0")

    assert len(r) > 0


@pytest.mark.api
def test_list_commits_check_author(github_api):
    r = github_api.list_commits("Oltsya", "QAAuto2.0")

    assert r[0]["commit"]["author"]["name"] == "Olha Fedak"


@pytest.mark.api
def test_list_commits_check_comitter_email(github_api):
    r = github_api.list_commits("Oltsya", "QAAuto2.0")

    assert r[0]["commit"]["committer"]["email"] == "onyskivo@gmail.com"
