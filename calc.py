from PyQt5 import QtWidgets, uic
import sys


class Calculator(QtWidgets.QWidget):
    """This class provides a simple GUI calculator"""
    def __init__(self):
        super().__init__()

        # Import and compile GUI, connect button actions to its specific slot.
        self.ui = uic.loadUi("calculator.ui", self)
        self.max_len = 12
        self.temp_number = ''      
        self.number_1 = ''
        self.number_2 = ''
        self.operator = ''
        self.result = ""
        self.display.setText("0")

        self.ui.bt_clr.clicked.connect(self.button_clr)
        self.ui.bt_0.clicked.connect(self.button_0)
        self.ui.bt_1.clicked.connect(self.button_1)
        self.ui.bt_2.clicked.connect(self.button_2)
        self.ui.bt_3.clicked.connect(self.button_3)
        self.ui.bt_4.clicked.connect(self.button_4)
        self.ui.bt_5.clicked.connect(self.button_5)
        self.ui.bt_6.clicked.connect(self.button_6)
        self.ui.bt_7.clicked.connect(self.button_7)
        self.ui.bt_8.clicked.connect(self.button_8)
        self.ui.bt_9.clicked.connect(self.button_9)
        self.ui.bt_point.clicked.connect(self.button_point)
        self.ui.bt_add.clicked.connect(self.button_add)
        self.ui.bt_sub.clicked.connect(self.button_sub)
        self.ui.bt_mult.clicked.connect(self.button_mult)
        self.ui.bt_div.clicked.connect(self.button_div)
        self.ui.bt_enter.clicked.connect(self.button_enter)
 
    def button_0(self):
        self.build_number("0")
    
    def button_1(self):
        self.build_number("1")

    def button_2(self):
        self.build_number("2")

    def button_3(self):
        self.build_number("3")

    def button_4(self):
        self.build_number("4")
        
    def button_5(self):
        self.build_number("5")
          
    def button_6(self):
        self.build_number("6")

    def button_7(self):
        self.build_number("7")   

    def button_8(self):
        self.build_number("8")

    def button_9(self):
        self.build_number("9")

    def button_point(self):
        # Set a dot to get a decimal number.
        if not "." in self.temp_number:

            if self.temp_number:
                self.build_number(".")
            elif not self.temp_number: 
                self.build_number("0.")

    def display_error(self):
        # Displays Error if range of display is insufficient and reset.
        self.display.setText("Error!")
        self.delete()
        
    def button_clr(self):
        # Reset and display zero
        self.display.setText("0")
        self.delete()
    
    def delete(self):
        self.temp_number = ''
        self.number_1 = ''
        self.number_2 = ''
        self.operator = ''
        self.result = ""

    def build_number(self, char):
        # Build and display a number, taking characters via buttons.
        if len(self.temp_number) < self.max_len - 2:

            if self.result:
                self.delete()
            self.temp_number += char
            self.display.setText(self.temp_number)

    # Set the first number and the operator.
    def button_add(self):
        self.set_operator("+")

    def button_sub(self):
        self.set_operator("-")
    
    def button_mult(self):
        self.set_operator("*")
    
    def button_div(self):
        self.set_operator("/")
  
    def set_operator(self, operator):

        if not self.temp_number:
            self.temp_number = "0"

        if self.temp_number and not self.number_1 and not self.number_2:
            self.number_1 = self.temp_number
            self.operator = operator        
            self.display.setText(self.operator)
            self.temp_number = ""

        if self.result:
            self.number_1 = self.result
            self.operator = operator      
            self.display.setText(self.operator)
            self.temp_number = ""
            self.number_2 = ""
            self.result = ""

    def button_enter(self):
        # Set the second number, calculate and display result.
        if self.temp_number and self.number_1 and not self.number_2:
            self.number_2 = self.temp_number
            self.temp_number = ""
        
        if self.number_1 and self.number_2 and not self.result:

            if self.operator == "+":
                self.number_1 = float(self.number_1)
                self.number_2 = float(self.number_2)
                self.result = self.number_1 + self.number_2    
                self.result = round(self.result, 4)          
                self.result = str(self.result)         

                if len(self.result) < self.max_len:                   
                    self.display.setText(self.result)
                    self.temp_number = ""
                else:
                    self.display_error()
            
            if self.operator == "-":
                self.number_1 = float(self.number_1)
                self.number_2 = float(self.number_2)
                self.result = self.number_1 - self.number_2  
                self.result = round(self.result, 4)          
                self.result = str(self.result)

                if len(self.result) < self.max_len:                   
                    self.display.setText(self.result)
                    self.temp_number = ""
                else:
                    self.display_error()

            if self.operator == "*":
                self.number_1 = float(self.number_1)
                self.number_2 = float(self.number_2)
                self.result = self.number_1 * self.number_2   
                self.result = round(self.result, 4)          
                self.result = str(self.result)

                if len(self.result) < self.max_len:                   
                    self.display.setText(self.result)
                    self.temp_number = ""
                else:
                    self.display_error()

            if self.operator == "/":
                self.number_1 = float(self.number_1)
                self.number_2 = float(self.number_2)
                try:                   
                    self.result = self.number_1 / self.number_2                      
                except ZeroDivisionError:
                    self.display.setText("Don't!")
                else:
                    self.result = round(self.result, 4)  
                    self.result = str(self.result)

                    if self.result == "0.0":
                        self.display_error()
                        return
                    
                    if len(self.result) < self.max_len:                   
                        self.display.setText(self.result)
                        self.temp_number = ""
                    else:
                        self.display_error()

            self.number_1 = ''
            self.number_2 = ''
            self.operator = ''
            self.temp_number = '' 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_ui = Calculator()
    main_ui.show()
    sys.exit(app.exec_())


