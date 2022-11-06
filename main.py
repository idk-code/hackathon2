# Flask Setup
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from flask import Flask, jsonify, request, abort
from flask import render_template
app = Flask(__name__)

# Google Sheets API Setup
credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",
                                                               "https://www.googleapis.com/auth/spreadsheets",
                                                               "https://www.googleapis.com/auth/drive.file",
                                                               "https://www.googleapis.com/auth/drive"])

client = gspread.authorize(credential)
gsheet = client.open("Hungry in Chapel Hill").sheet1
# An example GET Route to get all reviews



@app.route("/")
def index():
    print(gsheet.get_all_records())
    myData = []
    gsheet.sort((5, 'asc'))
    for x in gsheet.get_all_records():
        #print(x['Date'])
        myData.append(x)
    return render_template('index.html', test=myData)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
