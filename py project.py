  
class Page(QWebEnginePage):
  
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()
  
    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')
  
    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()
  
def exact_url(url):
    index = url.find("B0")
    index = index + 10
    current_url = ""
    current_url = url[:index]
    return current_url
      
  
def mainprogram():
    url = "https://www.amazon.com/Redragon-K552-Mechanical-Keyboard-Equivalent/dp/B016MAK38U/ref=sr_1_1?dchild=1&keywords=gaming+keyboard&pd_rd_r=8517aadf-046a-451f-ac79-76622042a7df&pd_rd_w=kEl74&pd_rd_wg=BY97H&pf_rd_p=5811f97a-f703-4231-aa5f-c344167bfe13&pf_rd_r=JWNWYHN70DQHCF3P48MX&qid=1623160019&sr=8-1"
    exacturl = exact_url(url) # main url to extract data
    page = Page(exacturl)
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('span', id ='priceblock_ourprice')
    if js_test is None:
        js_test = soup.find('span', id ='priceblock_dealprice')        
    str = ""
    for line in js_test.stripped_strings :
        str = line
  
    # convert to integer
    str = str.replace(", ", "")
    current_price = int(float(str))
    your_price = 600
    if current_price < your_price :
        print("Price decreased book now")
        winsound.Beep(frequency, duration)
    else:
        print("Price is high please wait for the best deal")
      
def job():
    print("Tracking....")    
    mainprogram()
  
# main code
schedule.every(1).minutes.do(job)
  
while True:
    schedule.run_pending()
    time.sleep(1)