from crewai import Agent

from tools.browser_tools import BrowserTools
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.sec_tools import SECTools

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool

import os
from langchain_openai import AzureChatOpenAI

from dotenv import load_dotenv
load_dotenv()

# 大模型配置
default_llm = AzureChatOpenAI(
    openai_api_version=os.environ.get("AZURE_OPENAI_VERSION", "2023-07-01-preview"),
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "gpt35"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT", "https://<your-endpoint>.openai.azure.com/"),
    api_key=os.environ.get("AZURE_OPENAI_KEY")
)

class StockAnalysisAgents():
  
  # 创建财务分析师代理
  def financial_analyst(self):
    return Agent(
      role='最优秀的财务分析师',
      goal="""用你的财务数据和市场趋势分析打动所有客户""",
      backstory="""最有经验的财务分析师，在股票市场分析和投资策略方面拥有丰富的专业知识，正在为一位非常重要的客户工作。""",
      verbose=True,
      llm=default_llm,
      tools=[
        BrowserTools.scrape_and_summarize_website, # 负责抓取并总结网站内容
        SearchTools.search_internet, # 负责搜索互联网内容
        CalculatorTools.calculate, # 负责计算
        SECTools.search_10q, # 查询10q资料 10-Q 是一份季度报告，提供公司在每个财务季度（前三个季度）的财务状况和经营成果
        SECTools.search_10k # 查询10k资料 10-K 是一份年度报告，详细描述公司的财务状况和经营业绩
      ]
    )

  # 职员研究人员 
  def research_analyst(self):
    return Agent(
      role='最优秀的研究人员',
      goal="""善于收集、解读数据并让客户惊叹""",
      backstory="""你被称为最优秀的研究人员，擅长筛选新闻、公司公告和市场情绪。现在，你正在为一位超级重要的客户工作""",
      verbose=True,
      llm=default_llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news, # 收集新闻
        YahooFinanceNewsTool(), # 雅虎财经新闻
        SECTools.search_10q,
        SECTools.search_10k
      ]
  )

  # 私人投资顾问
  def investment_advisor(self):
    return Agent(
      role='私人投资顾问',
      goal="""通过全面的股票分析和更完善的投资建议给您的客户留下深刻印象""",
      backstory="""您是最有经验的投资顾问，您结合各种分析见解来制定战略投资建议。您现在正在为一位您需要打动的超级重要客户工作。""",
      verbose=True,
      llm=default_llm,
      tools=[
        BrowserTools.scrape_and_summarize_website,
        SearchTools.search_internet,
        SearchTools.search_news,
        CalculatorTools.calculate,
        YahooFinanceNewsTool()
      ]
    )
