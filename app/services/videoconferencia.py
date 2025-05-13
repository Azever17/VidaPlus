import random
import string

def gerar_link_videoconferencia():
    sala_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"https://meet.jit.si/{sala_id}"
