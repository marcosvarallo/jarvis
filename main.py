from intent_router import detect_intention
from ai_core import generate_ia_response
from services import agenda, email, music
from speech_output import speak

def main():
    print("Hi, I'm FRIDAY. How can I help?")
    while True:
        entry = input("You: ")

        if entry.lower() in ["sair", "exit", "quit"]:
            print("FRIDAY: See you later!")
            break

        tipo, dados = detect_intention(entry)

        if tipo == "agenda":
            response = agenda.check_agenda(dados)
        elif tipo == "email":
            response = email.send_email(dados)
        elif tipo == "music":
            response = music.play_music(dados)
        elif tipo == "ia":
            response = generate_ia_response(entry)
        else:
            response = "Sorry, I didn't understand that."

        print(f"FRIDAY: {response}")
        speak(response)

if __name__ == "__main__":
    main()
