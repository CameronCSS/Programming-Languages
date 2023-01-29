## A Simple Python code that Creates a UI and then calculates your Wages/Bills

####  How it works

```
-- The Remaining balance will be shown after you Enter wage, hours, Bills and Hit calculate --

-- This app uses the PyQt5 library to build a UI --

-- On the First tab you will enter your Wage and Hours worked --
-- You Then Hit 'Calculate' to calculate your check amount --

-- On the second tab you will hit "Add Bill" and enter a bill amount. --
-- The Remaining Balance will be updated live as you enter Bills --
```

![wage-calculator (3)](https://user-images.githubusercontent.com/121735588/211175350-f105e7f0-e049-4288-925c-4c9c8fa92d97.gif)



```python

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set the window title
		self.setWindowTitle('Income & Bills')
		
		# set the geometry of the window
		self.setGeometry(200, 200, 400, 400)
		
		# create the tabs
		self.tabs = QTabWidget()
		self.setCentralWidget(self.tabs)
		
		# create the income tab
		self.income_tab = QWidget()
		self.tabs.addTab(self.income_tab, 'Income')
		
		# create the bills tab
		self.bills_tab = QWidget()
		self.tabs.addTab(self.bills_tab, 'Bills')
		
		# create the income tab layout
		self.income_layout = QFormLayout()
		self.income_tab.setLayout(self.income_layout)
		
		# create the hourly wage label and input
		self.hourly_wage_label = QLabel('Hourly Wage')
		self.hourly_wage_input = QLineEdit()
		self.hourly_wage_input.setValidator(QDoubleValidator(0.00, 99.99, 2))
		self.income_layout.addRow(self.hourly_wage_label, self.hourly_wage_input)
		
		# create the hours worked label and input
		self.hours_worked_label = QLabel('Hours Worked')
		self.hours_worked_input = QLineEdit()
		self.hours_worked_input.setValidator(QDoubleValidator(0.00, 99.99, 2))
		self.income_layout.addRow(self.hours_worked_label, self.hours_worked_input)
		
		# create the calculate button
		self.calculate_button = QPushButton('Calculate')
		self.calculate_button.clicked.connect(self.calculate_income)
		self.income_layout.addRow(self.calculate_button)
		
		# create the bills tab layout
		self.bills_layout = QVBoxLayout()
		self.bills_tab.setLayout(self.bills_layout)
		
		# create the bills list
		self.bills_list = QListWidget()
		self.bills_layout.addWidget(self.bills_list)
		
		# create the add bill button
		self.add_bill_button = QPushButton('Add Bill')
		self.add_bill_button.clicked.connect(self.add_bill)
		self.bills_layout.addWidget(self.add_bill_button)
		
		# create the calculated income label
		self.calculated_income_label = QLabel('Calculated Income: 0.00')
		self.bills_layout.addWidget(self.calculated_income_label)
		
		# create the remaining balance label
		self.remaining_balance_label = QLabel('Remaining Balance: 0.00')
		self.bills_layout.addWidget(self.remaining_balance_label)
		
		# set the initial tab
		self.tabs.setCurrentIndex(0)
		
	def calculate_income(self):
		# calculate the income
		try:
			hourly_wage = float(self.hourly_wage_input.text())
			hours_worked = float(self.hours_worked_input.text())
			
			calculated_income = hourly_wage * hours_worked
			
			self.calculated_income_label.setText('Calculated Income: {:.2f}'.format(calculated_income))
			
			self.remaining_balance = calculated_income
			self.remaining_balance_label.setText('Remaining Balance: {:.2f}'.format(self.remaining_balance))
			
			self.tabs.setCurrentIndex(1)
		except:
			pass
			
	def add_bill(self):
		# add a bill
		bill_text, ok = QInputDialog.getText(self, 'Add Bill', 'Bill Amount:')
		
		if ok and bill_text != '':
			# add the bill to the list
			item = QListWidgetItem(bill_text)
			self.bills_list.addItem(item)
			
			# subtract the bill from the remaining balance
			bill_amount = float(bill_text)
			self.remaining_balance -= bill_amount
			
			# update the remaining balance label
			self.remaining_balance_label.setText('Remaining Balance: {:.2f}'.format(self.remaining_balance))
			
# run the app
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())

```

### <a href="https://github.com/CameronCSS/PersonalProjects/blob/main/README.md">BACK TO PORTFOLIO</a>

## Contact Me

| Contact Method | Link |
| --- | --- |
| Email | CameronSeamons@gmail.com |
| LinkedIn | https://www.linkedin.com/in/cameron-css/|
| Twitter | https://twitter.com/Cameron_CSS |
| Resume | ['Cameron Seamons' Resume](https://drive.google.com/file/d/19vkbf2HjEpXpxndWYa4A6Dyt6gsnGv73/view?usp=sharing) | 
