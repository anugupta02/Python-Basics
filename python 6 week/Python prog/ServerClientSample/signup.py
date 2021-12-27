import smtplib
ser = smtplib.SMTP('smtp.gmail.com',587)
ser.starttls()
ser.login('anugupta02021996@gmail.com','ALure@02*96')
msg = "Hays"
ser.sendmail('anugupta02021996@gmail.com','akashgupta0202@gmail.com',msg)
print("Sent")
ser.close()