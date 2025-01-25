from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class MarketingAgent():
	"""MarketingAgent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def industry_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['industry_researcher'],
			verbose=True
		)

	@agent
	def trends_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['trends_analyst'],
			verbose=True
		)

	@agent
	def suggest_usecase(self) -> Agent:
		return Agent(
			config=self.agents_config['suggest_usecase'],
			verbose=True
		)
	
	@agent
	def resource_collector(self) -> Agent:
		return Agent(
			config=self.agents_config['resource_collector'],
			verbose=True
		)
	
	@agent
	def genai_solutions(self) -> Agent:
		return Agent(
			config=self.agents_config['genai_solutions'],
			verbose=True
		)
	
	@agent
	def write_edit(self) -> Agent:
		return Agent(
			config=self.agents_config['write_edit'],
			verbose=True
		)
	


	@task
	def industry_researcher_task(self) -> Task:
		return Task(
			config=self.tasks_config['industry_researcher_task'],
		)
	
	@task
	def trends_analyst_task(self) -> Task:
		return Task(
			config=self.tasks_config['trends_analyst_task'],
		)
	
	@task
	def suggest_usecase_task(self) -> Task:
		return Task(
			config=self.tasks_config['suggest_usecase_task'],
		)
	
	@task
	def resource_collector_task(self) -> Task:
		return Task(
			config=self.tasks_config['resource_collector_task'],
			# output_file='report.md'
		)
	
	@task
	def genai_solutions_task(self) -> Task:
		return Task(
			config=self.tasks_config['genai_solutions_task'],
			# output_file='report.md'
		)
	
	@task
	def write_edit_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_edit_task'],
			
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the MarketingAgent crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
