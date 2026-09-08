# GitHub Repo Explorer

A learning-focused Python terminal application that retrieves public GitHub
profile and repository data through the GitHub REST API.

## Current Features

- Accepts a GitHub username from terminal input
- Fetches and displays public profile information
- Fetches and displays public repositories
- Shows each repository's name, primary language, stars, and forks
- Searches repository names using case-insensitive partial matching
- Includes reusable case-insensitive language-filtering logic
- Handles nonexistent users, unexpected HTTP statuses, and request failures

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Requests:

```bash
python -m pip install requests
```

## Run

```bash
python main.py
```

Enter a public GitHub username when prompted. After showing the profile and
repository information, the program asks for a repository name to search for.

## Project Structure

- `main.py`: API requests, display helpers, repository operations, and program
  orchestration
- `learning.py`: small request/response learning exercise
- `PROJECT.md`: project scope and learning goals
- `LEARNING_STYLE.md`: preferred learning and collaboration approach
- `LEARNING_HANDOFF.md`: prior Python experience and completed concepts

## Scope

This project intentionally uses public, unauthenticated GitHub data. It does
not access private repositories or perform GitHub write actions. The repository
request uses GitHub's default first page of results.
