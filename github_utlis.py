import os #for importing enviorment variables from your system, interact with OS
import requests #for handing HTTP requests
from dotenv import load_dotenv #load variables from the .env file

load_dotenv()
GitHub_Token = os.getenv('GITHUB_TOKEN')

HEADERS={
    "Authorization": f"token {GitHub_Token}",
    "Accept": "application/vnd.github.v3+json",
}

def get_commits(owner, repo):
    url= f"https://api.github.com/repos/{owner}/{repo}/commits"
    
    #Sends a GET request to GitHub with your authentication headers.
    response=requests.get(url, headers=HEADERS)

    # converts tha API response from JSON into python dictionary
    commits=response.json()

    commit_data=[]
    for commit in commits[:10]:#takes the last 10 commits only
        commit_data.append({
            "author": commit["commit"]["author"]["name"],
            "message": commit["commit"]["message"],
            "data": commit["commit"]["author"]["date"],
            "url": commit["html_url"]
        })
    return commit_data