import streamlit as st
from moviepy.editor import AudioFileClip

def main():
    st.title("Promotoria de Justiça de Piracicaba")
    st.subheader('Audiências  >>>  mp3')
    st.text("by Pimentel - 2024")
    
    # Upload do arquivo de vídeo
    uploaded_file = st.file_uploader("Carregue o arquivo da audiência:", type=['mp4', 'mov', 'avi', 'mkv', 'webm', 'asf'])
    if uploaded_file is not None:
        # Configurações para o arquivo de saída
        audio_file_name = "audio_output.mp3"
        
        if st.button("Extrair Áudio"):
            video_path = uploaded_file.name
            st.text('Por favor, aguarde...')
            # Grava o arquivo de vídeo temporário
            with open(video_path, "wb") as f:
                f.write(uploaded_file.getvalue())
            
            audio = AudioFileClip(video_path)
            # Especificar que o formato de saída é mp3
            audio.write_audiofile(audio_file_name, codec='mp3', bitrate="192k")
            audio.close()
            
            # Disponibilizar o download do arquivo de áudio
            with open(audio_file_name, "rb") as f:
                btn = st.download_button(
                    label="Baixar arquivo de áudio",
                    data=f,
                    file_name=audio_file_name,
                    mime='audio/mpeg'
                )
                
if __name__ == '__main__':
    main()
