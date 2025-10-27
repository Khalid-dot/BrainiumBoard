from fastapi import FastAPI
from github_utlis import get_commits

app=FastAPI()

#creating a decorator with "summary" endpoint
@app.get("/summary")
def summary(owner:str, repo:str):
    commits = get_commits(owner,repo)

    return{
        "repository": f"{owner}/{repo}",
        "recent_commit": commits
    }
    