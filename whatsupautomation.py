import pywhatkit as pw
print("NOTE:Make sure you are logged in to your whatsweb on your PC before executing this code")
phoneNo=input("Enter 10 digit whatsup number to whom you wanted to send message :")
message=input("Enter Your Msg Here :")
time=int(input("Enter hour time(24 hr pattern) : "))
min=int(input("Enter minute time  :"))

pw.sendwhatmsg("+91"+phoneNo,message,time,min);
