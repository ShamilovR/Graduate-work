from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.modalview import ModalView
from kivy.uix.checkbox import CheckBox
import os
import CoordinateDescent
import GradientDescent
import SteepestDescent
import GaussZeidel
import Parser
import Table
import Graphic
import Tests

WIDTH = 900
HEIGHT = 600
BUTTON_WIDTH = 285
BUTTON_HEIGHT = 80
START_POS_FORMULA = 305
LABEL_SHIFT = 47
TEXTINPUT_SHIFT = 37
LABEL_WIDTH = 45
TEXTINPUT_WIDTH = 35
FORMULA_WIDGETS_HEIGHT = 30
active_widgets = []
table_show = False
table = object

def get_table():
    if table_show:
        return table
    else:
        return False

def remove_active_widgets(parent):
    for widget in active_widgets:
        parent.remove_widget(widget)

class Error:
    def show_error_window(self, text):
        window = ModalView(size_hint=(0.6, 0.3))
        window.add_widget(Label(text=text,
                                font_size=20))
        window.open()

class ResultTest:
    def show_result_window(self, text):
        window = ModalView(size_hint=(0.6, 0.3))
        window.add_widget(Label(text=text,
                                font_size=20))
        window.open()

class Information:
    def show_info_window(self):
        text = '1. Выберите интересующий Вас метод\n'
        text += '2. Введите коэффициенты целевой функции\n'
        text += '3. Введите начальное приближение, точность\n и параметры алгортма (если требуется)\n'
        text += 'Важно: десятичные значения требуется\n вводить через точку, а не запятую\n'
        text += 'Важно: количество знаков после точки\n не должно превышать пяти\n'
        text += '4. Выполните первую итерацию вручную\n и введите полученные результаты\n'
        text += 'В случае, если ввод окажется верным\n Вы получите полный итерационный процесс\n'
        text += 'Иначе придется все пересчитать и повторить попытку\n'
        text += 'Примечание: если Вам кажется, что программа\n зависла, то дайте ей минуту подумать\n'

        window = ModalView(size_hint=(0.7, 0.7))
        window.add_widget(Label(text=text,
                                font_size=20))
        window.open()

class InformationForTest:
    def show_info_window(self):
        text = '1. Нажмите "Начать тест" для запуска теста\n'
        text += '2. Выберите вариант ответа и\n нажмите "следующий вопрос"\n'
        text += '3. После прохождения теста, программа\n выдаст количество правильных ответов\n'
        text += 'Примечания:\n'
        text += '1. При каждом запуске программы тест\n можно пройти только один раз\n'
        text += '2. Вернуться к предыдущему вопросу невозможно\n'
        text += '3. Тест сохраняет вопрос, на котором вы остановились\nВсегда можно выйти из теста, для изучения теории\n'

        window = ModalView(size_hint=(0.7, 0.6))
        window.add_widget(Label(text=text,
                                font_size=20))
        window.open()

class MainMenuWidgets:
    def __init__(self):
        self.method = 0
        self.head_label = Label(text="Методы безусловной оптимизации",
                           size=(WIDTH, 40),
                           pos=(0, HEIGHT - 40),
                           font_size=25)
        self.labs_btn = Button(text="Лабораторные работы",
                           size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                           pos=(0, HEIGHT - 130),
                           font_size=20)
        self.theory_btn = Button(text="Теоретический материал",
                            size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                            pos=(0, HEIGHT - 210),
                            font_size=20)
        self.tests_btn = Button(text="Тесты",
                          size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                          pos=(0, HEIGHT - 290),
                          font_size=20)
        self.coordinate_descent_btn = Button(text="Циклический\nпокоординатный спуск",
                                        size=(BUTTON_WIDTH, 80),
                                        pos=(15, HEIGHT - 130),
                                        font_size=20)
        self.gradient_descent_btn = Button(text="Градиентный спуск",
                                      size=(BUTTON_WIDTH, BUTTON_HEIGHT),
                                      pos=(15, HEIGHT - 210),
                                      font_size=20)
        self.steepest_descent_btn = Button(text="Наискорейший спуск",
                               size=(BUTTON_WIDTH, BUTTON_HEIGHT),
                               pos=(15, HEIGHT - 290),
                               font_size=20)
        self.gauss_zeidel_btn = Button(text="Гаусса-Зейделя",
                                           size=(BUTTON_WIDTH, BUTTON_HEIGHT),
                                           pos=(15, HEIGHT - 370),
                                           font_size=20)
        self.reference_btn = Button(text='Справка',
                                    size=(BUTTON_WIDTH, BUTTON_HEIGHT),
                                    pos=(15, HEIGHT - 450),
                                    font_size=20)
        self.back_btn = Button(text="Назад",
                          size=(BUTTON_WIDTH, BUTTON_HEIGHT),
                          pos=(15, HEIGHT - 530),
                          font_size=20)
        self.coordinate_methods_btn = Button(text="Методы циклического\nпокоординатного спуска",
                                             size=(BUTTON_WIDTH + 15, 80),
                                             pos=(0, HEIGHT - 130),
                                             font_size=20)
        self.gradient_methods_btn = Button(text="Градиентные методы",
                                           size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                                           pos=(0, HEIGHT - 210),
                                           font_size=20)
        self.back_theory_btn = Button(text="Назад",
                                           size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                                           pos=(0, HEIGHT - 290),
                                           font_size=20)

        self.reference_btn.bind(on_press=lambda x: self.get_info())
        self.coordinate_methods_btn.bind(on_press=lambda x: self.open_coordinate_file())
        self.gradient_methods_btn.bind(on_press=lambda x: self.open_gradient_file())

    def get_info(self):
        info = Information()
        info.show_info_window()

    def get_theory_btns(self):
        widgets = [self.coordinate_methods_btn, self.gradient_methods_btn, self.back_theory_btn]
        return widgets

    def get_main_menu_buttons(self):
        widgets = [self.labs_btn, self.theory_btn, self.tests_btn]
        return widgets

    def get_methods_buttons(self):
        widgets = [self.coordinate_descent_btn, self.gradient_descent_btn, self.steepest_descent_btn,
                   self.gauss_zeidel_btn, self.reference_btn, self.back_btn]
        return widgets

    def open_gradient_file(self):
        info = Error()
        info.show_error_window('Открытие файла может занять\nкакое-то время.\nПожалуйста, подождите.')
        os.startfile('Градиентные методы.pdf')

    def open_coordinate_file(self):
        info = Error()
        info.show_error_window('Открытие файла может занять\nкакое-то время.\nПожалуйста, подождите.')
        os.startfile('Методы циклического покоординатного спуска.pdf')

class TestWidgets:
    def __init__(self, parent):
        self.pos_x = 320
        self.pos_y = 400
        self.width = 550
        self.height = 50
        self.shift = 50
        self.result_window = ResultTest()
        self.parent = parent
        self.right_answer = 0
        self.active_question = []
        self.test = Tests.Test()
        self.result = []
        self.count = 0
        self.questions = self.test.random_question()
        self.next_btn = Button(text="Начать тест",
                               size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                               pos=(0, HEIGHT - 130),
                               font_size=20)
        self.reference_btn = Button(text="Справка",
                               size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                               pos=(0, HEIGHT - 210),
                               font_size=20)
        self.back_btn = Button(text="Назад",
                               size=(BUTTON_WIDTH + 15, BUTTON_HEIGHT),
                               pos=(0, HEIGHT - 290),
                               font_size=20)
        self.question = Label(text='',
                              size=(550, 100),
                              pos=(310, HEIGHT - 160),
                              halign='center',
                              valign='middle',
                              font_size=20)
        self.question_number = Label(text='',
                                     size=(50, 70),
                                     pos=(830, 0),
                                     font_size=20)
        self.question.text_size = self.question.size
        self.answer1 = Label(text='',
                             pos=(self.pos_x + 30, self.pos_y),
                             size=(self.width, self.height),
                             halign='center',
                             valign='middle',
                             font_size=15)
        self.answer1.text_size = self.answer1.size
        self.answer2 = Label(text='',
                             pos=(self.pos_x + 30, self.pos_y - self.shift),
                             size=(self.width, self.height),
                             halign='center',
                             valign='middle',
                             font_size=15)
        self.answer2.text_size = self.answer2.size
        self.answer3 = Label(text='',
                             pos=(self.pos_x + 30, self.pos_y - 2 * self.shift),
                             size=(self.width, self.height),
                             halign='center',
                             valign='middle',
                             font_size=15)
        self.answer3.text_size = self.answer3.size
        self.answer4 = Label(text='',
                             pos=(self.pos_x + 30, self.pos_y - 3 * self.shift),
                             size=(self.width, self.height),
                             halign='center',
                             valign='middle',
                             font_size=15)
        self.answer4.text_size = self.answer4.size
        self.answer5 = Label(text='',
                             pos=(self.pos_x + 30, self.pos_y - 4 * self.shift),
                             size=(self.width, self.height),
                             halign='center',
                             valign='middle',
                             font_size=15)
        self.answer5.text_size = self.answer5.size
        self.answer6 = Label(text='',
                             pos=(self.pos_x + 30, self.pos_y - 5 * self.shift),
                             size=(self.width, self.height),
                             halign='center',
                             valign='middle',
                             font_size=15)
        self.answer6.text_size = self.answer6.size
        self.checkBox1 = CheckBox()
        self.checkBox2 = CheckBox()
        self.checkBox3 = CheckBox()
        self.checkBox4 = CheckBox()
        self.checkBox5 = CheckBox()
        self.checkBox6 = CheckBox()
        self.radioButton1 = CheckBox(pos=(self.pos_x, self.pos_y),
                                     size=(50, self.height),
                                     group='radioButton')
        self.radioButton2 = CheckBox(pos=(self.pos_x, self.pos_y - self.shift),
                                     size=(50, self.height),
                                     group='radioButton')
        self.radioButton3 = CheckBox(pos=(self.pos_x, self.pos_y - 2 * self.shift),
                                     size=(50, self.height),
                                     group='radioButton')
        self.radioButton4 = CheckBox(pos=(self.pos_x, self.pos_y - 3 * self.shift),
                                     size=(50, self.height),
                                     group='radioButton')
        self.checkBoxs = [self.checkBox1, self.checkBox2, self.checkBox3, self.checkBox4, self.checkBox5, self.checkBox6]
        self.radioButtons = [self.radioButton1, self.radioButton2, self.radioButton3, self.radioButton4]
        self.answers = [self.answer1, self.answer2, self.answer3, self.answer4, self.answer5, self.answer6]

        self.next_btn.bind(on_press=lambda x: self.display_question())
        self.reference_btn.bind(on_press=lambda x: self.get_info())

    def refresh_checkbox(self):
        for rb in self.radioButtons:
            rb.active = False
        for cb in self.checkBoxs:
            cb.active = False

    def get_info(self):
        info = InformationForTest()
        info.show_info_window()

    def display_question(self):
        if len(self.result) != 0:
            for i in self.result:
                if self.radioButtons[i].active:
                    self.right_answer += 1
        for widget in self.active_question:
            self.parent.remove_widget(widget)
        self.result = []
        self.active_question = []

        if self.count == len(self.questions):
            self.result_window.show_result_window('Тест пройден.\nКоличество верных ответов: ' + str(self.right_answer)
                                                  + ' из 42')
            self.question_number.text = ''
            self.next_btn.text = 'Результат'
            return
        self.next_btn.text = 'Следующий вопрос'
        self.question_number.text = str(self.count + 1) + '/42'

        self.refresh_checkbox()

        key = list(self.questions[self.count].keys())[0]
        self.question.text = key
        self.parent.add_widget(self.question)
        self.active_question.append(self.question)
        answers = list(self.questions[self.count].values())[0]
        for i in range(len(answers)):
            self.parent.add_widget(self.radioButtons[i])
            self.active_question.append(self.radioButtons[i])
            self.answers[i].text = list(answers[i].keys())[0]
            self.parent.add_widget(self.answers[i])
            self.active_question.append(self.answers[i])
            if list(answers[i].values())[0]:
                self.result.append(i)
        self.count += 1

    def get_widgets(self):
        for widget in self.active_question:
            self.parent.remove_widget(widget)
        widget = [self.next_btn, self.question_number, self.reference_btn, self.back_btn]
        return widget

class GradientDescentWidgets:
    def __init__(self, parent):
        self.success = False
        self.method = False
        self.coefficients = []
        self.data = []
        self.X = []
        self.eps = 0
        self.alpha = 0
        self.betta = 0
        self.parent = parent
        self.func_label = Label(text="",
                                size=(450, 40),
                                pos=(START_POS_FORMULA + 50, HEIGHT - 220),
                                font_size=20)
        self.first_coefficient = TextInput(text='0',
                                      size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                      pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 120),
                                      background_color=[.2, .2, .2, 1],
                                      foreground_color=[.22, .88, .82, 1],
                                      font_size=15,
                                      write_tab=False,
                                      multiline=False)
        self.second_coefficient = TextInput(text='0',
                                       size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                       pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                                       background_color=[.2, .2, .2, 1],
                                       foreground_color=[.22, .88, .82, 1],
                                       font_size=15,
                                       write_tab=False,
                                       multiline=False)
        self.third_coefficient = TextInput(text='0',
                                      size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                      pos=(START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 120),
                                      background_color=[.2, .2, .2, 1],
                                      foreground_color=[.22, .88, .82, 1],
                                      font_size=15,
                                      write_tab=False,
                                      multiline=False)
        self.fourth_coefficient = TextInput(text='0',
                                       size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                       pos=(START_POS_FORMULA + 4 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT + 5, HEIGHT - 120),
                                       background_color=[.2, .2, .2, 1],
                                       foreground_color=[.22, .88, .82, 1],
                                       font_size=15,
                                       write_tab=False,
                                       multiline=False)
        self.fifth_coefficient = TextInput(text='0',
                                      size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                      pos=(START_POS_FORMULA + 5 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT - 10, HEIGHT - 120),
                                      background_color=[.2, .2, .2, 1],
                                      foreground_color=[.22, .88, .82, 1],
                                      font_size=15,
                                      write_tab=False,
                                      multiline=False)
        self.first_label = Label(text='F(X) = ',
                            size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                            pos=(START_POS_FORMULA, HEIGHT - 120),
                            font_size=15)
        self.second_label = Label(text='X1' + u'\u00B2' + ' + ',
                             size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                             pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                             font_size=15)
        self.third_label = Label(text='X2' + u'\u00B2' + ' + ',
                            size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                            pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 120),
                            font_size=15)
        self.fourth_label = Label(text='X1 + ',
                             size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                             pos=(START_POS_FORMULA + 3 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT + 5, HEIGHT - 120),
                             font_size=15)
        self.fifth_label = Label(text='X2 + ',
                            size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                            pos=(START_POS_FORMULA + 4 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 120),
                            font_size=15)
        self.init_approx_X1_label = Label(text='X1' + u'\u00B0' + ': ',
                                     size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                     pos=(START_POS_FORMULA, HEIGHT - 170),
                                     font_size=15)
        self.init_approx_X2_label = Label(text='X2' + u"\u00B0" + ': ',
                                     size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                     pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                     font_size=15)
        self.init_approx_eps_label = Label(text='ε: ',
                                      size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                      pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                      font_size=15)
        self.init_approx_alpha_label = Label(text='alpha: ',
                                             size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                             pos=(START_POS_FORMULA + 3 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                             font_size=15)
        self.init_approx_betta_label = Label(text='betta: ',
                                             size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                             pos=(
                                             START_POS_FORMULA + 4 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                             font_size=15)
        self.init_approx_X1_input = TextInput(text='0',
                                         size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 170),
                                         background_color=[.2, .2, .2, 1],
                                         foreground_color=[.22, .88, .82, 1],
                                         font_size=15,
                                         write_tab=False,
                                         multiline=False)
        self.init_approx_X2_input = TextInput(text='0',
                                         size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                         background_color=[.2, .2, .2, 1],
                                         foreground_color=[.22, .88, .82, 1],
                                         font_size=15,
                                         write_tab=False,
                                         multiline=False)
        self.init_approx_eps_input = TextInput(text='0',
                                          size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                          background_color=[.2, .2, .2, 1],
                                          foreground_color=[.22, .88, .82, 1],
                                          font_size=15,
                                          write_tab=False,
                                          multiline=False)
        self.init_approx_alpha_input = TextInput(text='0',
                                                 size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                                 pos=(START_POS_FORMULA + 4 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                                 background_color=[.2, .2, .2, 1],
                                                 foreground_color=[.22, .88, .82, 1],
                                                 font_size=15,
                                                 write_tab=False,
                                                 multiline=False)
        self.init_approx_betta_input = TextInput(text='0',
                                                 size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                                 pos=(START_POS_FORMULA + 5 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT,
                                                      HEIGHT - 170),
                                                 background_color=[.2, .2, .2, 1],
                                                 foreground_color=[.22, .88, .82, 1],
                                                 font_size=15,
                                                 write_tab=False,
                                                 multiline=False)

        self.first_step_X1_label = Label(text='X1' + u'\u00B9' + ': ',
                                          size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA, HEIGHT - 220),
                                          font_size=15)
        self.first_step_X1_coefficient = TextInput(text='0',
                                            size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                            pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 220),
                                            background_color=[.2, .2, .2, 1],
                                            foreground_color=[.22, .88, .82, 1],
                                            font_size=15,
                                            write_tab=False,
                                            multiline=False)
        self.first_step_X2_label = Label(text='X2' + u'\u00B9' + ': ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT * 2, HEIGHT - 220),
                                         font_size=15)
        self.first_step_X2_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT * 2, HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.first_step_Fx_label = Label(text='F(X' + u'\u00B9' + '): ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 220),
                                         font_size=15)
        self.first_step_Fx_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(
                                                   START_POS_FORMULA + 3 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)

        self.decision_btn = Button(text="Решение",
                              size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                              pos=(WIDTH / 3, 0),
                              font_size=20)

        self.graph_btn = Button(text="График",
                           size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                           pos=(WIDTH / 3 * 2 - 100, 0),
                           font_size=20)
        self.first_step_btn = Button(text="Первый шаг",
                                size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                pos=(WIDTH - 200, 0),
                                font_size=20)

        self.decision_btn.bind(on_press=lambda x: self.gradient_method_decision())
        self.graph_btn.bind(on_press=lambda x: self.graph())
        self.first_step_btn.bind(on_press=lambda x: self.first_step())

    def get_coeff(self):
        coefficients = [self.first_coefficient, self.second_coefficient, self.third_coefficient,
                        self.fourth_coefficient, self.fifth_coefficient]
        return coefficients

    def get_X(self):
        X = [self.init_approx_X1_input, self.init_approx_X2_input]
        return X

    def get_first_step_widgets(self):
        widgets = [self.first_step_X1_label, self.first_step_X1_coefficient, self.first_step_X2_label,
                   self.first_step_X2_coefficient, self.first_step_Fx_label, self.first_step_Fx_coefficient]
        return widgets

    def get_widgets(self):
        widgets = [self.first_label, self.first_coefficient, self.second_label, self.second_coefficient,
                   self.third_label, self.third_coefficient, self.fourth_label, self.fourth_coefficient,
                   self.fifth_label, self.fifth_coefficient,
                   self.init_approx_X1_label, self.init_approx_X1_input, self.init_approx_X2_label,
                   self.init_approx_X2_input, self.init_approx_eps_label, self.init_approx_eps_input,
                   self.decision_btn, self.graph_btn, self.first_step_btn, self.init_approx_alpha_label, self.init_approx_alpha_input,
                   self.init_approx_betta_label, self.init_approx_betta_input, self.func_label]
        return widgets

    def first_step(self):
        global table, table_show
        self.coefficients = []
        self.X = []
        self.func_label.text = ''
        error = Error()
        self.success = False
        self.method = False
        if table_show:
            self.parent.remove_widget(table)
            table_show = False
        for coefficient in self.get_coeff():
            if not Parser.check_length(coefficient.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(coefficient.text):
                self.coefficients.append(float(coefficient.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        for x in self.get_X():
            if not Parser.check_length(x.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(x.text):
                self.X.append(float(x.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        if Parser.is_number(self.init_approx_eps_input.text):
            self.eps = float(self.init_approx_eps_input.text)
            if self.eps <= 0:
                error.show_error_window('Значение точности должно\n быть положительным')
                return False
        else:
            error.show_error_window('Введенное значение точности\n не является числом')
            return False

        if Parser.is_number(self.init_approx_alpha_input.text):
            self.alpha = float(self.init_approx_alpha_input.text)
            if self.alpha < 0:
                error.show_error_window('Значение начального шага \nне может быть меньше нуля')
                return False
        else:
            error.show_error_window('Введенное значение начального шага\n не является числом')
            return False

        if Parser.is_number(self.init_approx_betta_input.text):
            self.betta = float(self.init_approx_betta_input.text)
            if (self.betta >= 1) or (self.betta < 0):
                error.show_error_window('Значение параметра алгоритма не может быть\n больше единицы или меньше нуля')
                return False
        else:
            error.show_error_window('Введенное значение параметра алгоритма\n не является числом')
            return False

        self.success = True
        remove_active_widgets(self.parent)
        for widget in self.get_first_step_widgets():
            self.parent.add_widget(widget)
            active_widgets.append(widget)

        self.method = GradientDescent.GradientDescent(self.eps, self.alpha, self.betta, self.X, self.coefficients)
        self.data = self.method.iteration_proccess()

    def gradient_method_decision(self):
        global table, table_show
        self.func_label.text = ''
        error = Error()
        if table_show:
            self.parent.remove_widget(table)
            table_show = False

        if self.success:
            if str(self.method.first_step_result[0]) != self.first_step_X1_coefficient.text:
                error.show_error_window('Введено неверное значение Х1 первой итерации')
                return False
            if str(self.method.first_step_result[1]) != self.first_step_X2_coefficient.text:
                error.show_error_window('Введено неверное значение Х2 первой итерации')
                return False
            if str(self.method.first_step_result[2]) != self.first_step_Fx_coefficient.text:
                error.show_error_window('Введено неверное значение целевой\nфункции первой итерации')
                return False
        else:
            error.show_error_window('Необходимо выполнить первый шаг вручную')
            return False

        remove_active_widgets(self.parent)
        table = Table.RV(self.data)
        self.parent.add_widget(table)
        table_show = True
        self.func_label.text = 'F(X) = ' + str(self.coefficients[0]) + '*X1' + u'\u00B2' + ' + ' + str(self.coefficients[1]) \
                          + '*X2' + u'\u00B2' + ' + ' + str(self.coefficients[2]) + '*X1 + ' + str(self.coefficients[3]) \
                          + '*X2 + ' + str(self.coefficients[4])

    def graph(self):
        if not self.method:
            error = Error()
            error.show_error_window('Для построения графика необходимо\nвыполнить итерационный процесс')
        else:
            graphic = Graphic.CreateGraph(self.method.z_array, self.method.x_array, self.method.y_array,
                                          'Градиентный спуск')
            graphic.create_graph()


class SteepestDescentWidgets:
    def __init__(self, parent):
        self.method = False
        self.success = False
        self.data = []
        self.coefficients = []
        self.data = []
        self.X = []
        self.eps = 0
        self.parent = parent
        self.func_label = Label(text="",
                                size=(450, 40),
                                pos=(START_POS_FORMULA + 50, HEIGHT - 220),
                                font_size=20)
        self.first_coefficient = TextInput(text='0',
                                           size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 120),
                                           background_color=[.2, .2, .2, 1],
                                           foreground_color=[.22, .88, .82, 1],
                                           font_size=15,
                                           write_tab=False,
                                           multiline=False)
        self.second_coefficient = TextInput(text='0',
                                            size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                            pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                                            background_color=[.2, .2, .2, 1],
                                            foreground_color=[.22, .88, .82, 1],
                                            font_size=15,
                                            write_tab=False,
                                            multiline=False)
        self.third_coefficient = TextInput(text='0',
                                           size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(
                                           START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 120),
                                           background_color=[.2, .2, .2, 1],
                                           foreground_color=[.22, .88, .82, 1],
                                           font_size=15,
                                           write_tab=False,
                                           multiline=False)
        self.fourth_coefficient = TextInput(text='0',
                                            size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                            pos=(START_POS_FORMULA + 4 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT + 5,
                                                 HEIGHT - 120),
                                            background_color=[.2, .2, .2, 1],
                                            foreground_color=[.22, .88, .82, 1],
                                            font_size=15,
                                            write_tab=False,
                                            multiline=False)
        self.fifth_coefficient = TextInput(text='0',
                                           size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(START_POS_FORMULA + 5 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT - 10,
                                                HEIGHT - 120),
                                           background_color=[.2, .2, .2, 1],
                                           foreground_color=[.22, .88, .82, 1],
                                           font_size=15,
                                           write_tab=False,
                                           multiline=False)
        self.first_label = Label(text='F(X) = ',
                                 size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                 pos=(START_POS_FORMULA, HEIGHT - 120),
                                 font_size=15)
        self.second_label = Label(text='X1' + u'\u00B2' + ' + ',
                                  size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                  pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                                  font_size=15)
        self.third_label = Label(text='X2' + u'\u00B2' + ' + ',
                                 size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                 pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 120),
                                 font_size=15)
        self.fourth_label = Label(text='X1 + ',
                                  size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                  pos=(START_POS_FORMULA + 3 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT + 5, HEIGHT - 120),
                                  font_size=15)
        self.fifth_label = Label(text='X2 + ',
                                 size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                 pos=(START_POS_FORMULA + 4 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 120),
                                 font_size=15)
        self.init_approx_X1_label = Label(text='X1' + u'\u00B0' + ': ',
                                          size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA, HEIGHT - 170),
                                          font_size=15)
        self.init_approx_X2_label = Label(text='X2' + u'\u00B0' + ': ',
                                          size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                          font_size=15)
        self.init_approx_eps_label = Label(text='ε: ',
                                           size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(
                                           START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                           font_size=15)
        self.init_approx_X1_input = TextInput(text='0',
                                              size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                              pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 170),
                                              background_color=[.2, .2, .2, 1],
                                              foreground_color=[.22, .88, .82, 1],
                                              font_size=15,
                                              write_tab=False,
                                              multiline=False)
        self.init_approx_X2_input = TextInput(text='0',
                                              size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                              pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                              background_color=[.2, .2, .2, 1],
                                              foreground_color=[.22, .88, .82, 1],
                                              font_size=15,
                                              write_tab=False,
                                              multiline=False)
        self.init_approx_eps_input = TextInput(text='0',
                                               size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                               pos=(
                                               START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                               background_color=[.2, .2, .2, 1],
                                               foreground_color=[.22, .88, .82, 1],
                                               font_size=15,
                                               write_tab=False,
                                               multiline=False)
        self.first_step_X1_label = Label(text='X1' + u'\u00B9' + ': ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA, HEIGHT - 220),
                                         font_size=15)
        self.first_step_X1_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.first_step_X2_label = Label(text='X2' + u'\u00B9' + ': ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT * 2, HEIGHT - 220),
                                         font_size=15)
        self.first_step_X2_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT * 2,
                                                        HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.first_step_Fx_label = Label(text='F(X' + u'\u00B9' + '): ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 220),
                                         font_size=15)
        self.first_step_Fx_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(
                                                       START_POS_FORMULA + 3 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT,
                                                       HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.decision_btn = Button(text="Решение",
                                   size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                   pos=(WIDTH / 3, 0),
                                   font_size=20)

        self.graph_btn = Button(text="График",
                                size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                pos=(WIDTH / 3 * 2 - 100, 0),
                                font_size=20)
        self.first_step_btn = Button(text="Первый шаг",
                                     size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                     pos=(WIDTH - 200, 0),
                                     font_size=20)

        self.decision_btn.bind(on_press=lambda x: self.steepest_method_decision())
        self.graph_btn.bind(on_press=lambda x: self.graph())
        self.first_step_btn.bind(on_press=lambda x: self.first_step())

    def get_widgets(self):
        widgets = [self.first_label, self.first_coefficient, self.second_label, self.second_coefficient,
                   self.third_label, self.third_coefficient, self.fourth_label, self.fourth_coefficient,
                   self.fifth_label, self.fifth_coefficient,
                   self.init_approx_X1_label, self.init_approx_X1_input, self.init_approx_X2_label,
                   self.init_approx_X2_input, self.init_approx_eps_label, self.init_approx_eps_input,
                   self.decision_btn, self.graph_btn, self.first_step_btn, self.func_label]
        return widgets

    def get_first_step_widgets(self):
        widgets = [self.first_step_X1_label, self.first_step_X1_coefficient, self.first_step_X2_label,
                   self.first_step_X2_coefficient, self.first_step_Fx_label, self.first_step_Fx_coefficient]
        return widgets

    def get_coeff(self):
        coefficients = [self.first_coefficient, self.second_coefficient, self.third_coefficient,
                        self.fourth_coefficient, self.fifth_coefficient]
        return coefficients

    def get_X(self):
        X = [self.init_approx_X1_input, self.init_approx_X2_input]
        return X

    def first_step(self):
        global table, table_show
        self.coefficients = []
        self.X = []
        self.func_label.text = ''
        error = Error()
        self.success = False
        self.method = False
        if table_show:
            self.parent.remove_widget(table)
            table_show = False
        for coefficient in self.get_coeff():
            if not Parser.check_length(coefficient.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(coefficient.text):
                self.coefficients.append(float(coefficient.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        for x in self.get_X():
            if not Parser.check_length(x.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(x.text):
                self.X.append(float(x.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        if Parser.is_number(self.init_approx_eps_input.text):
            self.eps = float(self.init_approx_eps_input.text)
            if self.eps <= 0:
                error.show_error_window('Значение точности должно\n быть положительным')
                return False
        else:
            error.show_error_window('Введенное значение точности\n не является числом')
            return False

        self.success = True
        remove_active_widgets(self.parent)
        for widget in self.get_first_step_widgets():
            self.parent.add_widget(widget)
            active_widgets.append(widget)

        self.method = SteepestDescent.SteepestDescent(self.eps, self.X, self.coefficients)
        self.data = self.method.iteration_proccess()

    def steepest_method_decision(self):
        global table, table_show
        self.func_label.text = ''
        error = Error()
        if table_show:
            self.parent.remove_widget(table)
            table_show = False

        if self.success:
            if str(self.method.first_step_result[0]) != self.first_step_X1_coefficient.text:
                error.show_error_window('Введено неверное значение Х1 первой итерации')
                return False
            if str(self.method.first_step_result[1]) != self.first_step_X2_coefficient.text:
                error.show_error_window('Введено неверное значение Х2 первой итерации')
                return False
            if str(self.method.first_step_result[2]) != self.first_step_Fx_coefficient.text:
                error.show_error_window('Введено неверное значение целевой\nфункции первой итерации')
                return False
        else:
            error.show_error_window('Необходимо выполнить первый шаг вручную')
            return False

        remove_active_widgets(self.parent)
        table = Table.RV(self.data)
        self.parent.add_widget(table)
        table_show = True
        self.func_label.text = 'F(X) = ' + str(self.coefficients[0]) + '*X1' + u'\u00B2' + ' + ' + str(
            self.coefficients[1]) \
                               + '*X2' + u'\u00B2' + ' + ' + str(self.coefficients[2]) + '*X1 + ' + str(
            self.coefficients[3]) \
                               + '*X2 + ' + str(self.coefficients[4])

    def graph(self):
        if not self.method:
            error = Error()
            error.show_error_window('Для построения графика необходимо\nвыполнить итерационный процесс')
        else:
            graphic = Graphic.CreateGraph(self.method.z_array, self.method.x_array, self.method.y_array,
                                          'Градиентный спуск')
            graphic.create_graph()


class GaussZeidelWidgets():
    def __init__(self, parent):
        self.method = False
        self.success = False
        self.data = []
        self.eps = 0
        self.X = []
        self.coefficients = []
        self.parent = parent
        self.func_label = Label(text="",
                                size=(450, 40),
                                pos=(START_POS_FORMULA + 50, HEIGHT - 220),
                                font_size=20)
        self.first_coefficient = TextInput(text='0',
                                           size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 120),
                                           background_color=[.2, .2, .2, 1],
                                           foreground_color=[.22, .88, .82, 1],
                                           font_size=15,
                                           write_tab=False,
                                           multiline=False)
        self.second_coefficient = TextInput(text='0',
                                            size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                            pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                                            background_color=[.2, .2, .2, 1],
                                            foreground_color=[.22, .88, .82, 1],
                                            font_size=15,
                                            write_tab=False,
                                            multiline=False)
        self.third_coefficient = TextInput(text='0',
                                           size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(
                                               START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 120),
                                           background_color=[.2, .2, .2, 1],
                                           foreground_color=[.22, .88, .82, 1],
                                           font_size=15,
                                           write_tab=False,
                                           multiline=False)
        self.first_label = Label(text='F(X) = ',
                                 size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                 pos=(START_POS_FORMULA, HEIGHT - 120),
                                 font_size=15)
        self.second_label = Label(text='X1' + u'\u00B2' + ' + ',
                                  size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                  pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                                  font_size=15)
        self.third_label = Label(text='X2' + u'\u00B2' + ' + ',
                                 size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                 pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 120),
                                 font_size=15)
        self.fourth_label = Label(text='X1*X2',
                                  size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                  pos=(START_POS_FORMULA + 3 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT + 5, HEIGHT - 120),
                                  font_size=15)
        self.init_approx_X1_label = Label(text='X1' + u'\u00B0' + ': ',
                                          size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA, HEIGHT - 170),
                                          font_size=15)
        self.init_approx_X2_label = Label(text='X2' + u'\u00B0' + ': ',
                                          size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                          font_size=15)
        self.init_approx_eps_label = Label(text='ε: ',
                                           size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(
                                               START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                           font_size=15)
        self.init_approx_X1_input = TextInput(text='0',
                                              size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                              pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 170),
                                              background_color=[.2, .2, .2, 1],
                                              foreground_color=[.22, .88, .82, 1],
                                              font_size=15,
                                              write_tab=False,
                                              multiline=False)
        self.init_approx_X2_input = TextInput(text='0',
                                              size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                              pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                              background_color=[.2, .2, .2, 1],
                                              foreground_color=[.22, .88, .82, 1],
                                              font_size=15,
                                              write_tab=False,
                                              multiline=False)
        self.init_approx_eps_input = TextInput(text='0',
                                               size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                               pos=(
                                                   START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT,
                                                   HEIGHT - 170),
                                               background_color=[.2, .2, .2, 1],
                                               foreground_color=[.22, .88, .82, 1],
                                               font_size=15,
                                               write_tab=False,
                                               multiline=False)
        self.first_step_X1_label = Label(text='X1' + u'\u00B9' + ': ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA, HEIGHT - 220),
                                         font_size=15)
        self.first_step_X1_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.first_step_X2_label = Label(text='X2' + u'\u00B9' + ': ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT * 2, HEIGHT - 220),
                                         font_size=15)
        self.first_step_X2_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT * 2,
                                                        HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.first_step_Fx_label = Label(text='F(X' + u'\u00B9' + '): ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 220),
                                         font_size=15)
        self.first_step_Fx_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(
                                                       START_POS_FORMULA + 3 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT,
                                                       HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)

        self.decision_btn = Button(text="Решение",
                                   size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                   pos=(WIDTH / 3, 0),
                                   font_size=20)

        self.graph_btn = Button(text="График",
                                size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                pos=(WIDTH / 3 * 2 - 100, 0),
                                font_size=20)
        self.first_step_btn = Button(text="Первый шаг",
                                     size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                     pos=(WIDTH - 200, 0),
                                     font_size=20)

        self.decision_btn.bind(on_press=lambda x: self.gauss_zeidel_decision())
        self.graph_btn.bind(on_press=lambda x: self.graph())
        self.first_step_btn.bind(on_press=lambda x: self.first_step())

    def get_widgets(self):
        widgets = [self.first_label, self.first_coefficient, self.second_label, self.second_coefficient,
                   self.third_label, self.third_coefficient, self.fourth_label,
                   self.init_approx_X1_label, self.init_approx_X1_input, self.init_approx_X2_label,
                   self.init_approx_X2_input, self.init_approx_eps_label, self.init_approx_eps_input,
                   self.decision_btn, self.graph_btn, self.first_step_btn, self.func_label]
        return widgets

    def get_coeff(self):
        coefficients = [self.first_coefficient, self.second_coefficient, self.third_coefficient]
        return coefficients

    def get_first_step_widgets(self):
        widgets = [self.first_step_X1_label, self.first_step_X1_coefficient, self.first_step_X2_label,
                   self.first_step_X2_coefficient, self.first_step_Fx_label, self.first_step_Fx_coefficient]
        return widgets

    def get_X(self):
        X = [self.init_approx_X1_input, self.init_approx_X2_input]
        return X

    def first_step(self):
        global table, table_show
        self.coefficients = []
        self.X = []
        self.func_label.text = ''
        error = Error()
        self.success = False
        self.method = False
        if table_show:
            self.parent.remove_widget(table)
            table_show = False
        for coefficient in self.get_coeff():
            if not Parser.check_length(coefficient.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(coefficient.text):
                self.coefficients.append(float(coefficient.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        for x in self.get_X():
            if not Parser.check_length(x.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(x.text):
                self.X.append(float(x.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        if Parser.is_number(self.init_approx_eps_input.text):
            self.eps = float(self.init_approx_eps_input.text)
            if self.eps <= 0:
                error.show_error_window('Значение точности должно\n быть положительным')
                return False
        else:
            error.show_error_window('Введенное значение точности\n не является числом')
            return False

        self.success = True
        remove_active_widgets(self.parent)
        for widget in self.get_first_step_widgets():
            self.parent.add_widget(widget)
            active_widgets.append(widget)

        self.method = GaussZeidel.GaussZeidel(self.eps, self.X, self.coefficients)
        self.data = self.method.iteration_proccess()

    def gauss_zeidel_decision(self):
        global table, table_show
        self.func_label.text = ''
        error = Error()
        if table_show:
            self.parent.remove_widget(table)
            table_show = False

        if self.success:
            if str(self.method.first_step_result[0]) != self.first_step_X1_coefficient.text:
                error.show_error_window('Введено неверное значение Х1 первой итерации')
                return False
            if str(self.method.first_step_result[1]) != self.first_step_X2_coefficient.text:
                error.show_error_window('Введено неверное значение Х2 первой итерации')
                return False
            if str(self.method.first_step_result[2]) != self.first_step_Fx_coefficient.text:
                error.show_error_window('Введено неверное значение целевой\nфункции первой итерации')
                return False
        else:
            error.show_error_window('Необходимо выполнить первый шаг вручную')
            return False

        remove_active_widgets(self.parent)
        table = Table.RV(self.data)
        self.parent.add_widget(table)
        table_show = True
        self.func_label.text = 'F(X) = ' + str(self.coefficients[0]) + '*X1' + u'\u00B2' + ' + ' + str(
            self.coefficients[1]) \
                               + '*X2' + u'\u00B2' + ' + ' + str(self.coefficients[2]) + '*X1*X2'

    def graph(self):
        if not self.method:
            error = Error()
            error.show_error_window('Для построения графика необходимо\nвыполнить итерационный процесс')
        else:
            graphic = Graphic.CreateGraph(self.method.z_array, self.method.x_array, self.method.y_array,
                                          'Гаусса-Зейделя')
            graphic.create_graph()

class CoordinateDescentWidgets:
    def __init__(self, parent):
        self.method = False
        self.success = False
        self.data = []
        self.eps = 0
        self.alpha = 0
        self.betta = 0
        self.X = []
        self.coefficients = []
        self.parent = parent
        self.func_label = Label(text="",
                                size=(450, 40),
                                pos=(START_POS_FORMULA + 50, HEIGHT - 220),
                                font_size=20)
        self.first_coefficient = TextInput(text='0',
                                           size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 120),
                                           background_color=[.2, .2, .2, 1],
                                           foreground_color=[.22, .88, .82, 1],
                                           font_size=15,
                                           write_tab=False,
                                           multiline=False)
        self.second_coefficient = TextInput(text='0',
                                            size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                            pos=(
                                            START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                                            background_color=[.2, .2, .2, 1],
                                            foreground_color=[.22, .88, .82, 1],
                                            font_size=15,
                                            write_tab=False,
                                            multiline=False)
        self.third_coefficient = TextInput(text='0',
                                           size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(
                                               START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT,
                                               HEIGHT - 120),
                                           background_color=[.2, .2, .2, 1],
                                           foreground_color=[.22, .88, .82, 1],
                                           font_size=15,
                                           write_tab=False,
                                           multiline=False)
        self.first_label = Label(text='F(X) = ',
                                 size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                 pos=(START_POS_FORMULA, HEIGHT - 120),
                                 font_size=15)
        self.second_label = Label(text='X1' + u'\u00B2' + ' + ',
                                  size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                  pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 120),
                                  font_size=15)
        self.third_label = Label(text='X2' + u'\u00B2' + ' + ',
                                 size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                 pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT, HEIGHT - 120),
                                 font_size=15)
        self.fourth_label = Label(text='X1*X2',
                                  size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                  pos=(START_POS_FORMULA + 3 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT + 5, HEIGHT - 120),
                                  font_size=15)
        self.init_approx_X1_label = Label(text='X1' + u'\u00B0' + ': ',
                                          size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA, HEIGHT - 170),
                                          font_size=15)
        self.init_approx_X2_label = Label(text='X2' + u'\u00B0' + ': ',
                                          size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                          pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                          font_size=15)
        self.init_approx_eps_label = Label(text='ε: ',
                                           size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                           pos=(
                                               START_POS_FORMULA + 2 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT,
                                               HEIGHT - 170),
                                           font_size=15)
        self.init_approx_alpha_label = Label(text='alpha: ',
                                             size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                             pos=(
                                             START_POS_FORMULA + 3 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT, HEIGHT - 170),
                                             font_size=15)
        self.init_approx_betta_label = Label(text='betta: ',
                                             size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                             pos=(
                                                 START_POS_FORMULA + 4 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT,
                                                 HEIGHT - 170),
                                             font_size=15)
        self.init_approx_X1_input = TextInput(text='0',
                                              size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                              pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 170),
                                              background_color=[.2, .2, .2, 1],
                                              foreground_color=[.22, .88, .82, 1],
                                              font_size=15,
                                              write_tab=False,
                                              multiline=False)
        self.init_approx_X2_input = TextInput(text='0',
                                              size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                              pos=(
                                              START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT, HEIGHT - 170),
                                              background_color=[.2, .2, .2, 1],
                                              foreground_color=[.22, .88, .82, 1],
                                              font_size=15,
                                              write_tab=False,
                                              multiline=False)
        self.init_approx_eps_input = TextInput(text='0',
                                               size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                               pos=(
                                                   START_POS_FORMULA + 3 * LABEL_SHIFT + 2 * TEXTINPUT_SHIFT,
                                                   HEIGHT - 170),
                                               background_color=[.2, .2, .2, 1],
                                               foreground_color=[.22, .88, .82, 1],
                                               font_size=15,
                                               write_tab=False,
                                               multiline=False)
        self.init_approx_alpha_input = TextInput(text='0',
                                                 size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                                 pos=(START_POS_FORMULA + 4 * LABEL_SHIFT + 3 * TEXTINPUT_SHIFT,
                                                      HEIGHT - 170),
                                                 background_color=[.2, .2, .2, 1],
                                                 foreground_color=[.22, .88, .82, 1],
                                                 font_size=15,
                                                 write_tab=False,
                                                 multiline=False)
        self.init_approx_betta_input = TextInput(text='0',
                                                 size=(TEXTINPUT_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                                 pos=(START_POS_FORMULA + 5 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT,
                                                      HEIGHT - 170),
                                                 background_color=[.2, .2, .2, 1],
                                                 foreground_color=[.22, .88, .82, 1],
                                                 font_size=15,
                                                 write_tab=False,
                                                 multiline=False)
        self.first_step_X1_label = Label(text='X1' + u'\u00B9' + ': ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA, HEIGHT - 220),
                                         font_size=15)
        self.first_step_X1_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(START_POS_FORMULA + LABEL_SHIFT, HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.first_step_X2_label = Label(text='X2' + u'\u00B9' + ': ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + LABEL_SHIFT + TEXTINPUT_SHIFT * 2, HEIGHT - 220),
                                         font_size=15)
        self.first_step_X2_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + TEXTINPUT_SHIFT * 2,
                                                        HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)
        self.first_step_Fx_label = Label(text='F(X' + u'\u00B9' + '): ',
                                         size=(LABEL_WIDTH, FORMULA_WIDGETS_HEIGHT),
                                         pos=(START_POS_FORMULA + 2 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT, HEIGHT - 220),
                                         font_size=15)
        self.first_step_Fx_coefficient = TextInput(text='0',
                                                   size=(TEXTINPUT_WIDTH * 2, FORMULA_WIDGETS_HEIGHT),
                                                   pos=(
                                                       START_POS_FORMULA + 3 * LABEL_SHIFT + 4 * TEXTINPUT_SHIFT,
                                                       HEIGHT - 220),
                                                   background_color=[.2, .2, .2, 1],
                                                   foreground_color=[.22, .88, .82, 1],
                                                   font_size=15,
                                                   write_tab=False,
                                                   multiline=False)

        self.decision_btn = Button(text="Решение",
                                   size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                   pos=(WIDTH / 3, 0),
                                   font_size=20)

        self.graph_btn = Button(text="График",
                                size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                pos=(WIDTH / 3 * 2 - 100, 0),
                                font_size=20)
        self.first_step_btn = Button(text="Первый шаг",
                                     size=(WIDTH / 3 - 100, BUTTON_HEIGHT),
                                     pos=(WIDTH - 200, 0),
                                     font_size=20)

        self.decision_btn.bind(on_press=lambda x: self.coordinate_descent_decision())
        self.graph_btn.bind(on_press=lambda x: self.graph())
        self.first_step_btn.bind(on_press=lambda x: self.first_step())

    def get_widgets(self):
        widgets = [self.first_label, self.first_coefficient, self.second_label, self.second_coefficient,
                   self.third_label, self.third_coefficient, self.fourth_label,
                   self.init_approx_X1_label, self.init_approx_X1_input, self.init_approx_X2_label,
                   self.init_approx_X2_input, self.init_approx_eps_label, self.init_approx_eps_input,
                   self.init_approx_alpha_label, self.init_approx_alpha_input, self.init_approx_betta_label,
                   self.init_approx_betta_input, self.decision_btn, self.graph_btn, self.first_step_btn, self.func_label]
        return widgets

    def get_coeff(self):
        coefficients = [self.first_coefficient, self.second_coefficient, self.third_coefficient]
        return coefficients

    def get_first_step_widgets(self):
        widgets = [self.first_step_X1_label, self.first_step_X1_coefficient, self.first_step_X2_label,
                   self.first_step_X2_coefficient, self.first_step_Fx_label, self.first_step_Fx_coefficient]
        return widgets

    def get_X(self):
        X = [self.init_approx_X1_input, self.init_approx_X2_input]
        return X

    def first_step(self):
        global table, table_show
        self.coefficients = []
        self.X = []
        self.func_label.text = ''
        error = Error()
        self.success = False
        self.method = False
        if table_show:
            self.parent.remove_widget(table)
            table_show = False
        for coefficient in self.get_coeff():
            if not Parser.check_length(coefficient.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(coefficient.text):
                self.coefficients.append(float(coefficient.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        for x in self.get_X():
            if not Parser.check_length(x.text):
                error.show_error_window('Введено слишком большое значение')
                return False
            if Parser.is_number(x.text):
                self.X.append(float(x.text))
            else:
                error.show_error_window('Введеное значение не является числом')
                return False

        if Parser.is_number(self.init_approx_eps_input.text):
            self.eps = float(self.init_approx_eps_input.text)
            if self.eps <= 0:
                error.show_error_window('Значение точности должно\n быть положительным')
                return False
        else:
            error.show_error_window('Введенное значение точности\n не является числом')
            return False

        if Parser.is_number(self.init_approx_alpha_input.text):
            self.alpha = float(self.init_approx_alpha_input.text)
            if self.alpha < 0:
                error.show_error_window('Значение начального шага \nне может быть меньше нуля')
                return False
        else:
            error.show_error_window('Введенное значение начального шага\n не является числом')
            return False

        if Parser.is_number(self.init_approx_betta_input.text):
            self.betta = float(self.init_approx_betta_input.text)
            if (self.betta >= 1) or (self.betta < 0):
                error.show_error_window('Значение параметра алгоритма не может быть\n больше единицы или меньше нуля')
                return False
        else:
            error.show_error_window('Введенное значение параметра алгоритма\n не является числом')
            return False

        self.success = True
        remove_active_widgets(self.parent)
        for widget in self.get_first_step_widgets():
            self.parent.add_widget(widget)
            active_widgets.append(widget)

        self.method = CoordinateDescent.CoordinateDescent(self.eps, self.alpha, self.betta, self.X, self.coefficients)
        self.data = self.method.iteration_proccess()

    def coordinate_descent_decision(self):
        global table, table_show
        self.func_label.text = ''
        error = Error()
        if table_show:
            self.parent.remove_widget(table)
            table_show = False

        if self.success:
            if str(self.method.first_step_result[0]) != self.first_step_X1_coefficient.text:
                error.show_error_window('Введено неверное значение Х1 первой итерации')
                return False
            if str(self.method.first_step_result[1]) != self.first_step_X2_coefficient.text:
                error.show_error_window('Введено неверное значение Х2 первой итерации')
                return False
            if str(self.method.first_step_result[2]) != self.first_step_Fx_coefficient.text:
                error.show_error_window('Введено неверное значение целевой\nфункции первой итерации')
                return False
        else:
            error.show_error_window('Необходимо выполнить первый шаг вручную')
            return False

        remove_active_widgets(self.parent)
        table = Table.RV(self.data)
        self.parent.add_widget(table)
        table_show = True
        self.func_label.text = 'F(X) = ' + str(self.coefficients[0]) + '*X1' + u'\u00B2' + ' + ' + str(
            self.coefficients[1]) \
                               + '*X2' + u'\u00B2' + ' + ' + str(self.coefficients[2]) + '*X1*X2'

    def graph(self):
        if not self.method:
            error = Error()
            error.show_error_window('Для построения графика необходимо\nвыполнить итерационный процесс')
        else:
            graphic = Graphic.CreateGraph(self.method.z_array, self.method.x_array, self.method.y_array,
                                          'Циклический покоординатный спуск')
            graphic.create_graph()

