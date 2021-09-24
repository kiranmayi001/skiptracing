from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright



app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    NAME = request.form['name']
    EMAIL= request.form['email']
    WMOBILE = request.form['wmob']
    org = request.form['Org']
    DESIGNATION = request.form['Desi']
    WCITY = request.form['Wcity']

    RE = (NAME).replace(" ", "+") + "+" + (org).replace(" ", "+") + "+" + EMAIL + "+" + WMOBILE + "+" + (
        DESIGNATION).replace(" ", "+") + "+" + WCITY
    url = "https://www.google.com/search?q=" + RE
    info = []
    data= []
    li = []
    links = []
    p = sync_playwright().start()
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    src = (page.content())
    soup = BeautifulSoup(src, 'lxml')
    containers = soup.find_all('div', {'class': 'g'})
    for i in containers:
        info.append(i)
    cont1 = info[0].get_text().strip()
    cont2 = info[1].get_text().strip()
    cont3 = info[2].get_text().strip()
    cont4 = info[3].get_text().strip()
    cont5 = info[4].get_text().strip()
    cont6 = info[5].get_text().strip()
    cont7 = info[6].get_text().strip()
    cont8 = info[7].get_text().strip()

    data.append(cont1)
    data.append(cont2)
    data.append(cont3)
    data.append(cont4)
    data.append(cont5)
    data.append(cont6)
    data.append(cont7)
    data.append(cont8)
    data1 = list(data)


    return render_template("after.html",data1=data1)






if __name__ == '__main__':
    app.run(port=8080,debug=True)