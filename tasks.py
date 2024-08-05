from crewai import Task
from tools import yt_tool
from agents import blog_researcher,blog_writer


# Research Task

research_task=Task(
  description=(
    "Identity the video {topic}"
    "Get detailed information about the video from the channel"
  ),
  expected_output="A Comprehensive 3 paragraph long report based on the {topic} of video content",
  tools=[yt_tool],
  agent=blog_researcher,
)

## Writing Task 

write_task=Task(
  description=(
    "Get the info from the youtube channel on the topic {topic}."
  ),
    expected_output="Summarize the info from the you tube channel video on the topic{topic} and create content for the blog",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,  # Agents will parallely working
    output_file='new-blog-post.md' # Example of output 
)