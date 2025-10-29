import os #for importing enviorment variables from your system, interact with OS
import requests #for handing HTTP requests
from dotenv import load_dotenv #load variables from the .env file
from code_summary import get_summary

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
    for commit in commits[:3]:#takes the last 5 commits only

        sha=commit["sha"]

        commit_url= f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"

        detailed_response=requests.get(commit_url, headers=HEADERS).json()

        branch_url=commit_url= f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}/branches-where-head"
        branch_resp=requests.get(branch_url, headers=HEADERS).json()
        branch_name=branch_resp[0]["name"] if branch_resp else None

        for f in detailed_response.get("files", []):
            filename= f["filename"]
            code_changes= f.get("patch","No Changes Detected")
            message= commit["commit"]["message"],

            summary=get_summary(filename, message, code_changes)

        files_changed=[
            {
                "filename": filename,
                "branch": branch_name,
                "status": f["status"],
                "additions": f["additions"],
                "deletions": f["deletions"],
                "changes": f["changes"],
                "summary": summary
            }
        ]

        commit_data.append({
            "author": commit["commit"]["author"]["name"],
            "message": message,
            "date": commit["commit"]["author"]["date"],
            "url": commit["html_url"],
            "files_changed": files_changed,
        })
    return commit_data