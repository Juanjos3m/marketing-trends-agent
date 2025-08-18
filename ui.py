import streamlit as st

def render_header():
    st.title("📊 Marketing Trends Agent")
    st.markdown(
        "Un asistente ejecutivo para la **investigación, redacción y edición** de tendencias de marketing."
    )
    st.divider()

def render_timeline():
    st.markdown("## 🔄 Flujo de trabajo de los agentes")

    st.markdown(
        """
        <style>
        .timeline {
            position: relative;
            margin: 20px 0;
            padding-left: 35px;
            border-left: 3px solid #2563EB; /* Azul corporativo */
        }
        .timeline-step {
            position: relative;
            margin-bottom: 45px;
            padding-left: 25px;
        }
        .timeline-step::before {
            content: '';
            position: absolute;
            left: -14px;
            top: 5px;
            width: 18px;
            height: 18px;
            background-color: #111827; /* fondo oscuro */
            border: 3px solid #2563EB; /* azul corporativo */
            border-radius: 50%;
        }
        .timeline-step h4 {
            margin: 0;
            font-size: 18px;
            font-weight: 700;
            color: #F3F4F6; /* gris muy claro, casi blanco */
        }
        .timeline-step p {
            margin: 6px 0 0 0;
            font-size: 14px;
            line-height: 1.6;
            color: #D1D5DB; /* gris claro elegante */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Contenido sin emojis, más ejecutivo
    st.markdown(
        """
        <div class="timeline">
            <div class="timeline-step">
                <h4>Research Agent</h4>
                <p>Analiza rigurosamente tendencias del mercado y recopila información validada de múltiples fuentes.</p>
            </div>
            <div class="timeline-step">
                <h4>Writer Agent</h4>
                <p>Transforma la investigación en un artículo estratégico, narrativo y con visión ejecutiva.</p>
            </div>
            <div class="timeline-step">
                <h4>Editor Agent</h4>
                <p>Optimiza el contenido final, asegurando precisión, claridad y estilo profesional.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )