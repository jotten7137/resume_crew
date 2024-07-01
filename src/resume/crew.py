from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from resume.tools.search import SearchTools

# Uncomment the following line to use an example of a custom tool
# from resume.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class ResumeCrew:
    """Resume crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    #Agents
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[
              SearchTools.search_tool,
              SearchTools.scrape_tool,
            ],
            verbose=True,
        )
    
    @agent
    def profiler(self) -> Agent:
        return Agent(
            config=self.agents_config["profiler"],
            tools=[
              SearchTools.search_tool,
              SearchTools.scrape_tool,
            ],
            verbose=True,
        )
    
    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_strategist"],
            tools = [
              SearchTools.search_tool,
              SearchTools.scrape_tool,
              SearchTools.read_resume, 
              SearchTools.semantic_search_resume],
            verbose=True,
            
        )
    
    @agent
    def interview_preparer(self) -> Agent:
        return Agent(
            config=self.agents_config["interview_preparer"],
            tools = [
              SearchTools.search_tool,
              SearchTools.scrape_tool,
              SearchTools.read_resume, 
              SearchTools.semantic_search_resume],
            verbose=True,
        )
    
    #Tasks
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research"],
            agent=self.researcher(),
        )
    
    @task
    def profile_task(self) -> Task:
        return Task(
            config=self.tasks_config["profile"],
            agent=self.profiler(),
        )
    
    @task
    def resume_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["resume_strategy"],
            agent=self.resume_strategist(),
            output_file="src/resume/markdowns/tailored_resume.md",
        )
    
    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config=self.tasks_config["interview_preparation"],
            agent=self.interview_preparer(),
            output_file="src/resume/markdowns/interview_materials.md",
        )
    
    #Crew
    @crew
    def crew(self) -> Crew:
        """Creates the Instagram crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )