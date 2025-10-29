import os
import google.generativeai as genai
# from github_utilis import get_commits
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model=genai.GenerativeModel("gemini-2.5-pro")

def get_summary (filename, message, code_changes):
    # commits=get_commits(owner, repo)

    if not code_changes or code_changes=="No Changes Detected":
        return "No Necessary Code Changes Detected."
    
    prompt=f"""
        You are a code reviewer. Summarize the following changes in **{filename}**
        in clear and concise technical language. Focus on what was added, modified, or deleted.

        Commit Message:
        {message}

        Changes:
        {code_changes}
    """

    try:
        response=model.generate_content(prompt)
        summary=response.text if response else "No Summary Generated."
    
    except Exception as e:
        summary= f"Error Generating Summary: {str(e)}"
    
    return summary



    # all_changes = []
    # for commit in commits:
    #     message=commit["message"]
    #     for file in commit["files_changed"]:
    #         filename=file["filename"],
    #         changes=file["code_changes"]

    #         all_changes.append(
    #             f"Commit Message: {message}\n",
    #             f"Filename: {filename}\n",
    #             f"Changes in Code: {changes}"
    #         )
        
    #     if not changes or changes == "No Changes Detected":
    #         print("No Changes Detected")
            
    #     else:
    #         prompt=f"""
    #             You are a code reviewer. Summarize the following changes in **{filename}**
    #             in clear and concise technical language. Focus on what was added, modified, or deleted.

    #             Commit Message:
    #             {message}

    #             Changes:
    #             {changes}
    #         """

    #         response=model.generate_content(prompt)
    #         code_summary=response.text if response else "No Summary Generated."
            



