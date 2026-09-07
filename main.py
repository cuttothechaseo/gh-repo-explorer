import requests


def display_profile(profile_data):
    print(f"Login: {profile_data['login']}")
    print(f"Name: {profile_data['name']}")
    print(f"Public Repos: {profile_data['public_repos']}")
    print(f"Followers: {profile_data['followers']}")
    print(f"URL: {profile_data['html_url']}")


username = input("Input a Github username:")

try:
    profile_response = requests.get(
        f"https://api.github.com/users/{username}", timeout=10
    )
    profile_data = profile_response.json()
    if profile_response.status_code == 200:
        display_profile(profile_data)
        repositories_response = requests.get(
            f"https://api.github.com/users/{username}/repos", timeout=10
        )
        repositories = repositories_response.json()
        if repositories_response.status_code == 200:
            print("Repositories:")
            for repository in repositories:
                print(f"Name: {repository['name']}")
                print(f"Language: {repository['language']}")
                print(f"Stars: {repository['stargazers_count']}")
                print(f"Forks: {repository['forks_count']}")
                print("")
        else:
            print(f"Could not fetch repositories. {repositories_response.status_code}")

    elif profile_response.status_code == 404:
        print("Github user not found.")
    else:
        print(f"Unexpected response status: {profile_response.status_code}")
except requests.exceptions.RequestException:
    print("Request failed. Please check your connection and try again.")
