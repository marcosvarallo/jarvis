from datetime import datetime


def check_agenda(dados: dict = None) -> str:
    hoje = datetime.now().strftime("%d/%m/%Y")

    compromissos = [
        {"hora": "09:00", "descricao": "Reunião com o time"},
        {"hora": "14:30", "descricao": "Revisar pull requests"},
        {"hora": "17:00", "descricao": "Ir à academia"},
    ]

    if not compromissos:
        return f"Você não tem compromissos agendados para hoje, {hoje}."

    resposta = f"Seus compromissos para hoje, {hoje}, são:\n"
    for item in compromissos:
        resposta += f"- {item['hora']}: {item['descricao']}\n"

    return resposta.strip()
