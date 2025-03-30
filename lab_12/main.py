# main.py

from package.gui import MaterialApp
from guizero import App

def main():
    app = App()
    MaterialApp(app)
    app.display()

if __name__ == "__main__":
    main()