#  Marketing Trends Agent

Un proyecto basado en **CrewAI** que investiga, redacta y edita automáticamente un artículo estratégico sobre las últimas tendencias de **Content Marketing (2024–2025)**, utilizando agentes inteligentes y modelos LLM open source.

---

##  Descripción

Este proyecto implementa un **flujo de tres agentes** que trabajan de forma colaborativa:

1. **Research Agent**  
   - Investiga rigurosamente las tendencias más recientes en *Content Marketing*.  
   - Reúne entre 8 y 12 tendencias con ejemplos globales, quick wins y fuentes verificables.

2. **Writer Agent**  
   - Convierte la investigación en un **artículo estratégico y narrativo** para CMOs y líderes de marketing.  
   - Redacta en español neutro, con estructura clara (introducción, tendencias, tácticas, checklist, roadmap, conclusión).

3. **Editor Agent**  
   - Revisa el artículo borrador, lo mejora en claridad, tono y fluidez.  
   - Asegura que cumpla con el estilo profesional y lo guarda como versión final en `Artículo_Final.md`.

---

##  Instalación
- git clone https://github.com/Juanjos3m/marketing-trends-agent.git
- cd marketing-trends-agent
- python -m venv .venv
- .venv\Scripts\activate
- pip install uv
- uv pip install -e .
- crewai run

---

##  Autor
Proyecto desarrollado por Juan José Muñoz.
