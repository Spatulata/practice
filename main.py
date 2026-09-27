import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

from practice import (
    calculate_sum,
    choose_structure,
    default_report_path,
    demo_loop_control,
    detect_value_type,
    filter_positive_even,
    format_report,
    lookup_or_update_dict,
    safe_parse_int,
    save_report,
    score_quiz,
)
from topics_data import AUTHORS, QUIZ_MENU, QUIZ_QUESTIONS, TOPICS


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Основы Python")
        self.geometry("960x650")
        self.minsize(800, 520)
        self.configure(bg="#f2f2f2")

        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure(".", background="#f2f2f2", foreground="#111111")
        style.configure("TFrame", background="#f2f2f2")
        style.configure("TLabel", background="#f2f2f2", foreground="#111111")
        style.configure("TLabelframe", background="#f2f2f2", foreground="#111111")
        style.configure("TLabelframe.Label", background="#f2f2f2", foreground="#111111")
        style.configure("TButton", foreground="#111111")

        self.menu_items = list(TOPICS) + [QUIZ_MENU]
        self.demo_topics = ("functions", "comprehension")
        self.catalog = {"apple": 80, "bread": 45, "milk": 70}
        self.quiz_answers = [None] * len(QUIZ_QUESTIONS)
        self.quiz_index = 0
        self.quiz_finished = False
        self.last_score = None
        self.current_index = 0

        self.build_ui()
        self.show_topic(0)
        self.set_status("Выберите тему слева")

    def build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        top = ttk.Frame(self, padding=10)
        top.grid(row=0, column=0, sticky="ew")
        ttk.Label(top, text="Основы Python", font=("Arial", 14, "bold")).pack(
            side=tk.LEFT
        )
        ttk.Label(top, text="Автор:").pack(side=tk.LEFT, padx=(20, 4))
        self.user_var = tk.StringVar(value="Поляков С. Р.")
        ttk.Entry(top, textvariable=self.user_var, width=16).pack(side=tk.LEFT)
        ttk.Button(top, text="О программе", command=self.show_about).pack(side=tk.RIGHT)

        mid = ttk.Frame(self, padding=(10, 0, 10, 8))
        mid.grid(row=1, column=0, sticky="nsew")
        mid.columnconfigure(1, weight=1)
        mid.rowconfigure(0, weight=1)

        left = ttk.LabelFrame(mid, text="Темы", padding=8)
        left.grid(row=0, column=0, sticky="ns", padx=(0, 8))

        self.topic_list = tk.Listbox(
            left,
            width=34,
            height=18,
            exportselection=False,
            bg="white",
            fg="#111111",
            selectbackground="#4a90d9",
            selectforeground="white",
            highlightthickness=1,
        )
        self.topic_list.pack(fill=tk.BOTH, expand=True)
        for item in self.menu_items:
            self.topic_list.insert(tk.END, item["title"])
        self.topic_list.bind("<<ListboxSelect>>", self.on_select)

        ttk.Button(left, text="Следующая тема", command=self.next_topic).pack(
            fill=tk.X, pady=(8, 2)
        )
        ttk.Button(left, text="Сохранить результат", command=self.save_results).pack(
            fill=tk.X, pady=2
        )

        right = ttk.Frame(mid)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(0, weight=1)
        right.rowconfigure(0, weight=3)
        right.rowconfigure(1, weight=2)

        theory_frame = ttk.LabelFrame(right, text="Теория и примеры", padding=8)
        theory_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 8))
        theory_frame.rowconfigure(0, weight=1)
        theory_frame.columnconfigure(0, weight=1)

        self.theory_text = scrolledtext.ScrolledText(
            theory_frame,
            wrap=tk.WORD,
            height=14,
            font=("Courier New", 11),
            bg="white",
            fg="#111111",
            insertbackground="#111111",
        )
        self.theory_text.grid(row=0, column=0, sticky="nsew")
        self.theory_text.config(state=tk.DISABLED)

        practice_frame = ttk.LabelFrame(right, text="Практика", padding=8)
        practice_frame.grid(row=1, column=0, sticky="nsew")
        practice_frame.columnconfigure(0, weight=1)
        practice_frame.rowconfigure(3, weight=1)

        self.hint_label = ttk.Label(practice_frame, text="", wraplength=580)
        self.hint_label.grid(row=0, column=0, sticky="ew", pady=(0, 6))

        self.controls = ttk.Frame(practice_frame)
        self.controls.grid(row=1, column=0, sticky="ew")
        self.controls.columnconfigure(1, weight=1)

        self.input_label = ttk.Label(self.controls, text="Ввод:")
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(self.controls, textvariable=self.input_var)

        self.choice_label = ttk.Label(self.controls, text="Выбор:")
        self.choice_var = tk.StringVar()
        self.choice_box = ttk.Combobox(
            self.controls, textvariable=self.choice_var, state="readonly"
        )

        self.radio_var = tk.StringVar(value="")
        self.radio_frame = ttk.Frame(self.controls)
        self.radio_buttons = []

        btns = ttk.Frame(practice_frame)
        btns.grid(row=2, column=0, sticky="ew", pady=4)
        ttk.Button(btns, text="Проверить", command=self.check_practice).pack(
            side=tk.LEFT, padx=(0, 6)
        )
        ttk.Button(btns, text="Очистить", command=self.clear_practice).pack(side=tk.LEFT)
        self.demo_args_btn = ttk.Button(btns, text="Демо *args", command=self.demo_args)

        self.result_text = scrolledtext.ScrolledText(
            practice_frame,
            wrap=tk.WORD,
            height=5,
            font=("Courier New", 11),
            bg="white",
            fg="#111111",
            insertbackground="#111111",
        )
        self.result_text.grid(row=3, column=0, sticky="nsew")
        self.result_text.config(state=tk.DISABLED)

        bottom = ttk.Frame(self, padding=(10, 4, 10, 8))
        bottom.grid(row=2, column=0, sticky="ew")
        self.status_var = tk.StringVar()
        ttk.Label(bottom, textvariable=self.status_var).pack(side=tk.LEFT)

    def on_select(self, event=None):
        sel = self.topic_list.curselection()
        if sel:
            self.show_topic(sel[0])

    def next_topic(self):
        i = min(self.current_index + 1, len(self.menu_items) - 1)
        self.topic_list.selection_clear(0, tk.END)
        self.topic_list.selection_set(i)
        self.topic_list.see(i)
        self.show_topic(i)

    def is_quiz(self, index=None):
        if index is None:
            index = self.current_index
        return self.menu_items[index]["id"] == "quiz"

    def set_demo_args_visible(self, visible):
        if visible:
            self.demo_args_btn.pack(side=tk.RIGHT)
        else:
            self.demo_args_btn.pack_forget()

    def set_controls_mode(self, mode):
        for w in (
            self.input_label,
            self.input_entry,
            self.choice_label,
            self.choice_box,
            self.radio_frame,
        ):
            w.grid_remove()

        self.input_var.set("")
        self.choice_var.set("")
        self.choice_box["values"] = ()
        self.radio_var.set("")

        if mode == "text":
            self.input_label.grid(row=0, column=0, sticky="w", padx=(0, 6))
            self.input_entry.grid(row=0, column=1, sticky="ew")
            self.input_entry.config(state=tk.NORMAL)
        elif mode == "choice":
            self.choice_label.grid(row=0, column=0, sticky="w", padx=(0, 6))
            self.choice_box.grid(row=0, column=1, sticky="w")
            self.choice_box.config(state="readonly")
        elif mode == "quiz":
            self.radio_frame.grid(row=0, column=0, columnspan=2, sticky="w")

    def show_topic(self, index):
        self.current_index = index
        self.clear_practice(silent=True)
        self.clear_radios()
        self.topic_list.selection_clear(0, tk.END)
        self.topic_list.selection_set(index)

        if self.is_quiz(index):
            self.show_quiz()
            return

        topic = self.menu_items[index]
        text = (
            topic["title"]
            + "\n"
            + "=" * 50
            + "\n\n"
            + "ТЕОРИЯ\n"
            + topic["theory"]
            + "\n\n"
            + "СИНТАКСИС\n"
            + topic["syntax"]
            + "\n\n"
            + "ПРИМЕР\n"
            + topic["example"]
        )
        self.set_text(self.theory_text, text)
        self.hint_label.config(text=topic["practice_hint"])
        self.setup_practice(topic["id"])
        self.set_status("Тема: " + topic["title"])

    def setup_practice(self, topic_id):
        self.set_demo_args_visible(topic_id in self.demo_topics)

        if topic_id in ("list_tuple", "loops"):
            self.set_controls_mode("choice")
            if topic_id == "list_tuple":
                self.choice_box["values"] = ("list", "tuple")
                self.choice_var.set("tuple")
            else:
                self.choice_box["values"] = ("break", "continue", "pass")
                self.choice_var.set("continue")
            return

        self.set_controls_mode("text")
        if topic_id == "types":
            self.input_var.set("42")
        elif topic_id == "dict":
            self.input_var.set("apple")
            self.set_result("Словарь сейчас: " + str(self.catalog))
        elif topic_id == "comprehension":
            self.input_var.set("-2 -1 0 1 2 3 4 5 6")
        elif topic_id == "exceptions":
            self.input_var.set("12")
        elif topic_id == "functions":
            self.input_var.set("1 2 3 4 5")

    def show_quiz(self):
        self.set_demo_args_visible(False)
        self.hint_label.config(
            text="Выберите ответ и нажмите Проверить. Потом можно сохранить результат."
        )
        if self.quiz_finished:
            self.set_controls_mode("none")
            self.draw_quiz_summary()
        else:
            self.set_controls_mode("quiz")
            self.draw_quiz()
        self.set_status("Итоговый тест")

    def draw_quiz(self):
        q = QUIZ_QUESTIONS[self.quiz_index]
        text = (
            "ИТОГОВЫЙ ТЕСТ\n"
            + "=" * 50
            + "\n\n"
            + "Вопрос {} из {}\n\n".format(self.quiz_index + 1, len(QUIZ_QUESTIONS))
            + q["question"]
            + "\n"
        )
        self.set_text(self.theory_text, text)
        self.clear_radios()
        self.radio_var.set("")
        for i, opt in enumerate(q["options"]):
            rb = ttk.Radiobutton(
                self.radio_frame, text=opt, value=str(i), variable=self.radio_var
            )
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)

        done = sum(1 for a in self.quiz_answers if a is not None)
        last = self.last_score if self.last_score else "ещё нет"
        self.set_result(
            "Отвечено: {}/{}. Последний результат: {}".format(
                done, len(QUIZ_QUESTIONS), last
            )
        )

    def draw_quiz_summary(self):
        self.clear_radios()
        text = (
            "ИТОГОВЫЙ ТЕСТ — завершён\n"
            + "=" * 50
            + "\n\n"
            + "Результат: {}\n\n".format(self.last_score or "-")
            + "Можно сохранить результат.\n"
            + "Чтобы пройти заново, нажмите Очистить."
        )
        self.set_text(self.theory_text, text)
        self.hint_label.config(text="Тест завершён.")
        self.set_result("Итог: " + (self.last_score or "-"))

    def check_practice(self):
        if self.is_quiz():
            self.check_quiz()
            return

        topic_id = self.menu_items[self.current_index]["id"]
        try:
            if topic_id == "types":
                type_name, value = detect_value_type(self.input_var.get())
                self.set_result(
                    "Значение: {!r}\nТип: {}\n{}".format(value, type_name, type(value))
                )
            elif topic_id == "list_tuple":
                _ok, msg = choose_structure(self.choice_var.get())
                self.set_result(msg)
            elif topic_id == "dict":
                self.catalog, msg = lookup_or_update_dict(
                    self.catalog, self.input_var.get()
                )
                self.set_result(msg)
            elif topic_id == "loops":
                self.set_result(demo_loop_control(self.choice_var.get()))
            elif topic_id == "comprehension":
                result = filter_positive_even(self.input_var.get())
                self.set_result("Положительные чётные: " + str(result))
            elif topic_id == "exceptions":
                _ok, msg = safe_parse_int(self.input_var.get())
                self.set_result(msg)
            elif topic_id == "functions":
                self.demo_args()
                return
            self.set_status("Проверено")
        except ValueError as e:
            self.set_status("Ошибка ввода")
            self.set_result("Ошибка: " + str(e))
            messagebox.showerror("Ошибка", str(e))

    def check_quiz(self):
        if self.quiz_finished:
            messagebox.showinfo("Тест", "Тест уже пройден. Нажмите Очистить.")
            return

        selected = self.radio_var.get()
        if selected == "":
            messagebox.showwarning("Внимание", "Сначала выберите вариант")
            return

        self.quiz_answers[self.quiz_index] = int(selected)
        correct = QUIZ_QUESTIONS[self.quiz_index]["answer"]
        if int(selected) == correct:
            feedback = "Верно!"
        else:
            right_opt = QUIZ_QUESTIONS[self.quiz_index]["options"][correct]
            feedback = "Неверно. Правильно: " + right_opt

        if self.quiz_index + 1 < len(QUIZ_QUESTIONS):
            self.quiz_index += 1
            self.draw_quiz()
            done = sum(1 for a in self.quiz_answers if a is not None)
            self.set_result(
                "{}\n\nОтвечено: {}/{}. Последний результат: {}".format(
                    feedback, done, len(QUIZ_QUESTIONS), self.last_score or "ещё нет"
                )
            )
        else:
            answers_key = [q["answer"] for q in QUIZ_QUESTIONS]
            right, total, percent, _answered = score_quiz(self.quiz_answers, answers_key)
            self.last_score = "{}/{} ({:.0f}%)".format(right, total, percent)
            self.quiz_finished = True
            self.set_controls_mode("none")
            self.draw_quiz_summary()
            self.set_result(feedback + "\n\nИтог: " + self.last_score)
            self.set_status("Тест: " + self.last_score)

    def clear_practice(self, silent=False):
        self.input_var.set("")
        self.choice_var.set("")
        self.radio_var.set("")
        self.set_result("")
        if self.is_quiz() and not silent:
            self.quiz_answers = [None] * len(QUIZ_QUESTIONS)
            self.quiz_index = 0
            self.quiz_finished = False
            self.last_score = None
            self.set_controls_mode("quiz")
            self.draw_quiz()
            self.set_status("Тест сброшен")
            return
        if not silent:
            self.set_status("Очищено")

    def demo_args(self):
        raw = self.input_var.get().strip()
        if not raw:
            raw = "1 2 3 4 5"
            self.input_var.set(raw)
        try:
            numbers = [float(token) for token in raw.split()]
        except ValueError:
            messagebox.showerror("Ошибка", "Введите числа через пробел")
            return
        total = calculate_sum(*numbers)
        self.set_result("calculate_sum(*{}) = {}".format(numbers, total))
        self.set_status("Демо *args")

    def save_results(self):
        answers_key = [q["answer"] for q in QUIZ_QUESTIONS]
        right, total, percent, answered = score_quiz(self.quiz_answers, answers_key)

        if answered == 0:
            score_text = "тест не пройден"
        elif answered < total:
            score_text = "{}/{} ({:.0f}%) — незавершён ({}/{} ответов)".format(
                right, total, percent, answered, total
            )
        elif self.last_score:
            score_text = self.last_score
        else:
            score_text = "{}/{} ({:.0f}%)".format(right, total, percent)

        user = self.user_var.get().strip() or "студент"
        titles = [t["title"] for t in TOPICS]
        report = format_report(
            Пользователь=user,
            Результат_теста=score_text,
            Темы="; ".join(titles),
            Словарь=str(self.catalog),
        )
        path = default_report_path()
        try:
            save_report(path, report)
        except OSError as e:
            messagebox.showerror("Ошибка", str(e))
            return
        self.set_result(report)
        messagebox.showinfo("Сохранено", "Файл: " + path)
        self.set_status("Сохранено в " + path)

    def show_about(self):
        messagebox.showinfo(
            "О программе",
            "Обучающее приложение по Python.\n"
            "Проектная работа в паре.\n\n" + "\n".join(AUTHORS),
        )

    def clear_radios(self):
        for b in self.radio_buttons:
            b.destroy()
        self.radio_buttons = []

    def set_text(self, widget, value):
        widget.config(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, value)
        widget.config(state=tk.DISABLED)

    def set_result(self, value):
        self.set_text(self.result_text, value)

    def set_status(self, text):
        self.status_var.set(text)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
