from crewai import Task
from textwrap import dedent

# 股票分析任务
class StockAnalysisTasks():

  # 研究任务
  def research(self, agent, company):
    return Task(description=dedent(f"""
        收集并总结与股票及其行业相关的最新新闻文章、新闻稿和市场分析。 
        特别关注任何重大事件、市场情绪和分析师的观点。还包括即将发生的事件，如收益等。 
  
        您的最终答案必须是一份报告，其中包括最新消息的全面摘要、市场情绪的
        任何显著变化以及对股票的潜在影响。
        另外，请务必返回股票行情。 
        
        {self.__tip_section()}
  
        确保尽可能使用最新的数据。 
  
        客户选择的公司是: {company}
      """),
      agent=agent # 将任务分配给研究人员
    )
   
  # 金融分析任务 
  def financial_analysis(self, agent): 
    return Task(description=dedent(f"""
        对股票的财务状况和市场表现进行全面分析。
        这包括检查关键财务指标，例如
        市盈率、每股收益增长、收入趋势和
        债务权益比。
        此外，分析股票的表现，并与
        同行业同行和整体市场趋势进行比较。 

        你的最终报告必须扩展所提供的摘要，但现在包括对股票的财务状况，
        优势和劣势，以及在当前市场情况下与竞争对手的表现的明确评估。
        {self.__tip_section()}

        确保尽可能使用最新的数据。 
      """),
      agent=agent
    )

  # 文件分析任务
  def filings_analysis(self, agent):
    return Task(description=dedent(f"""
        分析 EDGAR 针对相关股票的最新 10-Q 和 10-K 文件。
        重点关注关键部分，例如管理层讨论和分析、财务报表、内幕交易活动和任何披露的风险。
        提取可能影响股票未来表现的相关数据和见解。 

        您的最终答复必须是一份扩展报告，其中还应重点介绍这些文件中的
        重要发现，包括对您的客户而言的任何危险信号或积极指标。 
        {self.__tip_section()}        
      """),
      agent=agent
    )

  # 推荐任务
  def recommend(self, agent):
    return Task(description=dedent(f"""
        审查并综合财务分析师和研究人员提供的分析。
        将这些见解结合起来，形成全面的投资建议。 
        
        您必须考虑所有方面，包括财务状况、市场情绪和来自 EDGAR 文件的定性数据。 

        确保包含显示内幕交易活动和即将发生的事件（如收益）的部分。 

        您的最终答案必须是对您的
        客户的建议。它应该是一份完整的超详细报告，提供
        明确的投资立场和策略以及支持证据。
        使其为您的客户美观且格式良好。 
        {self.__tip_section()}
      """),
      agent=agent
    )

  def __tip_section(self):
    return "如果你做出了最好的工作，我会给你10,000美元的佣金！"
