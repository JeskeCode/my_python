import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
  def __init__(self, parent=None):
      super(Form, self).__init__(parent)
      button=QPushButton("Change Color")
      self.label=QLabel(self)
      fill = QPixmap(20,20)
      fill.fill(Qt.red)
      self.label.setPixmap(fill)
      layout = QHBoxLayout()
      layout.addWidget(button)


      layout.addWidget(self.label)
      self.setLayout(layout)
      self.setWindowTitle("Color Changer")

      self.connect(button, SIGNAL("clicked()"), self.change)

  def change(self):
      fill = QPixmap(20,20)
      fill.fill(Qt.blue)
      self.label.setPixmap(fill)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()