# PythonScripts
gui_helpers.py
import tkinter as tk
from tkinter import ttk


def setup_styles():
    # Create custom styles
    custom_styles = {
        "SystemButton.TButton": {"background": "#4d4d4d", "foreground": "white", "activebackground": "#808080", "activeforeground": "white", "highlightthickness": 0},
        "SubmitButton.TButton": {"background": "#4d4d4d", "foreground": "white", "activebackground": "#808080", "activeforeground": "white", "highlightthickness": 0},
        "QuitButton.TButton": {"background": "#4d4d4d", "foreground": "white", "activebackground": "#808080", "activeforeground": "white", "highlightthickness": 0},
        "OptionLabel.TLabel": {"background": "#d9d9d9", "foreground": "#4d4d4d"},
        "Option.TEntry": {"background": "white", "foreground": "#4d4d4d"},
        "Option.TRadiobutton": {"background": "#d9d9d9", "foreground": "#4d4d4d", "highlightthickness": 0},
    }
    style = ttk.Style()
    for style_name, options in custom_styles.items():
        style.configure(style_name, **options)


def create_system_button(master, system_name, options):
    # Create button
    button = ttk.Button(master, text=system_name, command=lambda: displaySystemOptions(master, system_name, options), style="SystemButton.TButton")
    button.pack(fill="x", padx=10, pady=10)


def setup_system_options_styles(system_options_window):
    system_options_window.option_add("*Button.Background", "#4d4d4d")
    system_options_window.option_add("*Button.Foreground", "white")
    system_options_window.option_add("*Button.activeBackground", "#808080")
    system_options_window.option_add("*Button.activeForeground", "white")
    system_options_window.option_add("*Button.highlightThickness", 0)
    system_options_window.option_add("*Label.Background", "#d9d9d9")
    system_options_window.option_add("*Label.Foreground", "#4d4d4d")


def setup_system_setup_options_styles(system_setup_options_window):
    system_setup_options_window.option_add("*Button.Background", "#4d4d4d")
    system_setup_options_window.option_add("*Button.Foreground", "white")
    system_setup_options_window.option_add("*Button.activeBackground", "#808080")
    system_setup_options_window.option_add("*Button.activeForeground", "white")
    system_setup_options_window.option_add("*Button.highlightThickness", 0)
    system_setup_options_window.option_add("*Label.Background", "#d9d9d9")
    system_setup_options_window.option_add("*Label.Foreground", "#4d4d4d")


def create_label_and_options(master, label_text, option_values):
    label = ttk.Label(master, text=label_text, style="OptionLabel.TLabel")
    label.pack(pady=5)
    var = tk.StringVar(value=option_values[0])
    for option_value in option_values:
        radio = ttk.Radiobutton(master, text=option_value, variable=var, value=option_value, style="Option.TRadiobutton")
        radio.pack()
    return var


def create_label_and_entry(master, label_text):
    label = ttk.Label(master, text=label_text, style="OptionLabel.TLabel")
    label.pack(pady=5)
    entry = ttk.Entry(master, style="Option.TEntry")
    entry.pack()
   
