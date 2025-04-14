import gspread

# サービスアカウントの認証
gc = gspread.service_account(filename="")

# ユーザーからファイル名の入力を受け取る
daily_report_filename = input("日報のファイル名（例: 2025.3 日報renew）を入力してください:　")
copy_file_filename = input("収支のファイル名（例: コピー収支2025.3）を入力してください: ")

# 指定されたファイル名でスプレッドシートを開く（フォルダIDはそのまま利用）
sh = gc.open(daily_report_filename, folder_id="")
# 「出金管理表」シートからデータを抽出
ws_outmoney = sh.worksheet("出金管理表")
val_food = ws_outmoney.acell("B34").value 
val_drink = ws_outmoney.acell("C34").value
val_consumables = ws_outmoney.acell("D34").value
val_water = ws_outmoney.acell("E34").value
val_ele = ws_outmoney.acell("F34").value
val_gas = ws_outmoney.acell("G34").value
val_phone = ws_outmoney.acell("H34").value
val_internet = ws_outmoney.acell("I34").value
val_wifi = ws_outmoney.acell("J34").value
val_ad = ws_outmoney.acell("K34").value
val_commission = ws_outmoney.acell("L34").value
val_salary = ws_outmoney.acell("M34").value
val_trans = ws_outmoney.acell("N34").value
val_employee_benefits = ws_outmoney.acell("O34").value
val_consumables_commission = int(val_consumables) + int(val_commission)

# 「集客状況」シートからデータを抽出
ws_customer = sh.worksheet("集客状況")
val_sumcustomer = ws_customer.acell("G51").value
val_sales = ws_customer.acell("G41").value
print("「F材料費:" + val_food + "」","「D材料費:" + val_drink + "」", "「消耗品費:" + val_consumables + "」", "「水道代:" + val_water + "」", "「電気代:" + val_ele + "」", "「ガス代:" + val_gas + "」",
    "「通信費（電話）:" + val_phone + "」", "「通信費（ネット）:" + val_internet + "」", "「通信費（Wi-fi）:" + val_wifi + "」", "「広告費:" + val_ad + "」", "「給料:" + val_salary + "」", "「交通費:" + val_trans + "」", "「福利厚生費:" + val_employee_benefits + "」", "「支払い手数料:" + val_commission + "」","「消耗品費+支払手数料（雑費）:" + str(val_consumables_commission) + "」" ,"「総売上:" + val_sales + "」", "「客数:" + val_sumcustomer + "」")
    
# コピー収支のスプレッドシートをユーザー指定のファイル名で開く
sh1 = gc.open(copy_file_filename, folder_id="")
ws = sh1.worksheet("PL財務諸表用")

# コピー収支2025.3 の "PL財務諸表用" にデータを書き込む
ws.update_cell(3, 3, val_sales)
ws.update_cell(4, 3, val_food)
ws.update_cell(5, 3, val_drink)
ws.update_cell(7, 3, val_salary)
ws.update_cell(8, 3, val_trans)
ws.update_cell(9, 3, val_employee_benefits)
ws.update_cell(12, 3, val_water)
ws.update_cell(13, 3, val_ele)
ws.update_cell(14, 3, val_gas)
ws.update_cell(17, 3, val_phone)
ws.update_cell(18, 3, val_internet)
ws.update_cell(19, 3, val_wifi)
ws.update_cell(20, 3, val_ad)
ws.update_cell(21, 3, val_consumables_commission)
ws.update_cell(3, 7, val_sales)
ws.update_cell(4, 7, val_sumcustomer)
