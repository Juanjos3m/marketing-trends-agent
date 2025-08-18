from src.marketing_trends_agent.crew import MarketingTrendsAgent

def ejecutar_investigacion(topic: str) -> str:
    """Ejecuta el crew de agentes y devuelve el artículo final en texto limpio"""

    crew_instance = MarketingTrendsAgent()
    result = crew_instance.crew().kickoff(inputs={"topic": topic})

    # Intentar extraer el artículo final
    try:
        article = result['tasks_output'][-1].raw  # si es dict
    except:
        article = result.tasks_output[-1].raw     # si es objeto

    return article
