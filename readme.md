## Fundamentus Scrapper
A simple [scrapy](https://scrapy.org/) web crawler to retrieve the data of a company stocks info from [Fundamentus](http://www.fundamentus.com.br).


#### Dependencies:
 -  python  3.6
 -   scrapy
#### How to use
After installing the required dependencies, download the project and in the root folder run the following command:

    scrapy crawl fundamentus -a start_url="http://www.fundamentus.com.br/detalhes.php?papel=MY_COMPANY_PAPER"
Where 'MY_COMPANY_PAPER' is the company paper you want to search for. The scrapper will generate a json file that contains the data of the company in the following format:

    {
	"info": {
		"Papel": "TAEE11",
		"Cotação": "20,32",
		"Tipo": "UNT",
		"Data últ cot": "06/08/2018",
		"Empresa": "TAESA UNT",
		"Min 52 sem": "18,09",
		"Setor": "Energia Elétrica",
		"Max 52 sem": "22,11",
		"Subsetor": "Energia Elétrica",
		"Vol $ méd (2m)": "25.863.200",
		"Valor de mercado": "7.000.220.000",
		"Últ balanço processado": "30/06/2018",
		"Valor da firma": "10.039.700.000",
		"Nro. Ações": "1.033.500.000"
	},
	"oscilations": {
		"Dia": "-0,20%",
		"Mês": "1,09%",
		"30 dias": "3,25%",
		"12 meses": "-6,53%",
		"2018": "0,84%",
		"2017": "10,96%",
		"2016": "40,67%",
		"2015": "-0,62%",
		"2014": "20,06%",
		"2013": "-6,80%"
	},
	"fundamentals": {
		"P/L": "8,22",
		"LPA": "2,47",
		"P/VP": "1,59",
		"VPA": "12,80",
		"P/EBIT": "7,79",
		"Marg. Bruta": "82,6%",
		"PSR": "5,63",
		"Marg. EBIT": "72,3%",
		"P/Ativos": "0,85",
		"Marg. Líquida": "68,5%",
		"P/Cap. Giro": "5,07",
		"EBIT / Ativo": "11,0%",
		"P/Ativ Circ Liq": "-4,06",
		"ROIC": "11,2%",
		"Div. Yield": "9,6%",
		"ROE": "19,3%",
		"EV / EBIT": "11,18",
		"Liquidez Corr": "3,03",
		"Giro Ativos": "0,15",
		"Div Br/ Patrim": "0,71",
		"Cres. Rec (5a)": "-6,6%"
	},
	"patrimonial_balance_data": {
		"Ativo": "8.193.880.000",
		"Dív. Bruta": "3.151.880.000",
		"Disponibilidades": "112.379.000",
		"Dív. Líquida": "3.039.500.000",
		"Ativo Circulante": "2.060.750.000",
		"Patrim. Líq": "4.410.910.000"
	},
	"demonstrative_results_data": {
		"last_year": {
			"Receita Líquida": "1.243.410.000",
			"EBIT": "898.406.000",
			"Lucro Líquido": "851.412.000"
		},
		"last_quarter": {
			"Receita Líquida": "351.238.000",
			"EBIT": "269.846.000",
			"Lucro Líquido": "259.251.000"
		}
	}
}

Please bear in mind that the Fundamentus website only contains brazilian companies.

Enjoy.