import random
import tkinter as tk


WIDTH, HEIGHT = 900, 640
WORDS = {
    "en": (
        "apple", "house", "green", "water", "music", "friend", "garden",
        "window", "planet", "bright", "pencil", "forest", "journey",
        "morning", "picture", "diamond", "library", "computer", "sunshine",
        "adventure", "wonderful", "butterfly", "strawberry", "understand",
    ),
    "tr": (
        "elma", "ev", "yeşil", "su", "müzik", "arkadaş", "bahçe",
        "pencere", "gezegen", "parlak", "kalem", "orman", "yolculuk",
        "sabah", "resim", "elmas", "kütüphane", "bilgisayar", "güneş",
        "macera", "harika", "kelebek", "çilek", "anlamak",
    ),
    "es": (
        "casa", "gato", "agua", "amigo", "verde", "musica", "jardin",
        "ventana", "planeta", "brillante", "lapiz", "bosque", "camino",
        "manana", "dibujo", "diamante", "biblioteca", "computadora",
        "aventura", "mariposa", "fresa", "familia", "estrella",
    ),
}
LANGUAGES = ("en", "tr", "es")
DIFFICULTIES = ("easy", "normal", "hard")
DIFFICULTY_LENGTHS = {"easy": (0, 5), "normal": (0, 99), "hard": (6, 99)}
ROUND_SECONDS = {"easy": 90, "normal": 60, "hard": 40}
UI = {
    "en": {
        "title": "WORD MASTER", "tagline": "Type words, get faster, and complete missions.",
        "ready": "Ready to play?", "mode_hint": "Timed or endless - choose your mode.",
        "start": "START GAME  ->", "infinite": "ENDLESS MODE", "missions": "MISSIONS",
        "settings": "SETTINGS", "tip_menu": "Type each word to get the next one.",
        "settings_title": "SETTINGS", "language": "Language", "difficulty": "Difficulty",
        "back": "<- BACK TO MENU", "easy": "Easy", "normal": "Normal", "hard": "Hard",
        "settings_hint": "Difficulty changes word length and timed mode duration.",
        "mission_hint": "Your progress updates as you play.",
        "mission_words": "Type 10 words in one game",
        "mission_score": "Reach 100 points in one game",
        "mission_streak": "Build a 5-word streak",
        "escape": "ESC  -  MAIN MENU", "score": "SCORE", "time": "TIME",
        "mode": "MODE", "streak": "STREAK", "prompt": "TYPE THIS WORD",
        "next_word": "Type the word correctly to get the next one.",
        "typing_tip": "Tip: Type the letters in the right order.",
        "good": "Nice work!", "points": "points!", "wrong": "Wrong letter; backspace and try again.",
        "time_up": "TIME'S UP!", "typed": "words typed.", "best_streak": "Best streak:",
        "again": "PLAY AGAIN", "menu": "MAIN MENU",
    },
    "tr": {
        "title": "KELIME USTASI", "tagline": "Kelimeleri yaz, hizlan ve gorevleri tamamla.",
        "ready": "Oynamaya hazir misin?", "mode_hint": "Sureli veya sonsuz modu sec.",
        "start": "OYUNA BASLA  ->", "infinite": "SONSUZ MOD", "missions": "GOREVLER",
        "settings": "AYARLAR", "tip_menu": "Her kelimeyi yazarak yenisini getir.",
        "settings_title": "AYARLAR", "language": "Dil", "difficulty": "Zorluk",
        "back": "<- ANA MENU", "easy": "Kolay", "normal": "Normal", "hard": "Zor",
        "settings_hint": "Zorluk, kelime uzunlugunu ve sureyi degistirir.",
        "mission_hint": "Oynadikca ilerlemen guncellenir.",
        "mission_words": "Bir oyunda 10 kelime yaz",
        "mission_score": "Bir oyunda 100 puana ulas",
        "mission_streak": "5 kelimelik seri yap",
        "escape": "ESC  -  ANA MENU", "score": "PUAN", "time": "SURE",
        "mode": "MOD", "streak": "SERI", "prompt": "BU KELIMEYI YAZ",
        "next_word": "Dogru yazinca siradaki kelime gelir.",
        "typing_tip": "Ipucu: Harfleri dogru sirayla yaz.",
        "good": "Guzel gidiyorsun!", "points": "puan!",
        "wrong": "Yanlis harf; silip tekrar dene.",
        "time_up": "SURE DOLDU!", "typed": "kelime yazdin.", "best_streak": "En iyi seri:",
        "again": "TEKRAR OYNA", "menu": "ANA MENU",
    },
    "es": {
        "title": "MAESTRO DE PALABRAS",
        "tagline": "Escribe palabras, mejora y completa misiones.",
        "ready": "Listo para jugar?", "mode_hint": "Elige modo con tiempo o infinito.",
        "start": "EMPEZAR  ->", "infinite": "MODO INFINITO", "missions": "MISIONES",
        "settings": "AJUSTES", "tip_menu": "Escribe cada palabra para ver la siguiente.",
        "settings_title": "AJUSTES", "language": "Idioma", "difficulty": "Dificultad",
        "back": "<- MENU PRINCIPAL", "easy": "Facil", "normal": "Normal", "hard": "Dificil",
        "settings_hint": "La dificultad cambia la longitud y el tiempo del modo cronometrado.",
        "mission_hint": "Tu progreso se actualiza mientras juegas.",
        "mission_words": "Escribe 10 palabras en una partida",
        "mission_score": "Consigue 100 puntos en una partida",
        "mission_streak": "Logra una racha de 5 palabras",
        "escape": "ESC  -  MENU PRINCIPAL", "score": "PUNTOS", "time": "TIEMPO",
        "mode": "MODO", "streak": "RACHA", "prompt": "ESCRIBE ESTA PALABRA",
        "next_word": "Escribe la palabra correctamente para continuar.",
        "typing_tip": "Consejo: escribe las letras en orden.",
        "good": "Muy bien!", "points": "puntos!",
        "wrong": "Letra incorrecta; borra e intentalo de nuevo.",
        "time_up": "TIEMPO!", "typed": "palabras escritas.", "best_streak": "Mejor racha:",
        "again": "JUGAR DE NUEVO", "menu": "MENU PRINCIPAL",
    },
}
BACKGROUND = "#101522"
PANEL = "#1a2233"
MUTED = "#9aa7bd"
TEXT = "#f4f7ff"
ACCENT = "#7c9cff"
GREEN = "#6fe0b0"
LANGUAGE_NAMES = {"en": "English", "tr": "Turkish", "es": "Spanish"}


class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kelime Ustasi")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND)

        self.canvas = tk.Canvas(
            root, width=WIDTH, height=HEIGHT, bg=BACKGROUND, highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Motion>", self.on_motion)

        self.screen = "menu"
        self.language = "tr"
        self.difficulty = "normal"
        self.buttons = {}
        self.words_typed = 0
        self.best_streak = 0
        self.score = 0
        self.streak = 0
        self.seconds_left = ROUND_SECONDS[self.difficulty]
        self.current_word = ""
        self.word_var = tk.StringVar()
        self.word_var.trace_add("write", self.on_word_changed)
        self.entry_window = None
        self.next_word_after = None
        self.timer_after = None

        self.draw_menu()

    def t(self, key):
        return UI[self.language][key]

    def text(self, x, y, value, size, color=TEXT, weight="normal", **options):
        return self.canvas.create_text(
            x, y, text=value, fill=color, font=("Segoe UI", size, weight), **options
        )

    def panel(self, x1, y1, x2, y2, color=PANEL, outline=""):
        return self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline=outline, width=1
        )

    def button(self, name, x1, y1, x2, y2, label, color=ACCENT, fg=TEXT):
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline="", tags=("button", name)
        )
        self.text(
            (x1 + x2) / 2, (y1 + y2) / 2, label, 15, fg, "bold",
            tags=("button", name),
        )
        self.buttons[name] = (x1, y1, x2, y2)

    def draw_background(self):
        if hasattr(self, "entry"):
            self.entry.destroy()
            del self.entry
        self.canvas.delete("all")
        self.buttons.clear()
        for x, y, radius in (
            (70, 90, 2), (830, 95, 2), (785, 530, 2), (110, 540, 2),
            (450, 62, 2), (730, 170, 2), (180, 470, 2),
        ):
            self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius,
                fill="#34405a", outline="",
            )

    def draw_menu(self):
        self.screen = "menu"
        self.root.title(self.t("title"))
        self.draw_background()
        self.text(WIDTH / 2, 150, self.t("title"), 34, TEXT, "bold")
        self.text(WIDTH / 2, 199, self.t("tagline"), 14, MUTED)
        self.panel(255, 260, 645, 435, "#1a2233", "#29344a")
        self.text(WIDTH / 2, 296, self.t("ready"), 19, TEXT, "bold")
        self.text(WIDTH / 2, 328, self.t("mode_hint"), 13, MUTED)
        self.button("start", 275, 360, 475, 410, self.t("start"))
        self.button("infinite", 490, 360, 625, 410, self.t("infinite"), "#52678f")
        self.button("missions", 275, 428, 450, 478, self.t("missions"), "#29344a")
        self.button("settings", 470, 428, 625, 478, self.t("settings"), "#29344a")
        self.text(WIDTH / 2, 548, self.t("tip_menu"), 12, MUTED)

    def draw_settings(self):
        self.screen = "settings"
        self.root.title(self.t("title"))
        self.draw_background()
        self.text(WIDTH / 2, 105, self.t("settings_title"), 30, TEXT, "bold")
        self.panel(175, 155, 725, 250, PANEL, "#29344a")
        self.text(220, 202, self.t("language"), 16, TEXT, "bold", anchor="w")
        self.button("language_prev", 420, 177, 470, 227, "<", "#29344a")
        self.text(570, 202, LANGUAGE_NAMES[self.language], 16, GREEN, "bold")
        self.button("language_next", 670, 177, 720, 227, ">", "#29344a")
        self.panel(175, 275, 725, 370, PANEL, "#29344a")
        self.text(220, 322, self.t("difficulty"), 16, TEXT, "bold", anchor="w")
        self.button("difficulty_prev", 420, 297, 470, 347, "<", "#29344a")
        self.text(570, 322, self.t(self.difficulty), 16, GREEN, "bold")
        self.button("difficulty_next", 670, 297, 720, 347, ">", "#29344a")
        self.text(WIDTH / 2, 415, self.t("settings_hint"), 12, MUTED)
        self.button("back", 345, 490, 555, 540, self.t("back"), "#29344a")

    def draw_missions(self):
        self.screen = "missions"
        self.draw_background()
        self.text(WIDTH / 2, 92, self.t("missions"), 30, TEXT, "bold")
        self.text(WIDTH / 2, 130, self.t("mission_hint"), 13, MUTED)
        missions = (
            ("mission_words", self.words_typed, 10),
            ("mission_score", self.score, 100),
            ("mission_streak", self.best_streak, 5),
        )
        for index, (mission, progress, goal) in enumerate(missions):
            top = 174 + index * 98
            self.panel(190, top, 710, top + 78, PANEL, "#29344a")
            done = progress >= goal
            self.canvas.create_oval(
                212, top + 22, 248, top + 58,
                fill="#214838" if done else "#29344a", outline="",
            )
            self.text(230, top + 40, "✓" if done else str(index + 1), 14,
                      GREEN if done else ACCENT, "bold")
            self.text(270, top + 38, self.t(mission), 13, TEXT, "bold", anchor="w")
            self.text(
                670, top + 38, f"{min(progress, goal)} / {goal}",
                12, GREEN if done else TEXT, "bold", anchor="e",
            )
        self.button("back", 345, 500, 555, 548, self.t("back"), "#29344a")

    def start_game(self, mode="timed"):
        self.screen = "game"
        self.mode = mode
        self.score = 0
        self.streak = 0
        self.words_typed = 0
        self.best_streak = 0
        self.seconds_left = ROUND_SECONDS[self.difficulty]
        self.word_var.set("")
        self.draw_game()
        self.next_word()
        if self.mode == "timed":
            self.timer_after = self.root.after(1000, self.tick)

    def draw_game(self):
        self.draw_background()
        self.text(54, 42, self.t("title"), 14, TEXT, "bold", anchor="w")
        self.text(846, 42, self.t("escape"), 10, MUTED, anchor="e")
        self.panel(115, 92, 785, 158, PANEL, "#29344a")
        self.text(185, 112, self.t("score"), 10, MUTED)
        self.score_label = self.text(185, 139, str(self.score), 20, TEXT, "bold")
        self.text(
            450, 112, self.t("time") if self.mode == "timed" else self.t("mode"),
            10, MUTED,
        )
        self.time_label = self.text(
            450, 139,
            str(self.seconds_left) if self.mode == "timed" else "∞",
            20, TEXT, "bold",
        )
        self.text(715, 112, self.t("streak"), 10, MUTED)
        self.streak_label = self.text(715, 139, str(self.streak), 20, GREEN, "bold")
        self.text(450, 226, self.t("prompt"), 11, MUTED, "bold")
        self.word_label = self.text(450, 280, "", 34, TEXT, "bold")
        self.feedback_label = self.text(450, 324, " ", 11, GREEN)

        self.panel(220, 372, 680, 433, "#1a2233", "#29344a")
        self.entry = tk.Entry(
            self.canvas,
            textvariable=self.word_var,
            justify="center",
            font=("Segoe UI", 19),
            bg="#1a2233",
            fg=TEXT,
            insertbackground=TEXT,
            disabledbackground="#1a2233",
            disabledforeground=TEXT,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
        )
        self.entry_window = self.canvas.create_window(
            450, 402, width=400, height=42, window=self.entry
        )
        self.text(450, 470, self.t("next_word"), 12, MUTED)
        self.text(450, 524, self.t("typing_tip"), 10, "#73819a")
        self.entry.focus_set()

    def next_word(self):
        if self.screen != "game":
            return
        minimum, maximum = DIFFICULTY_LENGTHS[self.difficulty]
        words = [
            word for word in WORDS[self.language]
            if minimum <= len(word) <= maximum
        ]
        self.current_word = random.choice(words)
        self.word_var.set("")
        self.canvas.itemconfigure(self.word_label, text=self.current_word, fill=TEXT)
        self.canvas.itemconfigure(self.feedback_label, text=" ", fill=GREEN)
        self.entry.configure(state="normal")
        self.entry.focus_set()

    def on_word_changed(self, *_):
        if self.screen != "game" or not hasattr(self, "entry"):
            return
        typed = self.word_var.get()
        if not typed:
            self.canvas.itemconfigure(self.word_label, fill=TEXT)
            self.canvas.itemconfigure(self.feedback_label, text=" ")
            return
        if self.current_word.startswith(typed):
            self.canvas.itemconfigure(self.word_label, fill=GREEN)
            self.canvas.itemconfigure(self.feedback_label, text=self.t("good"))
            if typed == self.current_word:
                self.score += len(self.current_word) * 2
                self.streak += 1
                self.words_typed += 1
                self.best_streak = max(self.best_streak, self.streak)
                self.canvas.itemconfigure(self.score_label, text=str(self.score))
                self.canvas.itemconfigure(self.streak_label, text=str(self.streak))
                self.canvas.itemconfigure(
                    self.feedback_label,
                    text=f"+{len(self.current_word) * 2} {self.t('points')}",
                )
                self.entry.configure(state="disabled")
                if self.next_word_after is not None:
                    self.root.after_cancel(self.next_word_after)
                self.next_word_after = self.root.after(350, self.next_word)
        else:
            self.streak = 0
            self.canvas.itemconfigure(self.word_label, fill="#ff7885")
            self.canvas.itemconfigure(
                self.feedback_label, text=self.t("wrong"),
                fill="#ff7885",
            )
            self.canvas.itemconfigure(self.streak_label, text="0")

    def tick(self):
        if self.screen != "game" or self.mode != "timed":
            return
        self.seconds_left -= 1
        self.canvas.itemconfigure(
            self.time_label, text=str(self.seconds_left),
            fill="#ff7885" if self.seconds_left <= 10 else TEXT,
        )
        if self.seconds_left <= 0:
            self.end_game()
        else:
            self.timer_after = self.root.after(1000, self.tick)

    def end_game(self):
        self.screen = "result"
        if self.next_word_after is not None:
            self.root.after_cancel(self.next_word_after)
            self.next_word_after = None
        self.draw_background()
        self.text(WIDTH / 2, 190, self.t("time_up"), 31, TEXT, "bold")
        self.text(WIDTH / 2, 258, f"{self.score} {self.t('score')}", 25, GREEN, "bold")
        self.text(WIDTH / 2, 305, f"{self.words_typed} {self.t('typed')}", 14, MUTED)
        self.text(
            WIDTH / 2, 338, f"{self.t('best_streak')} {self.best_streak}", 12, MUTED
        )
        self.button("play_again", 295, 390, 605, 440, self.t("again"))
        self.button("missions", 295, 455, 605, 505, self.t("missions"), "#29344a")
        self.button("menu", 295, 520, 605, 570, self.t("menu"), "#29344a")

    def on_click(self, event):
        for name, (x1, y1, x2, y2) in self.buttons.items():
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                if name == "start" or name == "play_again":
                    self.start_game()
                elif name == "infinite":
                    self.start_game(mode="infinite")
                elif name == "settings":
                    self.draw_settings()
                elif name == "language_prev":
                    index = LANGUAGES.index(self.language)
                    self.language = LANGUAGES[(index - 1) % len(LANGUAGES)]
                    self.draw_settings()
                elif name == "language_next":
                    index = LANGUAGES.index(self.language)
                    self.language = LANGUAGES[(index + 1) % len(LANGUAGES)]
                    self.draw_settings()
                elif name == "difficulty_prev":
                    index = DIFFICULTIES.index(self.difficulty)
                    self.difficulty = DIFFICULTIES[(index - 1) % len(DIFFICULTIES)]
                    self.draw_settings()
                elif name == "difficulty_next":
                    index = DIFFICULTIES.index(self.difficulty)
                    self.difficulty = DIFFICULTIES[(index + 1) % len(DIFFICULTIES)]
                    self.draw_settings()
                elif name == "missions":
                    self.cancel_timers()
                    self.draw_missions()
                elif name == "back" or name == "menu":
                    self.cancel_timers()
                    self.draw_menu()
                return

    def on_motion(self, event):
        self.canvas.configure(cursor="")
        for x1, y1, x2, y2 in self.buttons.values():
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.canvas.configure(cursor="hand2")
                return

    def cancel_timers(self):
        for timer in (self.timer_after, self.next_word_after):
            if timer is not None:
                self.root.after_cancel(timer)
        self.timer_after = None
        self.next_word_after = None

    def on_escape(self, _event):
        if self.screen == "game":
            self.cancel_timers()
            self.draw_menu()
        elif self.screen == "settings":
            self.draw_menu()


def main():
    root = tk.Tk()
    game = TypingGame(root)
    root.bind("<Escape>", game.on_escape)
    root.mainloop()


if __name__ == "__main__":
    main()