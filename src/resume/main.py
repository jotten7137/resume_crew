#!/usr/bin/env python
from resume.crew import ResumeCrew
import datetime

from crewai_tools import (
  FileReadTool,
  MDXSearchTool,
)
job_input = input('Enter target job application url here: ')
#'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
github_input = input("Enter your github account [i.e. https://github.com/xxxxx]: ")
#'github_url': 'https://github.com/jotten7137',

writeup_input = input("Enter a brief writeup about your background, experience, speciality, skills, education, etc.: ")
# 'personal_writeup': """Noah is an accomplished Software
#         Engineering Leader with 18 years of experience, specializing in
#         managing remote and in-office teams, and expert in multiple
#         programming languages and frameworks. He holds an MBA and a strong
#         background in AI and data science. Noah has successfully led
#         major tech initiatives and startups, proving his ability to drive
#         innovation and growth in the tech industry. Ideal for leadership
#         roles that require a strategic and innovative approach."""

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'read_resume' : FileReadTool(file_path='src/resume/markdowns//markdowns/resume.md'),
        'semantic_search_resume' : MDXSearchTool(mdx='src/resume/markdowns/resume.md'),
        'job_posting_url': job_input,
        'github_url': "https://github.com/" + github_input,
        'personal_writeup': writeup_input
        }
    
    ResumeCrew().crew().kickoff(inputs=inputs)

    from IPython.display import Markdown, display
    display(Markdown("src/resume/markdowns/tailored_resume.md"))

    display(Markdown("src/resume/markdowns/interview_materials.md"))