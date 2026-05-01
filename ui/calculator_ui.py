import ast
import math
import operator
import tkinter as tk
from tkinter import messagebox, ttk


APP_BG = "#f4f7f9"
PANEL_BG = "#ffffff"
TEXT = "#17212b"
MUTED = "#5f6b76"
ACCENT = "#087f8c"
ACCENT_DARK = "#066b75"
ERROR = "#b42318"

LENGTH_UNITS = {
    "Kilometer": 1000,
    "Meter": 1,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Micrometer": 0.000001,
    "Nanometer": 0.000000001,
    "Mile": 1609.344,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Nautical mile": 1852,
}


class SafeExpressionEvaluator(ast.NodeVisitor):
    binary_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }
    unary_operators = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def visit_Expression(self, node):
        return self.visit(node.body)

    def visit_Constant(self, node):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers are allowed.")

    def visit_BinOp(self, node):
        operator_type = type(node.op)
        if operator_type not in self.binary_operators:
            raise ValueError("That operator is not supported.")

        left = self.visit(node.left)
        right = self.visit(node.right)

        if operator_type in (ast.Div, ast.Mod) and right == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        return self.binary_operators[operator_type](left, right)

    def visit_UnaryOp(self, node):
        operator_type = type(node.op)
        if operator_type not in self.unary_operators:
            raise ValueError("That operator is not supported.")

        return self.unary_operators[operator_type](self.visit(node.operand))

    def generic_visit(self, node):
        raise ValueError("Invalid calculator expression.")


def calculate_expression(expression):
    cleaned_expression = (
        expression.replace("x", "*")
        .replace("X", "*")
        .replace("^", "**")
        .replace(" ", "")
    )

    if not cleaned_expression:
        return ""

    tree = ast.parse(cleaned_expression, mode="eval")
    return SafeExpressionEvaluator().visit(tree)


def format_number(value):
    if value == "":
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return f"{value:.12g}"


def read_float(entry, field_name):
    value = entry.get().strip()
    if not value:
        raise ValueError(f"{field_name} is required.")
    return float(value)


def read_int(entry, field_name):
    value = entry.get().strip()
    if not value:
        raise ValueError(f"{field_name} is required.")
    return int(value)


class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Calculator")
        self.geometry("560x720")
        self.minsize(460, 620)
        self.configure(bg=APP_BG)

        self.expression = tk.StringVar()
        self.result = tk.StringVar(value="Ready")
        self.scientific_result = tk.StringVar(value="Result")
        self.interest_result = tk.StringVar(value="Result")
        self.length_result = tk.StringVar(value="Result")

        self.setup_styles()
        self.create_layout()
        self.bind_keyboard()

    def setup_styles(self):
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TNotebook", background=APP_BG, borderwidth=0)
        self.style.configure("TNotebook.Tab", padding=(14, 8), font=("Segoe UI", 10))
        self.style.configure("Panel.TFrame", background=PANEL_BG)
        self.style.configure("App.TFrame", background=APP_BG)
        self.style.configure("TLabel", background=PANEL_BG, foreground=TEXT, font=("Segoe UI", 10))
        self.style.configure("Muted.TLabel", background=PANEL_BG, foreground=MUTED, font=("Segoe UI", 9))
        self.style.configure("Result.TLabel", background=PANEL_BG, foreground=ACCENT, font=("Segoe UI", 12, "bold"))
        self.style.configure("Error.TLabel", background=PANEL_BG, foreground=ERROR, font=("Segoe UI", 12, "bold"))
        self.style.configure("TEntry", padding=8, font=("Segoe UI", 11))
        self.style.configure("TCombobox", padding=8, font=("Segoe UI", 10))
        self.style.configure("Accent.TButton", background=ACCENT, foreground="#ffffff", font=("Segoe UI", 10, "bold"))
        self.style.map(
            "Accent.TButton",
            background=[("active", ACCENT_DARK), ("pressed", ACCENT_DARK)],
            foreground=[("active", "#ffffff"), ("pressed", "#ffffff")],
        )

    def create_layout(self):
        container = ttk.Frame(self, style="App.TFrame", padding=16)
        container.pack(fill="both", expand=True)

        notebook = ttk.Notebook(container)
        notebook.pack(fill="both", expand=True)

        notebook.add(self.create_standard_tab(notebook), text="Calculator")
        notebook.add(self.create_scientific_tab(notebook), text="Scientific")
        notebook.add(self.create_interest_tab(notebook), text="Interest")
        notebook.add(self.create_length_tab(notebook), text="Length")

    def create_panel(self, parent):
        panel = ttk.Frame(parent, style="Panel.TFrame", padding=16)
        panel.pack(fill="both", expand=True)
        return panel

    def create_scrollable_area(self, parent):
        scroll_frame = ttk.Frame(parent, style="Panel.TFrame")
        scroll_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(scroll_frame, bg=PANEL_BG, borderwidth=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        content = ttk.Frame(canvas, style="Panel.TFrame")
        content_window = canvas.create_window((0, 0), window=content, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        def update_scroll_region(_event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def update_content_width(event):
            canvas.itemconfigure(content_window, width=event.width)

        def scroll_with_mouse(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        content.bind("<Configure>", update_scroll_region)
        canvas.bind("<Configure>", update_content_width)
        canvas.bind("<Enter>", lambda _event: canvas.bind_all("<MouseWheel>", scroll_with_mouse))
        canvas.bind("<Leave>", lambda _event: canvas.unbind_all("<MouseWheel>"))
        return content

    def create_standard_tab(self, notebook):
        tab = ttk.Frame(notebook, style="App.TFrame")
        panel = self.create_panel(tab)

        display = ttk.Entry(
            panel,
            textvariable=self.expression,
            justify="right",
            font=("Segoe UI", 24),
        )
        display.pack(fill="x", pady=(0, 8))
        self.bind_entry_action(display, self.evaluate_standard_expression)

        self.result_label = ttk.Label(panel, textvariable=self.result, style="Result.TLabel", anchor="e")
        self.result_label.pack(fill="x", pady=(0, 16))

        buttons = [
            ["C", "Back", "%", "/"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "^", "="],
        ]

        button_area = ttk.Frame(panel, style="Panel.TFrame")
        button_area.pack(fill="both", expand=True)

        for row_index, row in enumerate(buttons):
            button_area.rowconfigure(row_index, weight=1, uniform="button-row")
            for column_index, label in enumerate(row):
                button_area.columnconfigure(column_index, weight=1, uniform="button-column")
                button = tk.Button(
                    button_area,
                    text=label,
                    command=lambda value=label: self.handle_calculator_button(value),
                    bg=ACCENT if label == "=" else "#e8eef2",
                    fg="#ffffff" if label == "=" else TEXT,
                    activebackground=ACCENT_DARK if label == "=" else "#d8e1e7",
                    activeforeground="#ffffff" if label == "=" else TEXT,
                    borderwidth=0,
                    font=("Segoe UI", 14, "bold" if label == "=" else "normal"),
                    relief="flat",
                    cursor="hand2",
                )
                button.grid(row=row_index, column=column_index, sticky="nsew", padx=5, pady=5)

        return tab

    def create_scientific_tab(self, notebook):
        tab = ttk.Frame(notebook, style="App.TFrame")
        panel = ttk.Frame(tab, style="Panel.TFrame", padding=16)
        panel.pack(fill="both", expand=True)

        ttk.Label(panel, textvariable=self.scientific_result, style="Result.TLabel", wraplength=460).pack(
            fill="x",
            pady=(0, 12),
        )

        content = self.create_scrollable_area(panel)

        ttk.Label(content, text="Power and root", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        power_frame = ttk.Frame(content, style="Panel.TFrame")
        power_frame.pack(fill="x", pady=(8, 16))
        self.base_entry = self.create_labeled_entry(power_frame, "Number", 0, 0)
        self.exponent_entry = self.create_labeled_entry(power_frame, "Exponent or root", 0, 1)
        self.create_action_button(power_frame, "Power", self.calculate_power, 2, 0)
        self.create_action_button(power_frame, "Nth root", self.calculate_root, 2, 1)

        ttk.Separator(content).pack(fill="x", pady=8)

        ttk.Label(content, text="Factorial", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        factorial_frame = ttk.Frame(content, style="Panel.TFrame")
        factorial_frame.pack(fill="x", pady=(8, 16))
        self.factorial_entry = self.create_labeled_entry(factorial_frame, "Whole number", 0, 0)
        self.create_action_button(factorial_frame, "Factorial", self.calculate_factorial, 1, 1)

        ttk.Separator(content).pack(fill="x", pady=8)

        ttk.Label(content, text="Trigonometry", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        trig_frame = ttk.Frame(content, style="Panel.TFrame")
        trig_frame.pack(fill="x", pady=(8, 16))
        self.angle_entry = self.create_labeled_entry(trig_frame, "Angle in degrees", 0, 0)
        self.terms_entry = self.create_labeled_entry(trig_frame, "Taylor terms", 0, 1)
        self.terms_entry.insert(0, "10")
        self.create_action_button(trig_frame, "sin", lambda: self.calculate_trig("sin"), 2, 0)
        self.create_action_button(trig_frame, "cos", lambda: self.calculate_trig("cos"), 2, 1)
        self.create_action_button(trig_frame, "tan", lambda: self.calculate_trig("tan"), 2, 2)
        self.create_action_button(trig_frame, "sec", lambda: self.calculate_trig("sec"), 3, 0)
        self.create_action_button(trig_frame, "cosec", lambda: self.calculate_trig("cosec"), 3, 1)
        self.create_action_button(trig_frame, "cot", lambda: self.calculate_trig("cot"), 3, 2)

        ttk.Separator(content).pack(fill="x", pady=8)

        ttk.Label(content, text="Logarithms", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        log_frame = ttk.Frame(content, style="Panel.TFrame")
        log_frame.pack(fill="x", pady=(8, 16))
        self.log_number_entry = self.create_labeled_entry(log_frame, "Number", 0, 0)
        self.log_base_entry = self.create_labeled_entry(log_frame, "Base", 0, 1)
        self.log_base_entry.insert(0, "10")
        self.create_action_button(log_frame, "log", lambda: self.calculate_log("log"), 2, 0)
        self.create_action_button(log_frame, "ln", lambda: self.calculate_log("ln"), 2, 1)

        self.bind_entry_action(self.base_entry, self.calculate_power)
        self.bind_entry_action(self.exponent_entry, self.calculate_power)
        self.bind_entry_action(self.factorial_entry, self.calculate_factorial)
        self.bind_entry_action(self.angle_entry, lambda: self.calculate_trig("sin"))
        self.bind_entry_action(self.terms_entry, lambda: self.calculate_trig("sin"))
        self.bind_entry_action(self.log_number_entry, lambda: self.calculate_log("log"))
        self.bind_entry_action(self.log_base_entry, lambda: self.calculate_log("log"))
        return tab

    def create_interest_tab(self, notebook):
        tab = ttk.Frame(notebook, style="App.TFrame")
        panel = self.create_panel(tab)

        form = ttk.Frame(panel, style="Panel.TFrame")
        form.pack(fill="x")

        self.principal_entry = self.create_labeled_entry(form, "Principal", 0, 0)
        self.rate_entry = self.create_labeled_entry(form, "Rate %", 0, 1)
        self.time_entry = self.create_labeled_entry(form, "Time in years", 1, 0)
        self.frequency_entry = self.create_labeled_entry(form, "Times per year", 1, 1)
        self.frequency_entry.insert(0, "1")

        self.create_action_button(form, "Simple interest", self.calculate_simple_interest, 4, 0)
        self.create_action_button(form, "Compound interest", self.calculate_compound_interest, 4, 1)

        self.bind_entry_action(self.principal_entry, self.calculate_simple_interest)
        self.bind_entry_action(self.rate_entry, self.calculate_simple_interest)
        self.bind_entry_action(self.time_entry, self.calculate_simple_interest)
        self.bind_entry_action(self.frequency_entry, self.calculate_compound_interest)

        ttk.Label(panel, textvariable=self.interest_result, style="Result.TLabel", wraplength=430).pack(
            fill="x",
            pady=(18, 0),
        )
        return tab

    def create_length_tab(self, notebook):
        tab = ttk.Frame(notebook, style="App.TFrame")
        panel = self.create_panel(tab)

        form = ttk.Frame(panel, style="Panel.TFrame")
        form.pack(fill="x")
        form.columnconfigure(0, weight=1)
        form.columnconfigure(1, weight=1)

        self.length_value_entry = self.create_labeled_entry(form, "Value", 0, 0)

        ttk.Label(form, text="From").grid(row=2, column=0, sticky="w", padx=4, pady=(8, 2))
        self.from_unit = ttk.Combobox(form, values=list(LENGTH_UNITS.keys()), state="readonly")
        self.from_unit.grid(row=3, column=0, sticky="ew", padx=4, pady=(0, 8))
        self.from_unit.set("Meter")

        ttk.Label(form, text="To").grid(row=2, column=1, sticky="w", padx=4, pady=(8, 2))
        self.to_unit = ttk.Combobox(form, values=list(LENGTH_UNITS.keys()), state="readonly")
        self.to_unit.grid(row=3, column=1, sticky="ew", padx=4, pady=(0, 8))
        self.to_unit.set("Centimeter")

        self.create_action_button(form, "Convert", self.convert_length, 4, 0, columnspan=2)
        self.bind_entry_action(self.length_value_entry, self.convert_length)

        ttk.Label(panel, textvariable=self.length_result, style="Result.TLabel", wraplength=430).pack(
            fill="x",
            pady=(18, 0),
        )
        return tab

    def create_labeled_entry(self, parent, label, row, column):
        parent.columnconfigure(column, weight=1)
        ttk.Label(parent, text=label).grid(row=row * 2, column=column, sticky="w", padx=4, pady=(4, 2))
        entry = ttk.Entry(parent)
        entry.grid(row=row * 2 + 1, column=column, sticky="ew", padx=4, pady=(0, 8))
        return entry

    def create_action_button(self, parent, text, command, row, column, columnspan=1):
        parent.columnconfigure(column, weight=1)
        button = ttk.Button(parent, text=text, command=command, style="Accent.TButton")
        button.grid(row=row, column=column, columnspan=columnspan, sticky="ew", padx=4, pady=8)
        return button

    def bind_entry_action(self, entry, command):
        def run_command(_event):
            command()
            return "break"

        entry.bind("<Return>", run_command)

    def bind_keyboard(self):
        for key in "0123456789.+-*/^":
            self.bind(key, lambda event, value=key: self.handle_keyboard_input(value))
        self.bind("%", lambda _event: self.handle_keyboard_input("/100"))
        self.bind("<Return>", lambda _event: self.handle_keyboard_action(self.evaluate_standard_expression))
        self.bind("<BackSpace>", lambda _event: self.handle_keyboard_action(self.backspace_expression))
        self.bind("<Escape>", lambda _event: self.handle_keyboard_action(self.clear_expression))

    def entry_has_focus(self):
        return isinstance(self.focus_get(), (tk.Entry, ttk.Entry, ttk.Combobox))

    def handle_keyboard_input(self, value):
        if self.entry_has_focus():
            return
        self.append_to_expression(value)

    def handle_keyboard_action(self, action):
        if self.entry_has_focus():
            return
        action()

    def handle_calculator_button(self, value):
        if value == "C":
            self.clear_expression()
        elif value == "Back":
            self.backspace_expression()
        elif value == "=":
            self.evaluate_standard_expression()
        elif value == "%":
            self.append_to_expression("/100")
        else:
            self.append_to_expression(value)

    def append_to_expression(self, value):
        if self.result.get().startswith("Error"):
            self.result.set("Ready")
        self.expression.set(self.expression.get() + value)

    def backspace_expression(self):
        self.expression.set(self.expression.get()[:-1])
        if self.result.get().startswith("Error"):
            self.result.set("Ready")

    def clear_expression(self):
        self.expression.set("")
        self.result.set("Ready")
        self.result_label.configure(style="Result.TLabel")

    def evaluate_standard_expression(self):
        try:
            value = calculate_expression(self.expression.get())
            formatted_value = format_number(value)
            self.expression.set(formatted_value)
            self.result.set(formatted_value)
            self.result_label.configure(style="Result.TLabel")
        except Exception as error:
            self.result.set(f"Error: {error}")
            self.result_label.configure(style="Error.TLabel")

    def calculate_power(self):
        try:
            base = read_float(self.base_entry, "Number")
            exponent = read_float(self.exponent_entry, "Exponent")
            self.scientific_result.set(f"Result: {format_number(base ** exponent)}")
        except Exception as error:
            self.show_form_error(error)

    def calculate_root(self):
        try:
            number = read_float(self.base_entry, "Number")
            root = read_float(self.exponent_entry, "Root")
            if root == 0:
                raise ZeroDivisionError("Root cannot be zero.")
            self.scientific_result.set(f"Result: {format_number(number ** (1 / root))}")
        except Exception as error:
            self.show_form_error(error)

    def calculate_factorial(self):
        try:
            number = read_int(self.factorial_entry, "Whole number")
            if number < 0:
                raise ValueError("Factorial needs a positive whole number.")
            self.scientific_result.set(f"Result: {math.factorial(number)}")
        except Exception as error:
            self.show_form_error(error)

    def calculate_trig(self, operation):
        try:
            angle = read_float(self.angle_entry, "Angle")
            terms = read_int(self.terms_entry, "Taylor terms")
            if terms <= 0:
                raise ValueError("Taylor terms must be greater than zero.")

            radians = math.radians(angle)
            sin_value = self.taylor_sin(radians, terms)
            cos_value = self.taylor_cos(radians, terms)

            if operation == "sin":
                value = sin_value
            elif operation == "cos":
                value = cos_value
            elif operation == "tan":
                if round(cos_value, 12) == 0:
                    raise ZeroDivisionError("Tangent is undefined for this angle.")
                value = sin_value / cos_value
            elif operation == "sec":
                if round(cos_value, 12) == 0:
                    raise ZeroDivisionError("Secant is undefined for this angle.")
                value = 1 / cos_value
            elif operation == "cosec":
                if round(sin_value, 12) == 0:
                    raise ZeroDivisionError("Cosecant is undefined for this angle.")
                value = 1 / sin_value
            elif operation == "cot":
                if round(sin_value, 12) == 0:
                    raise ZeroDivisionError("Cotangent is undefined for this angle.")
                value = cos_value / sin_value
            else:
                raise ValueError("That trig operation is not supported.")

            self.scientific_result.set(f"{operation}({format_number(angle)} degrees) = {format_number(value)}")
        except Exception as error:
            self.show_form_error(error)

    def calculate_log(self, operation):
        try:
            number = read_float(self.log_number_entry, "Number")
            if number <= 0:
                raise ValueError("Number must be greater than zero.")

            if operation == "ln":
                value = math.log(number)
                self.scientific_result.set(f"ln({format_number(number)}) = {format_number(value)}")
                return

            base = read_float(self.log_base_entry, "Base")
            if base <= 0:
                raise ValueError("Base must be greater than zero.")
            if base == 1:
                raise ValueError("Base cannot be 1.")

            value = math.log(number, base)
            self.scientific_result.set(
                f"log base {format_number(base)} of {format_number(number)} = {format_number(value)}"
            )
        except Exception as error:
            self.show_form_error(error)

    @staticmethod
    def taylor_sin(x_value, terms):
        total = 0
        for n in range(terms):
            total += ((-1) ** n) * (x_value ** (2 * n + 1)) / math.factorial(2 * n + 1)
        return total

    @staticmethod
    def taylor_cos(x_value, terms):
        total = 0
        for n in range(terms):
            total += ((-1) ** n) * (x_value ** (2 * n)) / math.factorial(2 * n)
        return total

    def calculate_simple_interest(self):
        try:
            principal = read_float(self.principal_entry, "Principal")
            rate = read_float(self.rate_entry, "Rate")
            time = read_float(self.time_entry, "Time")
            interest = principal * rate * time / 100
            amount = principal + interest
            self.interest_result.set(
                f"Interest: {format_number(interest)}    Amount: {format_number(amount)}"
            )
        except Exception as error:
            self.show_form_error(error)

    def calculate_compound_interest(self):
        try:
            principal = read_float(self.principal_entry, "Principal")
            rate = read_float(self.rate_entry, "Rate")
            time = read_float(self.time_entry, "Time")
            frequency = read_float(self.frequency_entry, "Times per year")
            if frequency <= 0:
                raise ValueError("Times per year must be greater than zero.")

            amount = principal * (1 + rate / (100 * frequency)) ** (time * frequency)
            interest = amount - principal
            self.interest_result.set(
                f"Interest: {format_number(interest)}    Amount: {format_number(amount)}"
            )
        except Exception as error:
            self.show_form_error(error)

    def convert_length(self):
        try:
            value = read_float(self.length_value_entry, "Value")
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()
            meters = value * LENGTH_UNITS[from_unit]
            converted_value = meters / LENGTH_UNITS[to_unit]
            self.length_result.set(
                f"{format_number(value)} {from_unit} = {format_number(converted_value)} {to_unit}"
            )
        except Exception as error:
            self.show_form_error(error)

    def show_form_error(self, error):
        messagebox.showerror("Calculator error", str(error))


def main():
    app = CalculatorUI()
    app.mainloop()


if __name__ == "__main__":
    main()
