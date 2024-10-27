# cn-project
intruder detection system
Given proect uses the simple usage of arrays in python to detect changes in environment and adds variable if changes are detected

opencv is used for video detection and processing
an external app twilio is used to send message to respective personel regarding intrusion

prerequistile softwares required
{run these commands in terminal post python installation}
pip install opencv-python
pip install cvzone
pip install twilio
pip install mediapipe(or reccomended to update existing python version)


#twilo process
->create account
->services-> send an sms
->get a trial phone no(be sure to copy auth token)
->create addition function sendsms():

*note* need to update auth token each time
