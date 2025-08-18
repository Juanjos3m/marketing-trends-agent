import streamlit as st
from ui import render_header, render_timeline
from logic import ejecutar_investigacion

# Configuración de página
st.set_page_config(page_title="Marketing Trends Agent", page_icon="📊", layout="wide")

# Cabecera
render_header()

# Timeline
render_timeline()

# Ejecución
st.subheader("🎯 Ejecutar un nuevo análisis")
topic = st.text_input("Tema a investigar", "Content Marketing")

if st.button("Ejecutar investigación"):
    with st.spinner("Ejecutando agentes... esto puede tardar unos minutos ⏳"):
        article = ejecutar_investigacion(topic)

    st.success("✅ Proceso completado")
    st.markdown("### 📄 Artículo Final")
    st.write(article)

    st.download_button(
        "📥 Descargar artículo",
        data=article,
        file_name="articulo_marketing.txt",
        mime="text/plain"
    )
