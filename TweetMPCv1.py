from twython import Twython
from Tkinter import *
#
app_key = "XXXX"
app_secret = "XXXXXX"
oauth_token = "XXXXXXX"
oauth_token_secret = "XXXXXXXXXXX"


#Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break






master = Tk()
Label(master, text="tweet1").grid(row=0)
Label(master, text="tweet2").grid(row=1)
Label(master, text="tweet3").grid(row=2)
Label(master, text="tweet4").grid(row=3)
Label(master, text="tweet5").grid(row=4)
Label(master, text="tweet6").grid(row=5)
Label(master, text="tweet7").grid(row=6)
Label(master, text="tweet8").grid(row=7)
Label(master, text="tweet9").grid(row=8)
Label(master, text="tweet10").grid(row=9)
######
Label(master, text="tweet11").grid(row=0, column=6)
Label(master, text="tweet12").grid(row=1, column=6)
Label(master, text="tweet13").grid(row=2, column=6)
Label(master, text="tweet14").grid(row=3, column=6)
Label(master, text="tweet15").grid(row=4, column=6)
Label(master, text="tweet16").grid(row=5, column=6)
Label(master, text="tweet17").grid(row=6, column=6)
Label(master, text="tweet18").grid(row=7, column=6)
Label(master, text="tweet19").grid(row=8, column=6)
Label(master, text="tweet20").grid(row=9, column=6)
###
Label(master, text="tweet21").grid(row=0, column=9)
Label(master, text="tweet22").grid(row=1, column=9)
Label(master, text="tweet23").grid(row=2, column=9)
Label(master, text="tweet24").grid(row=3, column=9)
Label(master, text="tweet25").grid(row=4, column=9)
Label(master, text="tweet26").grid(row=5, column=9)
Label(master, text="tweet27").grid(row=6, column=9)
Label(master, text="tweet28").grid(row=7, column=9)
Label(master, text="tweet29").grid(row=8, column=9)
Label(master, text="tweet30").grid(row=9, column=9)
###
Label(master, text="tweet31").grid(row=0, column=12)
Label(master, text="tweet32").grid(row=1, column=12)
Label(master, text="tweet33").grid(row=2, column=12)
Label(master, text="tweet34").grid(row=3, column=12)
Label(master, text="tweet35").grid(row=4, column=12)
Label(master, text="tweet36").grid(row=5, column=12)
Label(master, text="tweet37").grid(row=6, column=12)
Label(master, text="tweet38").grid(row=7, column=12)
Label(master, text="tweet39").grid(row=8, column=12)
Label(master, text="tweet40").grid(row=9, column=12)




def show_entry_field1():
   #print(e1.get())
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field2():
   #print(e2.get())
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field3():
  # print((e3.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field4():
   #print((e4.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field5():
  # print((e5.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field6():
  # print((e6.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field7():
   #print((e7.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field8():
   #print((e8.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='Ayour tweet here')
def show_entry_field9():
   #print((e9.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field10():
   #print((e10.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here ')
def show_entry_field11():
   #print((e11.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field12():
   #print((e12.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field13():
   #print((e13.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field14():
   #print((e14.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field15():
   #print((e15.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field16():
   #print((e16.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field17():
   #print((e17.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field18():
   #print((e18.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field19():
   #print((e19.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field20():
   #print((e20.get()))
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field21():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here ')
def show_entry_field22():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field23():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field24():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field25():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field26():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field27():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field28():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='Fyour tweet here')
def show_entry_field29():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field30():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field31():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field32():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field33():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='your tweet here')
def show_entry_field34():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='')
def show_entry_field35():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='')
def show_entry_field36():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='')
def show_entry_field37():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='')
def show_entry_field38():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='')
def show_entry_field39():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='')
def show_entry_field40():
   twitter.send_direct_message(user_id='gettwitter id of account you want', text='')   

Button(master, text='tweet', command=show_entry_field1).grid(row=0, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field2).grid(row=1, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field3).grid(row=2, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field4).grid(row=3, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field5).grid(row=4, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field6).grid(row=5, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field7).grid(row=6, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field8).grid(row=7, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field9).grid(row=8, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field10).grid(row=9, column=4, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field11).grid(row=0, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field12).grid(row=1, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field13).grid(row=2, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field14).grid(row=3, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field15).grid(row=4, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field16).grid(row=5, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field17).grid(row=6, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field18).grid(row=7, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field19).grid(row=8, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field20).grid(row=9, column=8, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field21).grid(row=0, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field22).grid(row=1, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field23).grid(row=2, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field24).grid(row=3, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field25).grid(row=4, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field26).grid(row=5, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field27).grid(row=6, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field28).grid(row=7, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field29).grid(row=8, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field30).grid(row=9, column=10, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field31).grid(row=0, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field32).grid(row=1, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field33).grid(row=2, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field34).grid(row=3, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field35).grid(row=4, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field36).grid(row=5, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field37).grid(row=6, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field38).grid(row=7, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field39).grid(row=8, column=13, sticky=W, pady=4)
Button(master, text='tweet', command=show_entry_field40).grid(row=9, column=13, sticky=W, pady=4)
Button(master, text='Quit', command=master.quit).grid(row=10, column=0, sticky=W, pady=9)

master.grid_columnconfigure(0,weight=1)
master.resizable(True,False)


mainloop( )
