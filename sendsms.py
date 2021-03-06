from flask import Flask,request
from kavenegar import *
import sys


app = Flask(__name__)
@app.route('/sendsms',methods=['POST'])
def sensms():
    try:
        msg = request.get_json()
        print(msg)
        req_data = request.get_json()
        dashboardId = req_data['dashboardId']
        messageg = req_data['message']
        ruleName = req_data['ruleName']
        state = req_data['state']
        title = req_data['title']
        api = KavenegarAPI('TOKEN')
        params = {
            'sender': 'senderNUMBER',#optional
            'receptor': '',#multiple mobile number, split by comma
            'message': "dashboardId = {} \nmessageg = {} \nruleName = {} \nstate = {} \ntitle ={}".format(dashboardId, messageg, ruleName, state, title)
        }
        response = api.sms_send(params)
        return(response)
    except APIException as e:
        return(e)
    except HTTPException as e:
        return(e)

    #return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)

