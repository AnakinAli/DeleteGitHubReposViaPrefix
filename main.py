from github import Github
from decouple import config

g = Github(config("GITHUB_TOKEN"))
PREFIXES = ["Spravka","Platform","School","dasdas"]

# Delete repos
def task():
    for repo in g.get_user().get_repos():
        for PREFIX in PREFIXES:
            if PREFIX in repo.name:
                print(repo.name)
                repo.delete()

while True:
    try:
        task()
    except:
        print("Error")


print("Successfully deleted the repos!")
