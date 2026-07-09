import ast
import os
import operator

from PyQt5 import QtWidgets, uic


class CalculatorWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "Calculator.ui")
        uic.loadUi(ui_path, self)

        self.expression = ""
        self.should_reset = False

        self.Text.setPlainText("0")
        self.Text.setReadOnly(True)
        self.Text.setUndoRedoEnabled(False)

        self._connect_buttons()

    def _connect_buttons(self):
        self.AC_start.clicked.connect(self.clear_display)
        self.pushButton.clicked.connect(self.calculate_result)
        self.percent_3.clicked.connect(lambda: self.append_operator("%"))
        self.Mult_on_4.clicked.connect(lambda: self.append_operator("*"))
        self.division_on_8.clicked.connect(lambda: self.append_operator("/"))
        self.sub_on_12.clicked.connect(lambda: self.append_operator("-"))
        self.add_on_16.clicked.connect(lambda: self.append_operator("+"))

        self.zero_2.clicked.connect(lambda: self.append_value("0"))
        self.one_13.clicked.connect(lambda: self.append_value("1"))
        self.two_14.clicked.connect(lambda: self.append_value("2"))
        self.three_15.clicked.connect(lambda: self.append_value("3"))
        self.four_9.clicked.connect(lambda: self.append_value("4"))
        self.five_10.clicked.connect(lambda: self.append_value("5"))
        self.six_11.clicked.connect(lambda: self.append_value("6"))
        self.seven_5.clicked.connect(lambda: self.append_value("7"))
        self.eight_6.clicked.connect(lambda: self.append_value("8"))
        self.nine_7.clicked.connect(lambda: self.append_value("9"))

    def append_value(self, value):
        if self.should_reset:
            self.expression = ""
            self.should_reset = False

        if self.expression in ("", "0"):
            self.expression = value
        else:
            self.expression += value

        self.Text.setPlainText(self.expression)

    def append_operator(self, operator_symbol):
        if operator_symbol == "%":
            if self.expression and self.expression[-1] != "%":
                self.expression += "%"
                self.Text.setPlainText(self.expression)
            return

        if self.should_reset:
            self.should_reset = False

        if not self.expression:
            if operator_symbol == "-":
                self.expression = "-"
            else:
                return
        else:
            if self.expression[-1] in "+-*/":
                self.expression = self.expression[:-1] + operator_symbol
            else:
                self.expression += operator_symbol

        self.Text.setPlainText(self.expression)

    def clear_display(self):
        self.expression = ""
        self.should_reset = False
        self.Text.setPlainText("0")

    def calculate_result(self):
        if not self.expression:
            return

        try:
            safe_expression = self.expression.replace("%", "/100")
            result = self._evaluate_expression(safe_expression)
            self.expression = str(result)
            self.Text.setPlainText(self.expression)
            self.should_reset = True
        except Exception:
            self.expression = ""
            self.Text.setPlainText("Error")
            self.should_reset = True

    def _evaluate_expression(self, expression):
        tree = ast.parse(expression, mode="eval")
        allowed_ops = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.USub: operator.neg,
            ast.UAdd: operator.pos,
        }

        def evaluate(node):
            if isinstance(node, ast.Expression):
                return evaluate(node.body)
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                return node.value
            if isinstance(node, ast.UnaryOp):
                return allowed_ops[type(node.op)](evaluate(node.operand))
            if isinstance(node, ast.BinOp):
                return allowed_ops[type(node.op)](evaluate(node.left), evaluate(node.right))
            raise ValueError("Unsupported expression")

        return evaluate(tree)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorWindow()
    window.setWindowTitle("Calculator")
    window.show()
    sys.exit(app.exec_())
