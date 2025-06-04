import os
import subprocess
import speech_recognition as sr
import pyttsx3
from transformers import pipeline


# Automatically download and load a local language model for text generation.
def load_model(model_name: str = "sberbank-ai/rugpt3small_based_on_gpt2"):
    """Load the HuggingFace model, downloading it if necessary."""
    print(f"Загружаю модель {model_name}...")
    return pipeline(
        "text-generation",
        model=model_name,
        device=-1,  # change to 0 if you have a GPU
    )


generator = load_model()


def speak(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen() -> str | None:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Слушаю...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as exc:
        print(f"Ошибка сервиса распознавания: {exc}")
    return None


def execute_command(command: str) -> str:
    """Execute a shell command and return its output."""
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError as exc:
        return (exc.output or str(exc)).strip()


def chat() -> None:
    history = [
        {"role": "system", "content": "Вы — дружелюбный ассистент."}
    ]
    while True:
        user_input = listen()
        if not user_input:
            continue
        print(f"Вы: {user_input}")
        if user_input.lower() in {"выход", "quit", "exit"}:
            speak("До свидания!")
            break

        if user_input.lower().startswith("команда "):
            cmd = user_input[8:].strip()
            if cmd:
                speak(f"Выполняю команду {cmd}")
                output = execute_command(cmd)
                if output:
                    print(output)
                    speak(output)
            continue

        history.append({"role": "user", "content": user_input})

        # Формируем простой текстовый запрос с контекстом диалога
        prompt = "\n".join([
            f"Пользователь: {m['content']}" if m["role"] == "user" else f"Ассистент: {m['content']}"
            for m in history
        ])
        prompt += "\nАссистент:"

        result = generator(prompt, max_length=len(prompt.split()) + 50, do_sample=True)
        generated = result[0]["generated_text"]
        assistant_msg = generated[len(prompt):].split("\n")[0].strip()
        print(f"Ассистент: {assistant_msg}")
        speak(assistant_msg)
        history.append({"role": "assistant", "content": assistant_msg})


if __name__ == "__main__":
    chat()
