import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain, width: int = 600, height: int = 500):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.config(width=width, height=height, bg=THEME_COLOR, padx=20, pady=20)
        self.window.title('Quiz game')
        self.canvas = tk.Canvas(width=width // 2, height=height // 2, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text='Question',
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'normal'),
                                                     width=280)

        true_image = tk.PhotoImage(file='images/true.png')
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.press_true)
        self.true_button.grid(row=2, column=0)

        false_image = tk.PhotoImage(file='images/false.png')
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.press_false)
        self.false_button.grid(row=2, column=1)

        self.score_label = tk.Label(text=f'Score : {self.quiz.score}',
                                    highlightthickness=0,
                                    bg=THEME_COLOR,
                                    fg='white',
                                    font=('Arial', 20, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.get_next_question()
        self.window.mainloop()

    def press_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def get_next_question(self):
        self.change_color('white')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def change_color(self, color: str='white'):
        self.canvas.config(bg=color)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.window.after(ms=1000, func=self.change_color('lightgreen'))
        else:
            self.window.after(ms=1000, func=self.change_color('red'))

        self.window.after(ms=1000, func=self.get_next_question)
        self.score_label.config(text=f'Score : {self.quiz.score}')
