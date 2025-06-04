
import streamlit as st
import openai

# Configura tu clave de API
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Generador de Historias de Usuario con IA", layout="centered")
st.title("🤖 Generador de Historias de Usuario con IA")
st.markdown("Este asistente transforma requerimientos en historias de usuario automáticamente.")

# Entrada del requerimiento
requerimiento = st.text_area("✍️ Ingresa tu requerimiento de software:", height=200)

# Opcional: seleccionar rol del usuario (para enriquecer prompt)
rol = st.selectbox("¿Qué rol tiene el usuario que solicita esto?", ["Líder funcional", "Product Owner", "Usuario final", "Desarrollador", "Otro"])

# Botón para generar historia
if st.button("Generar Historia de Usuario"):
    if requerimiento.strip() == "":
        st.warning("Por favor ingresa un requerimiento para continuar.")
    else:
        with st.spinner("Generando historia de usuario con IA..."):
            prompt = f"""
Eres un analista experto en requerimientos ágiles. Conviértelo en una historia de usuario clara y con criterios de aceptación.

Rol: {rol}

Requerimiento: {requerimiento}

Devuelve solo:
1. Historia de Usuario (Yo como... quiero... para...)
2. Lista de 3 o más Criterios de Aceptación numerados
"""

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Eres un experto en análisis funcional y metodologías ágiles."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.4,
                max_tokens=500
            )

            respuesta = response.choices[0].message.content
            st.success("✅ Historia generada correctamente")
            st.markdown(respuesta)

st.markdown("---")
st.markdown("Desarrollado por [Tu Nombre] | Proyecto de curso IA 💡")
