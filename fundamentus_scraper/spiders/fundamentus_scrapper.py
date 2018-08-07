# coding: utf-8
import scrapy


class PaperScrapper(scrapy.Spider):
    name = "fundamentus"

    def __init__(self, *args, **kwargs): 
      super(PaperScrapper, self).__init__(*args, **kwargs) 
      self.start_urls = [kwargs.get('start_url')] 
      self.start_requests()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tables = []
        for table in response.xpath('//table'):
            yield {
                tables.append(self.retrieve_table(table))
            }

        tables[0] = self.extract_table_info(tables[0] + tables[1])
        tables[2] = self.extract_table_info(tables[2], 1)
        tables[3] = self.extract_table_info(tables[3], 2)
        tables[4] = self.extract_table_info(tables[4], 3)

        company = { 'info': tables[0],
                    'oscilations': tables[2]['oscilations'],
                    'fundamentals': tables[2]['fundamentals'],
                    'patrimonial_balance_data': tables[3],
                    'demonstrative_results_data': tables[4] }

        import json
        with open('data.json', 'w') as f:
            json.dump(company, f, ensure_ascii=False)
        # with open('data.json', 'w') as outfile:
        #     json.dumps(company, ensure_ascii=False)

    def extract_table_info(self, table, extraction_type=0):
        company_info = {}

        if extraction_type == 0:
            for row in table:
                for j in range(0, len(row), 2):
                    if j % 2 == 0:
                        company_info[row[j]] = row[j+1] 

            return company_info

        elif extraction_type == 1:
            table = table[1:]
            company_info = {'oscilations': {}, 'fundamentals': {}}

            for row in table:
                if table.index(row) == len(table) - 1:
                    company_info['fundamentals'][row[0]] = row[1].replace('\n', '').strip()
                else:
                    company_info['oscilations'][row[0]] = row[1]
                    row = row[2:]

                    for j in range(0, len(row), 2):
                        if j % 2 == 0:
                            company_info['fundamentals'][row[j]] = row[j+1].replace('\n', '').strip()

            return company_info

        elif extraction_type == 2:
            table = table[1:]
            for row in table:
                for j in range(0, len(row), 2):
                    if j % 2 == 0:
                        company_info[row[j]] = row[j+1] 
            return company_info

        elif extraction_type == 3:
            table = table[2:]
            company_info = {'last_year': {}, 'last_quarter': {}}

            for row in table:
                company_info['last_year'][row[0]] = row[1]
                company_info['last_quarter'][row[2]] = row[3]

            return company_info





    def retrieve_row(self, row):
        row = list(filter(lambda a: a != '?', row.xpath('td//text()').extract()))
        return row

    def retrieve_table(self, table):
        res_rows = []
        rows = table.css('tr')
        for row in rows:
            res_rows.append(self.retrieve_row(row))

        return res_rows