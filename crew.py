from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task
from agents import llm

# Forming the tech-focused crew with some enhanced configurations

crew=Crew(
  agents=[blog_researcher,blog_writer],
  tasks=[research_task,write_task],
  process=Process.sequential, # Optional : sequential task execution is default
  memory=True,
  cache=True,
  llm=llm,
  max_rpm=100,
  share_crew=True
)

## Task execution with enhanced feedback

result=crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data science'})

print(result)