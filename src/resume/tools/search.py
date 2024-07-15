import requests
import json
import os

from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader

from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)

class SearchTools:
  
  @tool('search tool')
  def search_tool(query: str) -> str:
    """
    Use this tool to search the internet for information. This tools returns 5 results from Google search engine.
    """
    serper_tool = SerperDevTool()
    return serper_tool.run(query)
  
  @tool('scrape tool')
  def scrape_tool(query: str) -> str:
    """
    Use this tool to search webpages. This tools returns 5 results from webpage query.
    """
    scrape_tool = ScrapeWebsiteTool()
    scrape_tool.set_query(query)
    return scrape_tool.run()
  
  @tool('read resume')
  def read_resume():
    """
    Use this tool to read the resume. This tools returns resume for prompt.
    """
  #def read_resume(query:str) -> str:
    # read_resume = FileReadTool(file_path='src/resume/markdowns/resume.md')
    return FileReadTool(file_path='src/resume/markdowns/resume.md')

  @tool('semantic search resume')
  def semantic_search_resume(query: str) -> str:
    """
    Use this tool to search webpages based on resume. This tools returns 5 results from webpage query.
    Useful? - may delete later
    """
  # def semantic_search_resume(query:str) -> str:
    # semantic_search_resume = MDXSearchTool(mdx='src/resume/markdowns/resume.md')
    search_tool = MDXSearchTool(mdx='src/resume/markdowns/resume.md')
    return search_tool.search(query)
  
  
if __name__ == "__main__":
  print(SearchTools.open_page("https://www.python.org/"))
