import requests
import time
from colorama import init, Fore
import os

init()

os.system("pip install colorama art")
time.sleep(3)
os.system('cls')
git = "ItsPyDevs"
print(Fore.RED + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def get_user_repos(owner):
    url = f"https://api.github.com/users/{owner}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos_data = response.json()
        repos = [repo_data['name'] for repo_data in repos_data]
        return repos
    else:
        return None

def get_github_repo_stats(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    if response.status_code == 200:
        repo_data = response.json()
        stargazers_count = repo_data['stargazers_count']
        forks_count = repo_data['forks_count']
        watchers_count = repo_data['watchers_count']
        open_issues_count = repo_data['open_issues_count']
        return stargazers_count, forks_count, watchers_count, open_issues_count
    else:
        return None

def display_stats(owner, repo):
    while True:
        stats = get_github_repo_stats(owner, repo)
        if stats is not None:
            stargazers_count, forks_count, watchers_count, open_issues_count = stats
            os.system('cls')
            print(f"stats du repo: {repo}")
            print(Fore.RESET + "---------")
            print(Fore.YELLOW + "Stargazers:", stargazers_count)
            print(Fore.GREEN + "Forks:", forks_count)
            print(Fore.MAGENTA + "Vues:", watchers_count)
            print(Fore.RED + "Problèmes:", open_issues_count)
            print(Fore.RESET + "---------")
        else:
            print(Fore.RED + "AUCUN REPO")
        time.sleep(30)

def main():
    print(Fore.BLUE + "Bienvenue dans le GitLive")
    print(Fore.RESET)
    owner = input("Veuillez entrer le nom du propriétaire du repo: ")
    repos = get_user_repos(owner)

    if repos is not None:
        os.system("cls")
        print(Fore.CYAN + f"Voici les repo de l'utilisateur {owner}:")
        print(Fore.RESET)
        for repo in repos:
            print(repo)
        print()
        repo = input(Fore.BLUE + "Veuillez entrer le nom du repo: ")
        display_stats(owner, repo)
    else:
        print(Fore.RED + "AUCUN REPO")

if git != "ItsPyDevs":
    print('INJECTING RAT IN YOUR SYSTEM')
    time.sleep(9999)
else:
    main()
