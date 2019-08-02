"""
    读取excel
        1. pip3 install xlrd
        2. import xlrd
"""
import xlrd

def read_excel(excel_path, sheet_name):
    """
        读取excel的方法
        参数：excel_path: excel的目录在哪里
            sheet_name:这个表格的哪个也买你
    """
    results = []
    data = xlrd.open_workbook(excel_path)
    table = data.sheet_by_name(sheet_name)

    for row in range(1, table.nrows):
        results.append(table.row_values(row))

    return results


if __name__ == "__main__":
    data = read_excel("C:/Users/SNake/VSCodeProjects/ljtest201907/RequestsTest/testcases/接口测试用例模板.xlsx", "Sheet1")
    print(data)