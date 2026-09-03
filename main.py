import requests

username = input("Input a Github username:")

try:
    profile_response = requests.get(
        f"https://api.github.com/users/{username}", timeout=10
    )
    profile_data = profile_response.json()
    if profile_response.status_code == 200:
        print(f"Login: {profile_data['login']}")
        print(f"Name: {profile_data['name']}")
        print(f"Public Repos: {profile_data['public_repos']}")
        print(f"Followers: {profile_data['followers']}")
        print(f"URL: {profile_data['html_url']}")
    elif profile_response.status_code == 404:
        print("Github user not found.")
    else:
        print(f"Unexpected response status: {profile_response.status_code}")
except requests.exceptions.RequestException:
    print("Request failed. Please check your connection and try again.")
