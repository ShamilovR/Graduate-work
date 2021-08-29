from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '600')
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle)
import Widgets

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
active_widgets_for_method = []



class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(.22, .88, .82)
            Rectangle(pos=(0, HEIGHT - 40), size=(WIDTH, 40))
        with self.canvas:
            Color(.18, .71, .71)
            Rectangle(pos=(0, HEIGHT - 50), size=(WIDTH, 10))
        with self.canvas:
            Color(.1, .1, .1)
            Rectangle(pos=(0, 0), size=(WIDTH / 3, HEIGHT - 50))
        with self.canvas:
            Color(.15, .15, .15)
            Rectangle(pos=(WIDTH / 3, 0), size=(WIDTH - WIDTH / 3, HEIGHT - 50))


class KAIApp(App):
    slider_pos_y = 0

    def remove_active_widgets(self, parent):
        Widgets.remove_active_widgets(parent)
        for i in range(len(active_widgets_for_method)):
            parent.remove_widget(active_widgets_for_method[i])

    def remove_slider(self, parent):
        with parent.canvas:
            Color(.1, .1, .1)
            Rectangle(pos=(0, self.slider_pos_y), size=(15, 80))

    def slider_move(self, parent, pos_y):
        self.remove_slider(parent)
        self.slider_pos_y = pos_y
        with parent.canvas:
            Color(.22, .88, .82)
            Rectangle(pos=(0, pos_y), size=(15, 80))

    def display_button(self, parent, old_btns, new_btns):
        self.remove_slider(parent)
        self.remove_active_widgets(parent)
        if Widgets.get_table():
            parent.remove_widget(Widgets.get_table())
        for i in range(len(old_btns)):
            parent.remove_widget(old_btns[i])

        for i in range(len(new_btns)):
            parent.add_widget(new_btns[i])

    def display_method(self, parent, widgets, pos_y):
        self.slider_move(parent, pos_y)
        self.remove_active_widgets(parent)
        if Widgets.get_table():
            parent.remove_widget(Widgets.get_table())
        for i in range(len(widgets)):
            active_widgets_for_method.append(widgets[i])
            parent.add_widget(widgets[i])

    def build(self):
        parent = Widget()
        self.painter = MyWidget()
        parent.add_widget(self.painter)

        gradient_descent_widgets = Widgets.GradientDescentWidgets(parent)
        steepest_descent_widgets = Widgets.SteepestDescentWidgets(parent)
        gauss_zeidel_widgets = Widgets.GaussZeidelWidgets(parent)
        coordinate_descent_widgets = Widgets.CoordinateDescentWidgets(parent)
        main_menu_widgets = Widgets.MainMenuWidgets()
        test_widgets = Widgets.TestWidgets(parent)

        main_menu_widgets.labs_btn.bind(on_press=lambda x: self.display_button(parent,
                                                                               main_menu_widgets.get_main_menu_buttons(),
                                                                               main_menu_widgets.get_methods_buttons()
                                                                               ))
        main_menu_widgets.tests_btn.bind(on_press=lambda x: self.display_button(parent,
                                                                                main_menu_widgets.get_main_menu_buttons(),
                                                                                test_widgets.get_widgets() + test_widgets.active_question
                                                                                ))
        main_menu_widgets.theory_btn.bind(on_press=lambda x: self.display_button(parent,
                                                                                 main_menu_widgets.get_main_menu_buttons(),
                                                                                 main_menu_widgets.get_theory_btns()
                                                                                 ))
        main_menu_widgets.back_btn.bind(on_press=lambda x: self.display_button(parent,
                                                                               main_menu_widgets.get_methods_buttons(),
                                                                               main_menu_widgets.get_main_menu_buttons()
                                                                               ))
        main_menu_widgets.back_theory_btn.bind(on_press=lambda x: self.display_button(parent,
                                                                                      main_menu_widgets.get_theory_btns(),
                                                                                      main_menu_widgets.get_main_menu_buttons()
                                                                                      ))
        test_widgets.back_btn.bind(on_press=lambda X: self.display_button(parent,
                                                                          test_widgets.get_widgets(),
                                                                          main_menu_widgets.get_main_menu_buttons()
                                                                          ))
        main_menu_widgets.gradient_descent_btn.bind(on_press=lambda x: self.display_method(parent,
                                                                                           gradient_descent_widgets.get_widgets(),
                                                                                           main_menu_widgets.gradient_descent_btn.y
                                                                                           ))
        main_menu_widgets.steepest_descent_btn.bind(on_press=lambda x: self.display_method(parent,
                                                                                           steepest_descent_widgets.get_widgets(),
                                                                                           main_menu_widgets.steepest_descent_btn.y))
        main_menu_widgets.gauss_zeidel_btn.bind(on_press=lambda x: self.display_method(parent,
                                                                                       gauss_zeidel_widgets.get_widgets(),
                                                                                       main_menu_widgets.gauss_zeidel_btn.y))
        main_menu_widgets.coordinate_descent_btn.bind(on_press=lambda x: self.display_method(parent,
                                                                                             coordinate_descent_widgets.get_widgets(),
                                                                                             main_menu_widgets.coordinate_descent_btn.y))

        parent.add_widget(main_menu_widgets.head_label)
        parent.add_widget(main_menu_widgets.tests_btn)
        parent.add_widget(main_menu_widgets.theory_btn)
        parent.add_widget(main_menu_widgets.labs_btn)

        return parent

if __name__ == "__main__":
    KAIApp().run()
