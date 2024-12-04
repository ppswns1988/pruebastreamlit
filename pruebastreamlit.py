import streamlit as st

def main():
    # Título de la aplicación
    st.title("Mi Aplicación en Streamlit con Audio")

    # Descripción
    st.write("Explora esta sencilla aplicación con un reproductor de audio.")

    # Entrada de texto
    nombre = st.text_input("¿Cómo te llamas?", "")

    # Botón
    if st.button("Saludar"):
        if nombre:
            st.success(f"¡Hola, {nombre}! Bienvenido/a a mi aplicación.")
        else:
            st.warning("Por favor, introduce tu nombre.")

    # Reproductor de audio
    st.write("Reproductor de audio:")
    audio_file = st.file_uploader("Sube un archivo de audio (MP3, WAV)", type=["mp3", "wav"])
    if audio_file is not None:
        st.audio(audio_file, format="audio/mp3")
        st.success("Reproduciendo audio.")

if __name__ == "__main__":
    main()