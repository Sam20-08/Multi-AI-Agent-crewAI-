from crewai import Agent
from tools import yt_tool
import os
import os
from dotenv import load_dotenv
from langchain import OpenAI

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Assign the model to the llm variable
llm = OpenAI(
    model_name="gpt-4-0125-preview",
    api_key=api_key,
)

# Creating the blog content researcher 

blog_researcher=Agent(
  role="Blog Researcher from you tube videos",
  goal="Get the relevant video content for the topic {topic} from yt channel",
  verbose=True,
  memory=True,
  backstory=(
    "Expert in understanding videos in AI data science, Machine Learning and Gen AI and providing suggestion"
  ),
  tool=[],
  allow_delegation=True
)

## Create a senior blog content writer with yt tool

blog_writer=Agent(
  role="BLog Writer",
  goal="Narrate compelling tech stories about the video {topic} from YT channel",
  memory=True,
  verbose=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate bringing new"
    "discoveries to light in an accessible manner"
  ),
  tool=[yt_tool],
  llm=llm,
  allow_delegation=False
)