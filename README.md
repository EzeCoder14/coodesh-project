# Coodash Project

A simple FastAPI service that acts as a proxy to third-party integrations like Salesforce and UPS.

## Features

- Unified endpoint `/integrate/{provider}`
- Normalized JSON output
- Mocked third-party providers
- Graceful error handling
- Extensible provider handler logic
- API Key, Basic, and Bearer token auth support
- Includes unit test

## Tech Stack

- FastAPI
- Pydantic
- Pytest

## Setup

```bash
git clone https://github.com/EzeCoder14/coodesh-project.git
cd automation_proxy
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test
```bash
pytest
```


## Repository Readme

- It should contain the project title
- A one-sentence description about the project
- It should include a list of languages, frameworks, and/or technologies used
- How to install and use the project (instructions)
- Don’t forget the .gitignore
- If you are using a personal GitHub, mention that it is a challenge by Coodesh:

> This is a challenge by Coodesh

## Completion and Submission Instructions
1. Add the link to the repository with your solution to the task on the platform
2. Check if the Readme is good and make the final commit to your repository
3. Submit and wait for further instructions. If the test requires a video presentation, it will be possible to record it on the submission screen after adding the repository link. Good luck and success! =)

## Support

For questions about the process, send a message directly to a specialist in the platform chat.
