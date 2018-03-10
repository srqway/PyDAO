import sqlite3


class NasdaqDAO:

    def __init__(self):
        self.db = './StockInfo.sqlt3'
        self.conn = None
        self.curs = None
        self.bOpen = False
        self.fields = [('Symbol', 'TEXT'), ('SecurityName', 'TEXT'), ('MarketCategory', 'TEXT'), ('TestIssue', 'TEXT'), ('FinancialStatus', 'TEXT'), ('RoundLotSize', 'INTEGER'), ('ETF', 'TEXT'), ('NextShares', 'TEXT')]
        self.table_name = 'TOK_NASDAQ'
        
    def open(self):
        if self.bOpen is False:
            self.conn = sqlite3.connect(self.db)
            self.curs = self.conn.cursor()
            self.bOpen = True
        return True
        
    def close(self):
        if self.bOpen:
            self.conn.commit()
            self.bOpen = False
        return True
        
    def count(self):
        if self.bOpen:
            res = self.curs.execute("SELECT count(*) FROM TOK_NASDAQ;")
            return res.fetchone()[0]
        return -1
        
    def drop_table(self):
        if self.bOpen:
            self.curs.execute("DrOp TaBLe IF EXISTS TOK_NASDAQ;")
            return True
        return False
        
    def create_table(self):
        if self.bOpen:
            self.curs.execute("CREATE TABLE IF NOT EXISTS TOK_NASDAQ(ID INTEGER PRIMARY KEY AUTOINCREMENT, Symbol TEXT, SecurityName TEXT, MarketCategory TEXT, TestIssue TEXT, FinancialStatus TEXT, RoundLotSize INTEGER, ETF TEXT, NextShares TEXT);")
            return True
        return False
        
    def insert(self, fields):
        if self.bOpen:
            self.curs.execute("INSERT INTO TOK_NASDAQ ( Symbol, SecurityName, MarketCategory, TestIssue, FinancialStatus, RoundLotSize, ETF, NextShares) VALUES (?,?,?,?,?,?,?,?);", fields)
            return True
        return False
        
    def delete(self, primary_key):
        if self.bOpen:
            self.curs.execute("DELETE from TOK_NASDAQ WHERE ID = ?;", [primary_key])
            return True
        return False
        
    def select(self, sql_select):
        if self.bOpen:
            self.curs.execute(sql_select)
            zlist = self.curs.fetchall()
            for ref in zlist:
                yield ref
        return None
        
    @staticmethod
    def Import(dao, data_file='../DaoTest01/nasdaqlisted.txt', hasHeader=True, sep='|'):
        try:
            # dao.open()
            with open(data_file) as fh:
                line = fh.readline().strip()
                if hasHeader is True:
                    line = fh.readline().strip()
                while len(line) is not 0:
                    dao.insert(line.split(sep))
                    line = fh.readline().strip()
            # dao.close()
            return True
        except:
            pass
        return False
        
    