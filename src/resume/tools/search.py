import requests
import json
import os

from langchain.tools import tool
from langchain_community.document_loaders import WebBaseLoader

from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
#   MDXSearchTool,
  SerperDevTool
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
# read_resume = FileReadTool(file_path='fake_resume.md')
# semantic_search_resume = MDXSearchTool(mdx='./fake_resume.md')




class SearchTools:
  
  @tool('search tool')
  def search_tool(query: str) -> str:
    """
    Use this tool to search the internet for information. This tools returns 5 results from Google search engine.
    """
    return SerperDevTool()
  
  @tool('scrape tool')
  def scrape_tool(query: str) -> str:
    """
    Use this tool to search Instagram. This tools returns 5 results from Instagram pages.
    """
    return ScrapeWebsiteTool()
  
  # @tool('read resume')
  # def read_resume(query:str) -> str:
  #   read_resume = FileReadTool(file_path='./markdowns/resume.md')
  #   return read_resume

   # @tool('semantic search resume')
  # def semantic_search_resume(query:str) -> str:
  #   semantic_search_resume = MDXSearchTool(mdx='./markdowns/resume.md')
  #   return semantic_search_resume
  
  
if __name__ == "__main__":
  print(SearchTools.open_page("https://www.python.org/"))