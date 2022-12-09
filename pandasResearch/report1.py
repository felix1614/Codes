import random
import pandas as pd
import xlsxwriter as xl


def dataFrame():
    data = dict()
    sens = ["Gen set", "Fan", "Air Conditioner"]
    sensor_162 = pd.read_csv("Electric_Production.csv")
    tempSen = sensor_162["IPG"].copy()
    random.shuffle(tempSen)
    sensor_162["LPG"] = tempSen
    c = 156
    tag = 2
    sampleData = dict()
    for i in sensor_162:
        if str(sensor_162[i].dtypes) == "float64":
            sensor_162[i].fillna(0, inplace=True)
            sensor_162.rename(columns={i: f'tag_{c}'}, inplace=True)
            sampleData[f'tag_{c}'] = sum(sensor_162[f'tag_{c}'])
            c += 8
        else:
            sampleData[i] = 'TOTAL'
    sensor_162 = sensor_162.append(sampleData, ignore_index=True)
    sensor_165 = sensor_162.copy().drop(['DATE'], axis=1)
    sensor_169 = sensor_165.copy()
    dfs = [sensor_162, sensor_165, sensor_169]
    for i in sens:
        if len(data) < 1:
            data["sensors"] = dict()
            data["sensors"][i] = dfs[sens.index(i)]
        else:
            data["sensors"][i] = dfs[sens.index(i)]
    data['tags'] = tag

    # mainFrame = pd.concat([sensor_162, sensor_165], axis=1)
    # val = {"DATE": "TOTAL"}
    # mainFrame = mainFrame.append(val, ignore_index=True)
    return data


def reportGen():
    df = dataFrame()
    workbook = xl.Workbook('../dash/merge1.xlsx')
    worksheet = workbook.add_worksheet(name="test")
    # worksheet.set_column("A:G", 10)
    form = {
        'valign': 'vcenter',
        'fg_color': 'white',
        'border': 2}
    merge_format = workbook.add_format(form)

    def header(colLength):
        worksheet.merge_range('A1:D4', data="", cell_format=merge_format)
        option = {'x_offset': 10, 'y_offset': 5, 'x_scale': 0.5, 'y_scale': 0.7}
        worksheet.insert_image('A1:D1', "logo.png", options=option)
        form_1 = form.copy()
        form_1.update({'bold': True, 'align': 'center', 'bg_color': '#DCDCDC', 'font_size': 10})
        form_1.pop('fg_color')
        form_1['bg_color'] = '#F0F0F0'
        worksheet.merge_range(f'E1:{chr(colLength)}4', data="Home EB Usage Report", cell_format=workbook.add_format(form_1))
        form_1['align'] = 'left'
        form_1['bg_color'] = '#DCDCDC'
        worksheet.merge_range('A5:B5', data="Industry Name", cell_format=workbook.add_format(form_1))
        form_1['bg_color'] = '#F0F0F0'
        worksheet.merge_range('C5:D5', data="Elm", cell_format=workbook.add_format(form_1))
        form_1['bg_color'] = '#DCDCDC'
        worksheet.write("E5", "From Date", workbook.add_format(form_1))
        form_1['bg_color'] = '#F0F0F0'
        worksheet.merge_range(f'F5:{chr(colLength)}5', data=f"{'2022-11-30'}", cell_format=workbook.add_format(form_1))
        form_1['bg_color'] = '#DCDCDC'
        worksheet.merge_range('A6:B6', data="Location", cell_format=workbook.add_format(form_1))
        form_1['bg_color'] = '#F0F0F0'
        worksheet.merge_range('C6:D6', data=f"{'Bangalore'}", cell_format=workbook.add_format(form_1))
        form_1['bg_color'] = '#DCDCDC'
        worksheet.write("E6", "To Date", workbook.add_format(form_1))
        form_1['bg_color'] = '#F0F0F0'
        worksheet.merge_range(f'F6:{chr(colLength)}6', data=f"{'2022-12-02'}", cell_format=workbook.add_format(form_1))
        form_1['bg_color'] = '#DCDCDC'
        worksheet.merge_range('A7:B7', data="Assets Name", cell_format=workbook.add_format(form_1))
        form_1['bg_color'] = '#F0F0F0'
        worksheet.merge_range(f'C7:{chr(colLength)}7', data=f"{', '.join([sen for sen in df['sensors']])}", cell_format=workbook.add_format(form_1))
        form_1.pop('bg_color')
        worksheet.merge_range(f'A8:{chr(colLength)}8', data="", cell_format=workbook.add_format(form_1))
        worksheet.merge_range('A9:B9', data="", cell_format=workbook.add_format(form_1))
        worksheet.merge_range(f'{chr(colLength-1)}9:{chr(colLength)}9', data="", cell_format=workbook.add_format(form_1))
    chr_ = 67
    form_temp = form.copy()
    form_temp.pop('fg_color')
    form_temp.update({'bold': True, 'align': 'center', 'bg_color': '#DCDCDC', 'font_size': 10})

    for i in df["sensors"]:
        form_temp['bg_color'] = '#F0F0F0'
        worksheet.merge_range(f"{chr(chr_)}9:{chr(chr_+df['tags']-1)}9", data=f"{i}", cell_format=workbook.add_format(form_temp))
        chr_ += df['tags']
    form_temp['bg_color'] = '#DCDCDC'

    header(colLength=chr_+1)
    row, col, n = 9, 2, 1
    worksheet.merge_range(f"{chr(chr_)}10:{chr(chr_ + 1)}10", data="Remarks",
                          cell_format=workbook.add_format(form_temp))

    for i in df["sensors"]:
        for j in df["sensors"][i]:
            if j == 'DATE':
                worksheet.write(row, 0, "SI.No", workbook.add_format(form_temp))
                worksheet.write(row, 1, j, workbook.add_format(form_temp))
                row_1 = 10
                for date in df["sensors"][i][j]:
                    form_temp['bg_color'] = '#F0F0F0'
                    worksheet.write(row_1, 1, date, workbook.add_format(form_temp))
                    if len(df["sensors"][i][j])-1 > df["sensors"][i][j][df["sensors"][i][j] == date].index[0]:
                        worksheet.write(row_1, 0, n, workbook.add_format(form_temp))
                    else:
                        worksheet.write(row_1, 0, "", workbook.add_format(form_temp))
                    n += 1
                    row_1 += 1
            else:
                form_temp['bg_color'] = '#DCDCDC'
                worksheet.write(row, col, j, workbook.add_format(form_temp))
                row_1 = 10
                for date in df["sensors"][i][j]:
                    form_temp['bg_color'] = '#F0F0F0'
                    worksheet.write(row_1, col, date, workbook.add_format(form_temp))
                    worksheet.merge_range(f"{chr(chr_)}{row_1+1}:{chr(chr_ + 1)}{row_1+1}", data="",
                                          cell_format=workbook.add_format(form_temp))
                    n += 1
                    row_1 += 1
                col += 1

    workbook.close()


reportGen()
