from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks

from dotenv import load_dotenv
load_dotenv()

class FinancialCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = StockAnalysisAgents() # 代理
    tasks = StockAnalysisTasks() # 任务

    # 代理
    research_analyst_agent = agents.research_analyst()
    financial_analyst_agent = agents.financial_analyst()
    investment_advisor_agent = agents.investment_advisor()

    # 任务
    research_task = tasks.research(research_analyst_agent, self.company) # 研究人员
    financial_task = tasks.financial_analysis(financial_analyst_agent) # 财务分析师
    filings_task = tasks.filings_analysis(financial_analyst_agent) # 文件审查员
    recommend_task = tasks.recommend(investment_advisor_agent) # 投资建议

    # 实例化你的团队
    crew = Crew(
      agents=[
        research_analyst_agent,
        financial_analyst_agent,
        investment_advisor_agent
      ],
      tasks=[
        research_task,
        financial_task,
        filings_task,
        recommend_task
      ],
      verbose=True
    )

    # 开始执行任务
    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## 欢迎使用基于AI的财务分析团队")
  print('-------------------------------')
  company = input(
    dedent("""
     你想分析的公司是什么？ 
    """))
  
  financial_crew = FinancialCrew(company)
  result = financial_crew.run()
  print("\n\n########################")
  print("## 以下是报告:")
  print("########################\n")
  print(result)
