import scrapy

class PapersSpider(scrapy.Spider):
    name = 'papers'
    allowed_domains = ['online-journals.org']
    start_urls = ['https://online-journals.org/index.php/i-jim/issue/archive']

    def parse(self, response):
        journals = response.xpath("//li/div[@class='obj_issue_summary']/h2/a")
        for journal in journals:
            vol_num = journal.xpath(".//text()").get()
            link = journal.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_journal, meta={'journal_name': vol_num})

    def parse_journal(self, response):
        name = response.request.meta['journal_name']
        articles = response.xpath("//ul[@class='cmp_article_list articles']/li")
        for article in articles:
            title = article.xpath(".//div/h3/a/text()").get()
            link_article = article.xpath(".//div/h3/a/@href").get()

            yield response.follow(url=link_article, callback=self.parse_paper, meta={'article_name': title})

    def parse_paper(self, response):
        paper = response.request.meta['article_name']
        keywords = response.xpath("//section[@class='item keywords']/span[@class='value']/text()").re('.*')
        published = response.xpath("//div[@class='value']/span/text()").re('.*')
        abstract = response.xpath("//section[@class='item abstract']/p/text()").re('.*')
        abstract2 = response.xpath("//section[@class='item abstract']/text()").re('.*')
        abstract3 = response.xpath("//section[@class='item abstract']/br/text()").re('.*')
        abstract4 = response.xpath("//section[@class='item abstract']/p/em/text()").re('.*')
        yield {
            'paper_name': paper,
            'keywords_name': keywords,
            'publishing_date': published,
            'abstract': abstract,
            'abstract2': abstract2,
            'abstract3': abstract3,
            'abstract4': abstract4
        }
