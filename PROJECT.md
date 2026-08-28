# GitHub Repo Explorer CLI

## Project Overview

Build a terminal-based Python application that lets a user explore public GitHub profiles and repositories by calling the GitHub API.

The project should stay small, understandable, and incremental. The main learning goal is not to build a feature-rich GitHub client. The goal is to learn how a Python program communicates with an external web API, receives JSON data, converts that data into Python objects, and passes those values through multiple cooperating functions.

This project should reinforce existing skills with functions, modular design, validation, lists, dictionaries, loops, and data flow while introducing one primary new layer: HTTP requests and API responses.

## Version 1 Scope

A reasonable Version 1 should support:

- Entering a GitHub username
- Fetching that user's public GitHub profile
- Displaying a small set of useful profile fields
- Fetching the user's public repositories
- Displaying selected repository information
- Searching repositories by name
- Filtering repositories by programming language
- Sorting repositories by a useful metric such as stars
- Handling a username that does not exist
- Handling unsuccessful API responses
- Allowing the user to explore another username without restarting
- Exiting cleanly

Keep Version 1 focused. Do not add authentication, private repositories, GitHub write actions, databases, GUIs, classes, or web frameworks unless a real need emerges later.

## Primary New Concepts

The major new concept is communicating with an external web API.

The learner should come away understanding:

- What an HTTP request is
- What an HTTP response is
- The difference between a response object and the JSON data inside it
- What status codes represent
- How `requests.get()` fits into program flow
- How `.json()` converts response data into normal Python structures
- How to inspect the type and shape of returned API data
- How to handle unsuccessful requests
- How external data moves through the program

Mental model:

terminal input
→ API request
→ HTTP response
→ JSON
→ Python dictionary/list
→ program logic
→ terminal output

## Concepts This Project Reinforces

- Functions
- Arguments and parameters
- Return values
- Caller-to-callee value flow
- Lists and dictionaries
- Nested data
- Loops
- Conditionals
- String normalization
- Searching
- Filtering
- Sorting
- Input validation
- Error handling
- Modular responsibility boundaries
- `main()` as an orchestrator

## Development Progression

### Phase 1 — Learn the API Data Flow

Use `learning.py` for a very small amount of prerequisite practice.

Understand:

- importing `requests`
- making one simple GET request
- inspecting the response object
- reading a status code
- calling `.json()`
- checking whether the parsed result is a dictionary or list

Do not turn `learning.py` into a long curriculum. Move into the real project as soon as the request/response flow makes sense.

### Phase 2 — Fetch One GitHub Profile

Ask the user for a GitHub username and fetch that user's public profile.

Display only a few useful fields at first, such as:

- login
- display name
- public repo count
- followers
- profile URL

Goal: move one value from terminal input into an API request, then extract useful data from the returned dictionary.

### Phase 3 — Handle Failed Requests

Add clean handling for common failure cases:

- nonexistent username
- unexpected status code
- request failure

Goal: understand that API calls do not always succeed and the program should respond predictably.

### Phase 4 — Fetch Public Repositories

Fetch the selected user's public repositories.

Pay close attention to data shape:

- one profile dictionary
- a list of repository dictionaries
- one repository dictionary
- one field inside a repository dictionary

Display only a few fields for each repository, such as:

- repo name
- primary language
- star count
- fork count

### Phase 5 — Search and Filter

Add useful operations over fetched repositories.

Possible features:

- search repo names by partial text
- filter by programming language

Goal: reinforce list processing and helper functions using real external data.

### Phase 6 — Sort Repositories

Allow repositories to be sorted by one useful field, such as star count.

Goal: introduce or reinforce sorting without unnecessary complexity.

### Phase 7 — Build a Simple Menu Loop

Let the user choose actions from a terminal menu.

A possible flow:

- view profile
- view repositories
- search repositories
- filter by language
- sort repositories
- explore another user
- quit

Goal: coordinate the program through a clear high-level loop without allowing `main()` to become overloaded.

## Architecture Philosophy

Do not create a large multi-file architecture before it is needed.

Start with the smallest structure that keeps the code understandable.

If natural boundaries emerge, a later structure might separate:

- terminal interaction and orchestration
- GitHub API access
- repository filtering or sorting logic

Only split files when responsibilities are clearly distinct.

Avoid classes initially. Functions and built-in Python data structures are enough for Version 1.

## Learning Priorities

When functions cooperate, be explicit about:

- what value the caller currently has
- what expression is passed as the argument
- what parameter receives it
- what type and shape the parameter contains
- what the function returns
- what variable receives that returned value

This project should especially reinforce tracing external data across function boundaries.

## Error Handling Scope

Keep error handling realistic but simple.

Version 1 should reasonably handle:

- invalid usernames
- unsuccessful HTTP responses
- basic request failures
- unexpected or missing data when necessary

Do not build an elaborate retry system or production-grade networking layer.

## Out of Scope for Version 1

Avoid adding these unless the core project is complete and there is still a clear learning reason:

- GitHub authentication
- private repositories
- creating or editing GitHub content
- SQLite
- JSON persistence
- GUI
- Flask, FastAPI, or Django
- React or other frontend frameworks
- classes purely for practice
- asynchronous requests
- pagination beyond what is needed for a simple Version 1

## Definition of Success

The project is successful when the learner can explain:

- how a GitHub username becomes part of an API request
- what `requests.get()` returns
- what an HTTP status code represents
- how JSON becomes Python data
- the difference between a response object, a dictionary, a list of dictionaries, and one field
- how profile and repository data move between functions
- how search, filter, and sort functions operate on fetched repository data
- how errors are handled without crashing normal program flow
- why each major function has its assigned responsibility

The project does not need to become a complete GitHub client.

A small, working CLI that clearly demonstrates API data flow is a complete Version 1.
