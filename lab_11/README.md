# Лабораторная работа №11
## Вариант 4
## Задания
1. Реализуйте приложение с GUI (приложения-игры допускается делать с использованием TUI-пакетов) по своему варианту. Можно изменить задание на собственную тему, согласовав с преподавателем. Список GUI фреймворков:
- appJar
- Tkinter
- Flet
- wxPython
- PySimpleGUI
- Pyforms
- Toga
- PyGObject
- guizero
- guietta
- PySide6
- Dear PyGui
- PyGame
Оформите README.md. Он должен содержать:
- Название вашего приложения
- Описание
- Инструкции по запуску
- Краткую справку

**Описание:**

Приложение "Интерактивный Календарь" представляет собой графический календарь, позволяющий пользователю просматривать дни месяца и года, а также добавлять и просматривать заметки для конкретных дат. Приложение отображает календарь в текущем месяце и году, но есть возможность переключаться между месяцами.

**Инструкции по запуску:**

1. **Предварительные условия:**
    - Python 3.13.1 установлен.
    - Установлена библиотека `PySimpleGUI`. Установите ее с помощью команды: `pip install PySimpleGUI`

2. **Запуск приложения:**
   Сохраните код в файл `calendar_app.py` и выполните в терминале: `python calendar_app.py`

**Краткая справка:**

- **Отображение календаря:** Календарь отображает текущий месяц и год.
- **Переключение месяцев:** Используйте кнопки "<" и ">" для перехода к предыдущему или следующему месяцу.
- **Выбор даты:** Выберите дату, нажав на ее в календаре.
- **Добавление заметок:** Введите текст заметки в поле ввода и нажмите "Добавить заметку", чтобы сохранить заметку для выбранной даты.
- **Просмотр заметок:** Заметка для выбранной даты будет отображаться ниже поля добавления заметки.

**Автор:** [Иванов Григорий]

# Проделанная работа и скриншоты результатов
## Программа
``` py
import PySimpleGUI as sg
import calendar
from datetime import date
import json

def get_calendar_layout(year, month):
    cal = calendar.monthcalendar(year, month)
    header = [sg.Text(day, size=(3, 1), justification='center') for day in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']]
    rows = []
    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append(sg.Text("  ", size=(3, 1)))
            else:
                row.append(sg.Button(str(day), key=str(day), size=(3, 1)))
        rows.append(row)

    return [header] + rows

def load_notes():
    try:
        with open('notes.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_notes(notes):
    with open('notes.json', 'w') as f:
        json.dump(notes, f)

def update_notes_display(window, selected_date, notes):
    if selected_date in notes:
        window['-NOTE_DISPLAY-'].update(notes[selected_date])
    else:
        window['-NOTE_DISPLAY-'].update("")

# --- Начало программы ---

sg.theme('LightGreen')

today = date.today()
year, month = today.year, today.month
selected_date = today.strftime("%Y-%m-%d")
notes = load_notes()

layout = [
    [sg.Text(f'{calendar.month_name[month]} {year}', key='-MONTH_YEAR-', font=('Arial Bold', 14), expand_x=True, justification='center')],
    [sg.Button('<', key='-PREV_MONTH-'), sg.Button('>', key='-NEXT_MONTH-')],
    *get_calendar_layout(year, month),
    [sg.Text("Заметки для: ", key='-DATE_TEXT-',font=('Arial', 10)), sg.Text(selected_date,key='-SELECTED_DATE-')],
    [sg.Input(key='-NOTE_INPUT-', size=(40, 1)), sg.Button('Добавить заметку')],
    [sg.Multiline(key='-NOTE_DISPLAY-', size=(40, 5), disabled=True)],
]

window = sg.Window('Интерактивный Календарь', layout)
update_notes_display(window, selected_date, notes)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-PREV_MONTH-':
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        window['-MONTH_YEAR-'].update(f'{calendar.month_name[month]} {year}')
        for row in window.layout[2:len(window.layout)-3]:
            for el in row:
                el.update(visible=False)
        new_layout = get_calendar_layout(year, month)
        for row_index, row in enumerate(new_layout):
          for el_index,el in enumerate(row):
            window.layout[2+row_index][el_index] = el
            window.layout[2+row_index][el_index].update(visible=True)


    elif event == '-NEXT_MONTH-':
        month += 1
        if month == 13:
          month = 1
          year += 1
        window['-MONTH_YEAR-'].update(f'{calendar.month_name[month]} {year}')
        for row in window.layout[2:len(window.layout)-3]:
            for el in row:
                el.update(visible=False)
        new_layout = get_calendar_layout(year, month)
        for row_index, row in enumerate(new_layout):
          for el_index,el in enumerate(row):
            window.layout[2+row_index][el_index] = el
            window.layout[2+row_index][el_index].update(visible=True)
    
    elif event.isdigit():
        selected_date = date(year, month, int(event)).strftime("%Y-%m-%d")
        window['-SELECTED_DATE-'].update(selected_date)
        update_notes_display(window, selected_date, notes)

    elif event == 'Добавить заметку':
        note = values['-NOTE_INPUT-']
        if note:
            notes[selected_date] = note
            save_notes(notes)
            update_notes_display(window, selected_date, notes)
        window['-NOTE_INPUT-'].update('')

window.close()
```



