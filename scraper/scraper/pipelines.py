import sqlite3, json

class ScraperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('scrape_data.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS scrape_tb""")
        self.curr.execute("""CREATE TABLE scrape_tb(
                    title TEXT,
                    price TEXT,
                    img_url TEXT,
                    get_details TEXT
            )""")
    
    def process_item(self, item, spider):
        item['get_details'] = json.dumps(item['get_details'])
        print(item, '\n\n')
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute("""INSERT INTO scrape_tb VALUES (?,?,?,?)""",(
            item['title'],
            item['price'],
            item['img_url'],
            item['get_details']
        ))
        self.conn.commit()