def detect_intention(msg: str) -> tuple[str, dict]:
    msg = msg.lower()

    if  "compromisso" in msg or "agenda" in msg or "calendário" in msg:
        return "agenda", {}

    elif "email" in msg or "e-mail" in msg or "mensagem" in msg:
        return "email", {}

    elif "música" in msg or "tocar" in msg or "spotify" in msg:
        return "music", {}

    else:
        return "ia", {}