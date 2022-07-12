
from flask import Flask, render_template, request, redirect, url_for, session

import sqlite3
import time


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        t = time.time()
        con = sqlite3.connect('GeneStudy.db')
        cur = con.cursor()
        query = request.form.get("query")
        data = cur.execute(f"select * from GeneStudy where ApprovedSymbol like '%{query}%'; ")
        result = data.fetchall()
        dataSet = []
        for row in result:
            hgncid = row[0].split(':')[1]
            approvedname = row[1]
            approvedsymbol = row[2]
            previousname = row[3]
            status = row[4]
            datenamechanged	= row[5]
            previoussymbols = row[6]	
            synonyms = row [7]

            dataDict = {
                "hgncid"   : hgncid,
                "approvedname"  : approvedname,
                "approvedsymbol"   : approvedsymbol,
                "previousname": previousname,
                "status"   : status,
                "datenamechanged"  : datenamechanged,
                "previoussymbols"   : previoussymbols,
                "synonyms"   : synonyms
                
            } 
            dataSet.append(dataDict)

        return render_template("index.html", listData=dataSet,resulttime = f'{time.time()-t:.3f}')
    
    if request.method == "GET":
        return render_template('index.html')
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)