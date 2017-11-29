# How to Contribute

Coderplex web application comprises of two repositories :

* [Coderplex](https://github.com/coderplex/coderplex) : Frontend of the application

* [Coderplex-Backend](https://github.com/coderplex/coderplex-backend) : Backend of the application

## Table Of Contents

- [Code of Conduct](#code-of-conduct)
- [Open Development](#open-development)
- [Branching Model](#branching-model)
- [Development Workflow](#development-workflow)
  - [Work on Issues](#work-on-issues)
  - [Proposing a Change](#proposing-a-change)
  - [Prerequisites](#prerequisites)
  - [Sending a Pull Request](#sending-a-pull-request)
    - [Running Locally](#running-locally)
    - [Docker Deployment in production](#docker-deployment-in-production)
    - [Before submitting](#before-submitting)
    - [Submitting PullRequest](#submitting-pullrequest)
    - [After submitting](#after-submitting)
      - [Received a review request](#received-a-review-request)
  - [How to get in touch](#how-to-get-in-touch)

## Code of Conduct

Coderplex has adopted [Contributor Covenant](https://github.com/coderplex/coderplex/blob/develop/.github/CODE_OF_CONDUCT.md) that we expect project participants to adhere to.

## Open Development

All work related to the application takes place on Github itself. We use [Issues](https://github.com/coderplex/coderplex-backend/issues) to track bugs, discuss ideas and to engage open source contributors. [Projects](https://github.com/coderplex/coderplex-backend/projects) are used to keep track of everything and is our project management tool. We maintain [Wiki](https://github.com/coderplex/coderplex/wiki) for structuring our long term thoughts. Both core team members and contributors sends a pull request which goes through the same review process. Whole process is as transparent as it can be and we strive to keep it that way.

## Branching Model

The `master` branch of coderplex-backend is relatively stable branch which we update for every release. It is highly recommended for both maintainers and contributors to raise a pull request to `develop` branch. Before every release we throughly test develop branch and merge into master.

![Imgur](https://i.imgur.com/KPO2dLul.png)

_A pull request to any other branch may most likely be closed by our bots_.

## Development Workflow

We welcome pull requests from beginners and django developers alike!

### Work on Issues

1. Find an issue that needs assistance by searching for the [open issues](https://github.com/coderplex/coderplex-backend/labels/help wanted).
1. If you decide to fix an issue, please be sure to check the comment thread in case somebody is already working on a fix. If nobody is working on it at the moment, please leave a comment stating that you intend to work on it so other people don’t accidentally duplicate your effort.
1. If somebody claims an issue but doesn’t follow up for more than a weeks, it’s fine to take over it but you should still leave a comment.

### Proposing a Change

1. Open a new issue if you would like report a bug or suggest improvements.
1. Follow this [Issue Template](https://github.com/coderplex/coderplex-backend/blob/develop/.github/ISSUE_TEMPLATE.md)
1. Please wait for core team members to comment on the thread. This lets us reach an agreement on your proposal before you put significant effort into it.

### Prerequisites

1. [Python](https://www.python.org)

   * Minimum version 3.5+

   ```bash
   # To check python version
   python3 -V
   ```

1. [VirtualEnv](https://virtualenv.pypa.io/en/stable/)

   * Installing instructions are at [official docs](https://virtualenv.pypa.io/en/stable/installation/).   

1. [Git](https://git-scm.com/download/linux) (Familiarity with git is mandatory).

### Sending a Pull Request

*Working on your first Pull Request? You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)*

#### Running Locally

1. Fork the [repository](https://github.com/coderplex/coderplex-backend).
1. Then clone your forked repository
   ```bash
    git clone <your forked repository url>
   ```
1. Move to the repository's root folder
   ```bash
    cd coderplex-backend
   ```
1. Create a virtual environment
   ```bash
    virtualenv -p python3 venv
   ```
1. Activate venv
   ```bash
    source venv/bin/activate
   ```   
1. Install the requirements
   ```bash
    pip install -r requirements/requirements.txt
   ```
1. Add an environment variable `EMAIL_HOST_USER`
   ```bash
    echo "export EMAIL_HOST_USER=<your email>" >> ~/.bashrc
   ```
1. Add an environment variable `EMAIL_HOST_PASSWORD`
   ```bash
    echo "export EMAIL_HOST_PASSWORD=<your email password>" >> ~/.bashrc
   ```
1. Open new terminal session
   ```bash
    source ~/.bashrc
   ```
1. Run the migrations
    ```bash
    python webapp/manage.py makemigrations
    python webapp/manage.py migrate
   ```   
1. Create a SuperUser
    ```bash
    python webapp/manage.py createsuperuser
   ```
1. Run the Fixtures for adding Social Applications
    ```bash
    python webapp/manage.py loaddata authentication/fixtures/social_applications.json
   ```   
1. Start the development server
   ```bash
    python webapp/manage.py runserver
   ```   
   You can now open the App at `localhost:8000` in your browser
1. You can see all the implemented APIs in [API.md](../API.md)
    
#### For Production (Contributors can ignore this)
1. Change `client_id` and `client_secret` of social applications
1. Add environment variables `GITHUB_CALLBACK_URL` and `LINKEDIN_CALLBACK_URL` and set those with `<base_url> + "/callback"`
1. Docker build
   ```bash
    docker build -t production --build-arg build_env="production" -f Dockerfile .
   ```
1. Docker run
   ```bash
    docker run --name coderplex-production  -d -p 8000:8000 production
   ```   

#### Before submitting

1. From your fork, create a [branch](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/) and name it. eg. `typo-in-readme`
1. If you have added any new packages, you should add those in requirements
    ```bash
    pip freeze > requirements/requirements.txt
    ```
1. Remove the local `sqlite` database
    ```bash
    rm webapp/coderplex_apis/db.sqlite3
    ```
1. Run the migrations
    ```bash
    python webapp/manage.py makemigrations
    python webapp/manage.py migrate
    ```    
1. If you’ve fixed a bug or added code that should be tested, add tests!
1. Ensure that all tests pass
   ```bash
    python webapp/manage.py test
   ```
1. Add and commit your code. Please give meaningful commit messages.

#### Submitting PullRequest

1. Pull latest code from [upstream repository's](https://help.github.com/articles/merging-an-upstream-repository-into-your-fork/)`develop`, if in case anything new were merged while you were working on your fork.
1. Push the code to your fork.
1. Raise the pull request from your created branch to `develop` branch of coderplex. [why develop instead of master branch?](https://www.atlassian.com/git/tutorials/comparing-workflows)
1. Take some time to give a brief description of the work you have done.
1. Follow the [Pull Request Template](https://github.com/coderplex/coderplex-backend/blob/develop/.github/PULL_REQUEST_TEMPLATE.md)

#### After submitting

1. The core team will review your pull request and either merge it, request changes to it, or close it with an explanation.

##### Received a review request

* Work on the requested changes
* Push the changes as you did earlier, the pull request will automatically catch those and update itself.

### How to get in touch

* Coderplex [Discord Channel](https://discord.gg/dVnQ2Gf)