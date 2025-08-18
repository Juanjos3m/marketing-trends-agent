from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool

@CrewBase
class MarketingTrendsAgent():
    """MarketingTrendsAgent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # ----------------------
    # Definición de agentes
    # ----------------------
    @agent
    def research(self) -> Agent:
        """Agente investigador que busca tendencias"""
        return Agent(
            config=self.agents_config['research'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def writer(self) -> Agent:
        """Agente escritor que redacta el artículo"""
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        """Agente editor que revisa y optimiza el artículo"""
        return Agent(
            config=self.agents_config['editor'],
            verbose=True
        )

    # ----------------------
    # Definición de tareas
    # ----------------------
    @task
    def research_task(self) -> Task:
        """Tarea de investigación"""
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        """Tarea de redacción del artículo"""
        return Task(
            config=self.tasks_config['reporting_task'],
        )

    @task
    def editing_task(self) -> Task:
        """Tarea de edición final del artículo"""
        return Task(
            config=self.tasks_config['editing_task'],
            output_file='Articulo_Final.txt' 
        )

    # ----------------------
    # Crew principal
    # ----------------------
    @crew
    def crew(self) -> Crew:
        """Crea y ejecuta el crew de investigación, redacción y edición"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
