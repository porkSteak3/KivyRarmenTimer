from kivy.app import App
from kivy.lang import Builder

Builder.load_file('test.kv')


class TestApp(App):
    pass


if __name__ == '__main__':
    TestApp().run()
