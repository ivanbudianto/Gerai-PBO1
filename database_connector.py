import mysql.connector

class Database_Connect:
    def __init__(self):

        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        )
    
    def create_database(self):
        cursor = self.db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS db_shop;"
        cursor.execute(sql)
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db_shop"
        )

    def create_table(self):
        cursor = self.db.cursor()
        sql = """CREATE TABLE IF NOT EXISTS tb_warehouse (
                WarehouseID BIGINT AUTO_INCREMENT PRIMARY KEY,
                WarehouseAddress VARCHAR(255)
                );"""
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS tb_items (
                ItemID BIGINT AUTO_INCREMENT PRIMARY KEY,
                ProductName VARCHAR(255),
                CategoryName VARCHAR(255),
                UnitSellPrice double,
                UnitBuyPrice double,
                StockAvailable DOUBLE,
                StockSold DOUBLE,
                WarehouseID BIGINT,
                FOREIGN KEY (WarehouseID) REFERENCES tb_warehouse(WarehouseID)
                );"""
        cursor.execute(sql)

    def record_warehouse_value(self, a):
        cursor = self.db.cursor()
        sql = "INSERT INTO tb_warehouse (WarehouseAddress) VALUE (%s)"
        val = (a,)
        cursor.execute(sql,val)
        self.db.commit()

    def record_item_value(self, list_input):
        cursor = self.db.cursor()
        sql = "INSERT INTO tb_items (ProductName,CategoryName,UnitSellPrice,UnitBuyPrice,StockAvailable,StockSold,WarehouseID) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = list_input
        cursor.execute(sql, val)
        self.db.commit()

    def get_record_item(self):

        cursor = self.db.cursor()
        sql = """SELECT *
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = N'tb_items'"""
        cursor.execute(sql)
        headers = cursor.fetchall()
        headers_fix = []
        for i in headers:
            headers_fix.append(i[3])

        cursor = self.db.cursor()
        sql = "SELECT * FROM tb_items"
        cursor.execute(sql)
        results = cursor.fetchall()

        print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*headers_fix))
        if cursor.rowcount < 0:
            print("No data")
        else:
            for data in results:
                print("{: <10} {: <30} {: <15} {: <15} {: <15} {: <15} {: <15} {: <15}".format(*data))

        return headers_fix, results

    def get_record_warehouse(self):

        cursor = self.db.cursor()
        sql = """SELECT *
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = N'tb_warehouse'"""
        cursor.execute(sql)
        headers = cursor.fetchall()
        headers_fix = []
        for i in headers:
            headers_fix.append(i[3])

        cursor = self.db.cursor()
        sql = "SELECT * FROM tb_warehouse"
        cursor.execute(sql)
        results = cursor.fetchall()

        print("{: <15} {: <100}".format(*headers_fix))
        if cursor.rowcount < 0:
            print("No data")
        else:
            for data in results:
                print("{: <15} {: <100}".format(*data))


