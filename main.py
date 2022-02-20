import pandas as pd
from pylab import *
import matplotlib.pyplot as plt

# pip3 install pandas
# pip3 install xlrd
# pip3 install openpyxl
# pip3 install matplotlib


# Đọc file excel
xl = pd.ExcelFile('test.xlsx')
df = pd.read_excel(xl, 0, header=None)
xList = df[0].tolist()  # list từ column 1
yList = df[1].tolist()  # list từ column 2
print(xList, yList)

# Đồ thị điểm với Matplotlib

plt.plot(xList, yList)
plt.show()
