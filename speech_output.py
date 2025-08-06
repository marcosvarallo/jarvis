from gtts import gTTS
import os
import tempfile
import platform


def speak(texto: str, idioma="pt"):
    try:

        tts = gTTS(text=texto, lang=idioma)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            caminho_audio = fp.name

        if platform.system() == "Windows":
            os.system(f'start /min wmplayer /play /close "{caminho_audio}"')
        else:
            os.system(f"mpg123 {caminho_audio}")

    except Exception as e:
        print(f"[Erro no TTS] {e}")
