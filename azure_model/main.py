import sys
from crewai import Agent, Task
import os
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import AzureChatOpenAI

load_dotenv()

# 大模型配置
default_llm = AzureChatOpenAI(
    openai_api_version=os.environ.get("AZURE_OPENAI_VERSION", "2023-07-01-preview"),
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt35"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT", "https://<your-endpoint>.openai.azure.com/"),
    api_key=os.environ.get("AZURE_OPENAI_KEY")
)


# 创建研究员代理 
researcher = Agent(
  role='高级研究员',
  goal='探索突破性技术',
  verbose=True,
  llm=default_llm,
  backstory='你充满好奇心，着迷于前沿创新和改变世界的潜力，你对科技了如指掌。'
)

# 研究人员的任务 
research_task = Task(
  description='确定人工智能的下一个大趋势',
  agent=researcher  # 将任务分配给研究人员 
)


# 实例化你的团队 
tech_crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  process=Process.sequential  # 任务将依次执行 
)

# 开始执行任务 
tech_crew.kickoff()
