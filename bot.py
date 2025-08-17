import tkinter as tk
from tkinter import scrolledtext
from tkinter.simpledialog import askstring
import random
from datetime import datetime
import pyttsx3
import threading as th
import os
from tkinter import Checkbutton
from tkinter import messagebox
from dotenv import load_dotenv
import types

# errors
error = {
    "invalid_input": "ERROR 1/255: InvalidInputError\nUser has input invalid instructions.\n\n",
    "pass_error": '\nERROR 2/255: NameError\n.env variable "PASS" is not set or is false.\n\n',
    "none_input": "\nERROR 3/255: TypeError\nUser canceled the input dialog (received None/null).\n\n",
    "value_error": "\nERROR 4/255: ValueError\nUser input contained non-numeric characters or was empty.\n\n",
    "file_not_found": "\nERROR 5/255: FileNotFoundError\nA file failed to load\n\n",
    "tts_error": "\nERROR 6/255: TTSEngineFailedError\nThe TTS engine failed to load\n\n",
    "theme_error": "\nERROR 7/255: ThemeError\nTheme not configured correctly\n\n",
    "harmful_input": "\nERROR 254/255: ViolationError\nUser has input offensive wording.\n\n",
    "unknown": "\nERROR 255/255: UnknownError\nUnknown error occurred\n\n",
}


with open("bot_log.txt", "w", encoding="utf-8") as log_file:
    log_file.write("=== (2.5) Chat Log Initialized (2.5) ===\n\n")

version = "2.5 TESTING"

try:
    load_dotenv("config.env")
    confirmer = os.getenv("PASS")
    if confirmer == "true":
        key = os.getenv("DEV_KEY")
        name = os.getenv("NAME")
        is_published = os.getenv("MODE")
        back = os.getenv("THEME")
    else:
        name = os.getenv("NAME")
        is_published = os.getenv("MODE")
        back = os.getenv("THEME")
except FileNotFoundError:
    with open("bot_lox.txt", "a", encoding="utf-8") as log_file:
        log_file.write(error["file_not_found"])
except:
    with open("bot_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(error["unknown"])


def tts(string):
    def speak():
        try:
            eng = pyttsx3.init()
            eng.setProperty("rate", 140)
            eng.say(string)
            eng.runAndWait()
        except:
            with open("bot_log.txt", "a", encoding="utf-8") as logger:
                logger.write(error["tts_error"])

    th.Thread(target=speak, daemon=True).start()


root = tk.Tk()
root.title("East Joint Bot")
root.geometry("1280x720")
root.state("zoomed")

chat_box = scrolledtext.ScrolledText(
    root, width=100, height=20, wrap=tk.WORD, font=("Arial", 26, "bold")
)
chat_box.tag_config("red", foreground="red", font=("Arial", 26, "bold"))
chat_box.tag_config("blue", foreground="blue", font=("Arial", 26, "bold"))
chat_box.tag_config("yellow", foreground="yellow", font=("Arial", 26, "bold"))

chat_box.pack(padx=10, pady=10)


def safe_insert(self, *args, **kwargs):
    self.configure(state="normal")
    tk.Text.insert(self, *args, **kwargs)
    self.configure(state="disabled")
    self.see(tk.END)


chat_box.insert = types.MethodType(safe_insert, chat_box)

chat_box.config(state="disabled")
chat_box.bind("<Key>", lambda e: "break")
chat_box.bind("<Button-1>", lambda e: "break")

chat_box.insert(
    tk.END,
    'Bot is online. Type "help" to see commands.\nPlease check the README for more info.\n\n',
)

if is_published == "published":
    chat_box.insert(tk.END, "Welcome to East Joint Marketing Solutions!\n\n", "blue")
elif is_published == "_published_":
    chat_box.insert(tk.END, "Welcome to East Joint Marketing Solutions!\n\n", "blue")
elif is_published == "testing":
    chat_box.insert(tk.END, "THIS BOT IS IN TESTING EXPECT BUGS\n\n", "yellow")
    chat_box.see(tk.END)
elif is_published == "dead":
    chat_box.insert(tk.END, "\n\nTHIS MODEL IS NO LONGER IN USE.\n\n", "red")
    tts("THIS MODEL IS NO LONGER IN USE")
    root.after(3500, root.destroy)
else:
    chat_box.insert(tk.END, error["file_not_found"], "red")
    chat_box.see(tk.END)
    tts(error["file_not_found"])
    root.after(3500, root.destroy)

chat_box.insert(tk.END, "- help\n")
chat_box.insert(tk.END, "- hello\n")
chat_box.insert(tk.END, "- hours\n")
chat_box.insert(tk.END, "- AI\n")
chat_box.insert(tk.END, "- number\n")
chat_box.insert(tk.END, "- about\n")
chat_box.insert(tk.END, "- clear\n")
chat_box.insert(tk.END, "- exit / quit\n")
chat_box.insert(tk.END, "- services\n")
chat_box.insert(tk.END, "- company\n")
chat_box.insert(tk.END, "- links\n")
chat_box.insert(tk.END, "- why us\n")
chat_box.insert(tk.END, "- dev cut (requires a key)\n")
chat_box.insert(tk.END, "- logs (No TTS support to avoid confusion)\n")
chat_box.insert(tk.END, "- version\n")
chat_box.insert(tk.END, "- errors\n")
chat_box.insert(tk.END, "- settings\n\n")

user_input = tk.Entry(root, width=100, font=("Arial", 15, "normal"))
user_input.pack(padx=10, pady=(0, 10))

try:
    if back == "white":
        root.config(bg="white")
    elif back == "black":
        root.config(bg="black")
        chat_box.config(bg="black")
        chat_box.config(fg="white")
    elif back == "green":
        root.config(bg="lime")
        chat_box.config(bg="lime")
    elif back == "blue":
        root.config(bg="cyan")
        chat_box.config(bg="cyan")
    elif back in ("gray", "grey"):
        root.config(bg="grey")
        chat_box.config(bg="grey")
        chat_box.config(fg="white")
    else:
        messagebox.showerror("Theme Error", error["theme_error"])
except FileNotFoundError:
    chat_box.insert(tk.END, error["file_not_found"])
except:
    chat_box.insert(tk.END, error["unknown"])


if is_published == "published":
    tts_enabled = tk.BooleanVar(value=True)
    tts_checkbox = Checkbutton(
        root,
        text="Enable Text-To-Speech (TTS)",
        bg="cyan",
        variable=tts_enabled,
        font=("Arial", 14),
    )
elif is_published == "_published_":
    tts_enabled = tk.BooleanVar(value=False)
    tts_checkbox = Checkbutton(
        root,
        text="Enable Text-To-Speech (TTS)",
        bg="cyan",
        variable=tts_enabled,
        font=("Arial", 14),
    )
else:
    tts_enabled = tk.BooleanVar(value=False)
    tts_checkbox = Checkbutton(
        root,
        text="Enable Text-To-Speech (TTS)",
        bg="yellow",
        variable=tts_enabled,
        font=("Arial", 14),
    )
tts_checkbox.pack(padx=(0, 600), pady=(1, 10))


def send_input():
    con = tts_enabled.get()
    msg = user_input.get()
    if msg:
        now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        response = get_response(msg, con)

        chat_box.insert(tk.END, f">> {msg}\n", "user")
        chat_box.see(tk.END)
        if response:
            chat_box.insert(tk.END, response + "\n\n", "bot")
            chat_box.see(tk.END)
        try:
            with open("bot_log.txt", "a", encoding="utf-8") as log_file:
                log_file.write(f"{now}\n{name}: {msg}\n")
                if response:
                    log_file.write(f"BOT: {response}\n")
                else:
                    log_file.write("BOT: [no response]\n")
                log_file.write("-" * 100 + "\n\n")
        except FileNotFoundError:
            chat_box.insert(tk.END, error["file_not_found"])
            chat_box.see(tk.END)
        except:
            chat_box.insert(tk.END, error["unknown"])
            chat_box.see(tk.END)

        user_input.delete(0, tk.END)  # I forgor what dis do but it do a thingy


user_input.bind("<Return>", lambda event: send_input())
user_input.focus()


bot_number = random.randint(1, 100000)
sec_number = bot_number * bot_number * 4378129  # totally didn't type random stuff

lines = [
    "- Customer Support: Inbound, and outbound to tailor to your campaign needs.",
    "- Live Chat Assistance: Real-time support to help your customers with faster resolution and higher satisfaction.",
    "- Back-Office Solutions: Reliable handling of data entry, admin tasks, CRM updates, and reporting.",
    "- Lead Generation & Sales: Skilled outbound agents generating qualified leads and converting interest into action.",
    "- E-commerce Support: Order processing, customer care, returns, and inventory inquiries for online sellers.",
    "- Billing and Account Verification: Accurate, secure handling of billing-related concerns and client identity verification.\n\n",
    "Sectors We Serve\n ",
    "- Healthcare / We assist with appointment scheduling, insurance-related inquiries, patient follow-ups, and administrative coordination—delivered with professionalism and discretion.",
    "- Real Estate / From initial inquiry to post-sale coordination, we support agents and brokers with appointment setting, CRM updates, and follow-up calls.",
    "- Human Resources / Our team assists in recruitment processes, onboarding coordination, and HR helpdesk services, easing your internal workload.",
    "- Energy & Utilities / We provide billing assistance, outage reporting, and service inquiries, ensuring consistent and accurate client interaction.",
    "- eCommerce / We manage inquiries, returns, and support across marketplaces, helping you maintain customer satisfaction and operational efficiency.\n\n",
    "Link to Our Website: https://ejempire.com\n",
]


def get_response(user_input, con):
    user = user_input.lower().strip()
    try:
        with open("banned words.txt", "r") as f:
            bad_words = f.read().splitlines()
    except:
        if con:
            chat_box.insert(tk.END, error["file_not_found"])
            tts(error["file_not_found"])
            chat_box.see(tk.END)
        else:
            chat_box.insert(tk.END, error["file_not_found"])
            chat_box.see(tk.END)
        tk.after(
            4000, root.destroy
        )  # this punishes people who think they can bypass the filter

    if user in ("help", "command", "commands", "queries", "query", "dir"):
        return "\n".join(
            [
                "",
                "- help",
                "- hello",
                "- hours",
                "- AI",
                "- number",
                "- about",
                "- clear",
                "- exit / quit",
                "- services",
                "- company",
                "- links",
                "- why us",
                "- dev cut (requires a key)",
                "- logs (No TTS support to avoid confusion)",
                "- version",
                "- errors",
                "- settings",
            ]
        )

    elif user in (
        "hello",
        "hey",
        "hi",
        "yo",
        "yo hi",
        "yo hey",
        "yo hello",
        "wassup",
        "whats up",
        "what's up",
        "whats up?",
        "what's up?",
    ):
        if con:
            tts("Hello! How can I assist you today?")
            return "\nHello! How can I assist you today?"
        else:
            return "\nHello! How can I assist you today?"

    elif user in (
        "hours",
        "hour?",
        "hours",
        "hours?",
        "when are you open",
        "when are you open?",
    ):
        if con:
            tts("Our service is available twenty-four seven")
            return "\nOur service is available 24/7."
        else:
            return "\nOur service is available 24/7."

    elif user == "what do you do":
        if con:
            tts("I am a bot that provides information about our company.")
            return "\nI am a bot that provides information about our company."
        else:
            return "\nI am a bot that provides information about our company."

    elif user in (
        "is this an ai",
        "is this an ai?",
        "are you an ai",
        "are you an ai?",
        "ai",
        "ai?",
    ):
        if con:
            tts(
                f"No, I am not an AI. I am a bot with predetermined answers. My bot number is: {bot_number}"
            )
            return f"\nNo, I am not an AI. I am a bot with predetermined answers.\nMy bot number is: {bot_number}"
        else:
            return f"\nNo, I am not an AI. I am a bot with predetermined answers.\nMy bot number is: {bot_number}"

    elif user in ("number", "number?", "bot number", "bot number?"):
        if con:
            tts(f"My bot number is: {bot_number}, My security number is: {sec_number}")
            return (
                f"\nMy bot number is: {bot_number}\nMy security number is: {sec_number}"
            )
        else:
            return (
                f"\nMy bot number is: {bot_number}\nMy security number is: {sec_number}"
            )

    elif user == "about":
        if con:
            tts("")
            return "\n"
        else:
            return "\nplaceholder :/"  # mom will add stuff here :D

    elif user in ("who made you", "who made you?"):
        if con:
            tts("I was created by a developer who prefers to remain anonymous")
            return "\nI was created by a developer who prefers to remain anonymous"
        else:
            return "\nI was created by a developer who prefers to remain anonymous"

    elif user in ("exit", "quit"):
        if con:
            tts("Chat ended")
            root.after(2000, root.destroy)
            return "\nChat ended"
        else:
            root.after(800, root.destroy)
            return "\nChat ended"

    elif user in ("cls", "clear"):
        chat_box.config(state="normal")
        chat_box.delete(1.0, tk.END)
        chat_box.config(state="disabled")
        return "[SCREEN CLEARED]"

    elif user in (
        "services",
        "services?",
        "what are your services",
        "what are your services?",
        "what's your services",
        "whats your services",
        "what's your services?",
        "whats your services?",
    ):
        text = "\n".join(lines) + "\n"
        chat_box.insert(tk.END, text)
        chat_box.see(tk.END)

        def speak_services():
            combined_lines = " ".join([line for line in lines if line.strip()])
            tts(f"Our services include: {combined_lines}")
            return text

        if con:
            root.after(
                200, lambda: th.Thread(target=speak_services, daemon=True).start()
            )

    elif user in ("company", "company?", "comp", "comp?"):
        if con:
            tts("East Joint Marketing Solutions")
            return "\nEast Joint Marketing Solutions"
        else:
            return "\nEast Joint Marketing Solutions"

    elif user in ("links", "link", "linkie", "linkies", "address", "addresses"):
        webs = [
            "\nhttps://ejempire.com -- The Main Website - EJ Empire.",
            "https://jansassybeauty.com -- Bio Products - JanSassy Beauty.",
            "https://allweeksale.com -- Clothing - AllWeekSale.",
            "https://www.facebook.com/jansassybeauty -- Bio Products - JanSassy Beauty Facebook.",
            "https://www.facebook.com/profile.php?id=100070556280103 -- Bags - JanSassy Collection.",
        ]
        web_text = "\n".join(webs)
        if con:
            root.after(100, lambda: tts("Here are the links: " + " ".join(webs)))
            return web_text
        else:
            return web_text

    elif user in (
        "dev cut",
        "devcut",
        "devs cut",
        "devscut",
        "developer cut",
        "developers cut",
        "developer's cut",
        "dev",
        "developer",
    ):
        asker = askstring("Password", "Please input the key:")

        if asker is None:
            if con:
                tts(error["none_input"])
            return error["none_input"]
        elif not asker.strip():
            if con:
                tts(error["value_error"])
                return error["value_error"]
        try:
            if os.getenv("PASS") != "true":
                raise NameError
            if not key:
                raise NameError

            if asker == key:
                msg = f"\nHello, developer here, I just wanna say that this program took me about a week or 2, and I hope you got what you wanted from here. Bye from the East Joint dev team."
                if con:
                    tts(msg)
                return msg
            else:
                if con:
                    tts("User failed password")
                return "\nUser failed password"

        except NameError:
            if con:
                tts(error["pass_error"])
            return error["pass_error"]

    # Prevent logging the "logs" command to avoid recursive confusion
    elif user in (
        "log",
        "logs",
        "logging",
        "loggings",
        "logger",
        "loggers",
        "bot log",
        "bot logs",
        "show me your mind",
        "show me your logs",
        "show me your files",
        "log files",
    ):
        prompt = askstring("Password", "Please input the security number:")

        if prompt is None:
            if con:
                tts(error["none_input"])
                return error["none_input"]
            else:
                return error["none_input"]
        try:
            if int(prompt.strip()) == sec_number:
                with open("bot_log.txt", "r", encoding="utf-8") as Read:
                    logs = Read.read()
                    chat_box.insert(tk.END, logs)
                    chat_box.see(tk.END)
                return None
            else:
                return "\nIncorrect number\n\n"
        except ValueError:
            if con:
                tts(error["value_error"])
                return error["value_error"]
            else:
                return error["value_error"]

    elif user in (
        "version",
        "versions",
        "version number",
        "ver",
        "whats the version number",
        "what's the version number",
        "what's the version number?",
        "whats the version number?",
    ):
        if con:
            tts(f"\nThe version number is: {version}")
            return f"\nThe version number is: {version}"
        else:
            return f"\nThe version number is: {version}"

    elif user in (
        "error",
        "errors",
        "error messages",
        "1/255",
        "2/255",
        "3/255",
        "4/255",
        "254/255",
        "255/255",
    ):
        errors = "\n".join(error.values())
        if con:
            tts(errors)
        return errors

    elif user in (
        "why us",
        "why us?",
        "why you",
        "why you?",
        "why would you choose us",
        "why would you choose us?",
        "why would i choose you?",
        "why would i choose you",
        "why should i choose you",
        "why should i choose you?",
    ):
        if con:
            tts(
                "Our employees have over 8 years of B P O excellence, we have 24 7 operations with dedicated night shift teams, we have fully equipped, and experienced agents, flexible staff, and transparency on our work."
            )
            return "\nOur employees have over 8 years of BPO excellence, we have 24/7 operations with dedicated night shift teams, we have fully equipped, and experienced agents, flexible staff, and transparency on our work."
        else:
            return "\nOur employees have over 8 years of BPO excellence, we have 24/7 operations with dedicated night shift teams, we have fully equipped, and experienced agents, flexible staff, and transparency on our work."

    elif user in ("config", "configuration", "setting", "settings"):
        try:
            with open("config.env", "r") as idk:
                settings = idk.read().strip()
            formatted = f"\nCurrent Configuration:\n{settings}"
            if con:
                tts(formatted.replace("=", " is "))
            return formatted
        except FileNotFoundError:
            if con:
                tts(error["file_not_found"])
            return error["file_not_found"]

    # Input Moderation

    elif any(bad_word in user.split() for bad_word in bad_words):
        if con:
            tts(error["harmful_input"])
            messagebox.showerror("Profanity", error["harmful_input"])
            root.destroy()
        else:
            messagebox.showerror("Profanity", error["harmful_input"])
            root.destroy()

    # when the thingy fails (which it WILL)
    else:
        if con:
            tts(
                f'"{user}" doesn\'t look like a valid command. Type "help" to see the list of available commands.'
            )
            return f'\n"{user}" doesn\'t look like a valid command. Type "help" to see the list of available commands.\n{error["invalid_input"]}'
        else:
            return f'\n"{user}" doesn\'t look like a valid command. Type "help" to see the list of available commands.\n{error["invalid_input"]}'


def bot_start():
    root.mainloop()


if __name__ == "__main__":
    bot_start()  # the magic words
