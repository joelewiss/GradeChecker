"""Python file for a library of constants for making connections

Don't change any of these unless you know what you're doing!
"""

connection1 = {
"Content-Type": "application/json; charset=UTF-8",
}

connection2 = {
"Content-Type": "application/x-www-form-urlencoded"
}

base = """
{
    "acctParms": {
        "forceShowAcctDlg": false,
        "forceDlgRedirectURL": "",
        "titleDlg": "Account Settings",
        "titleEmail": "Change Email Address:",
        "labelEmailPrimary": "Primary Email Address",
        "labelEmailSecondary": "Secondary Email Address",
        "titlePwd": "Change Password:",
        "labelPwdOld": "Old Password",
        "labelPwdNew": "New Password",
        "labelPwdConfirm": "Confirm Password",
        "titleSecQuestion": "Change Security Question",
        "labelSecQuestion": "Security Question",
        "buttonSave": "Save...",
        "buttonCancel": "Cancel",
        "doChangeEmail": true,
        "doChangePwd": true,
        "doChangeSecQuest": true,
        "requireSecQuest": true,
        "requireEmail": true,
        "allowedSecAnswer": 3,
        "requiredSecAnswer": 1,
        "lenEmail": 75,
        "lenPwdMin": 8,
        "lenPwdMax": 20,
        "lenSecAnswer": 128,
        "errEmail": "",
        "errPwdLen": "",
        "errPwdMissing": "",
        "errPwdMatch": "",
        "errPwdMatchConfirm": "",
        "errSecQuestMandatory": "",
        "valueEmailPrimary": "",
        "valueEmailSecondary": "",
        "valuePwdOld": "",
        "valuePwdNew": "",
        "valuePwdConfirm": "",
        "wsmGetInfo": "/WebService/OCE_ws.asmx/CheckUpdateAccountInfo",
        "wsmSetInfo": "/WebService/OCE_ws.asmx/SetAccountInfo",
        "lcid": 1033,
        "acctID": -1,
        "acctName": "",
        "sessionID": "",
        "secQuest": null,
        "secAnswer": null,
        "forceClose": false,
        "forceRedirect": false,
        "redirectURL": "",
        "showDialog": true,
        "statusButton": "OK",
        "statusCode": 0,
        "statusDesc": "",
        "statusTitle": "Web Page Error"
    }
}
"""
