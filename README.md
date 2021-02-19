# Raspberry-Pi-Wired-Door-Bell

This is a simple wired door bell setup that sends a notification to your phone when it's pressed.<br/>
Note: you need access to a non-free Microsoft account with Power Automate.<br/>
You can pay for this yourself or most business accounts have it, i'm using my work account.<br/>

My Setup:<br/>
Raspberry Pi Zero W<br/>
Raspberry Pi OS<br/>
Standard Wired Door Bell (was £2.50 on amazon)<br/>
2 wires (i used 2 out of an old ethernet cable)<br/>

1. Strip the ends of the wires so there's about 1cm of bare copper showing<br/>
2. Attach the the two cables to each of the two contacts on the bell<br/>
<img src="images/bell_back.jpg" width="300">
4. Connect the other ends to the 3rd and 6th outside contacts on the Pi (you can use the same contacts no matter what Pi you're using)<br/>
<img src="images/pi_gpio.jpg" width="300">
6. Install Raspberry Pi OS Lite on a SD card, insert into your Pi and turn on<br/>
7. Setup your Pi by configuring WiFi, Hostname, Password and SSH<br/>
8. Install updates, python, python.rpi.gpio and python.requests<br/>
    *sudo apt update
    sudo apt upgrade
    sudo apt-get install python python.rpi.gpio python.requests
    sudo reboot*<br/>
7. Add the bell.py file to the root of your pi<br/>
8. Open Power Automate and sign in<br/>
9. Click Create, Automated Flow then skip<br/>
10. Add the trigger as "When a HTTP Request is received" and set the following as the body schema<br/>
    *{
        "type": "object",
        "properties": {
            "message": {
                    "type": "string"
                }
            }
    }*<br/>
11. Then add a new step called send me a mobile notification and set the text as the message tag from the previous step<br/>
12. Save the flow then copy the HTTP POST URL from the first step<br/>
<img src="images/post_notification_flow.PNG" width="300">
14. Enter the URL in the URL variable in the bell.py file<br/>
15. Run the bell.py, press the bell and see if you get a notification<br/>
Ensure you have the Power Automate app installed on your phone and signed in with the same account<br/>
    *python bell.py*<br/>
15. If its working, set the file to start on bootup<br/>
    *sudo nano /etc/rc.local*<br/>
    Add the following just before the exit 0<br/>
    *sudo python /bell.py &*<br/>
16. Reboot the pi and press the button after it boots up<br/>
