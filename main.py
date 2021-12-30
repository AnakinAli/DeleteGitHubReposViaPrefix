from github import Github
from decouple import config

g = Github(config("GITHUB_TOKEN"))
PREFIX = "Spravka"

# Delete repos
for repo in g.get_user().get_repos():
    if PREFIX in repo.name:
        repo.delete()

print("Successfully deleted the repos!")
