from tkinter import *
from random import choices


box, item, rate_box, sr_box, sr_rate, ssr_box, ssr_rate, grade = [], [], [], [], [], [], [], []


def clears():
    global box_text
    text_label.destroy()
    button_get['state'] = NORMAL


def get():
    global text_label

    text_label = Label(root, text="Save    Item:  %s      Tier:  %s       Rate:  %s"%(item_t.get(), tier_t.get(), rate_t.get()), font = 'dubai 12 bold')
    print("รับค่า    Item:  %s      Tier:  %s       Rate:  %s"%(item_t.get(), tier_t.get(), rate_t.get()))

    box.append(item_t.get())
    grade.append(tier_t.get())
    rate_box.append(float(rate_t.get()))


    if tier_t.get() == "SR" or tier_t.get() == "SSR":#ประกัน 10
                sr_box.append(item_t.get())
                sr_rate.append(float(rate_t.get()))
                if tier_t.get() == "SSR": #ประกันใหญ่
                    ssr_box.append(item_t.get())
                    ssr_rate.append(float(rate_t.get()))

    item_t.delete(0, END)
    tier_t.delete(0, END)
    rate_t.delete(0, END)

    text_label.pack()

    sampling_get['state'] = NORMAL
    button_get['state'] = DISABLED


def sampling_option():
    global garuntee_button
    global normal_button
    normal_button = Button(root, text='Normal', font = 'dubai 11 bold', command=sampling_n, bg = 'oldlace')
    normal_button.pack()
    garuntee_button = Button(root, text='Garuntee', font = 'dubai 11 bold', command=sampling_g, bg = 'tomato')
    garuntee_button.pack()


def sampling_n():
    garuntee_button['state'] = DISABLED
    Label(root, text="สุ่มแบบ Normal", font = 'dubai 11 bold').pack()

    def sampling_calculate_n():
        get = []


        roll_all = int(roll_t.get())

        count = 0
        keeper = []
        printer = []


        for roll in range(1, roll_all+1):
            get.append(choices(box, weights=rate_box, k=1))


        for unit in get:
            if unit not in keeper:
                keeper.append(unit)
        for j in keeper:
            for k in get:
                if j == k:
                    count += 1
            printer.append(count)
            count = 0
        keeper = [i[0] for i in keeper]
        for l in range(len(keeper)):
            print("ได้รับ     %s"%keeper[l], end = " ")
            print("จำนวน     %s"%printer[l]+' ชิ้น')



    roll_label = Label(root, text="กี่ Roll", font = 'dubai 11 bold')
    roll_label.pack()
    roll_t = Entry(root)
    roll_t.pack()


    normal_submit = Button(root, text='Submit', font = 'dubai 11 bold', command=sampling_calculate_n,  bg = 'tomato')
    normal_submit.pack()


def sampling_g():
    normal_button['state'] = DISABLED
    Label(root, text="สุ่มแบบมี Garuntee", font = 'dubai 11 bold').pack()

    def sampling_calculate_g():
        get = []

        garuntee = 0
        garuntee_option = int(garuntee_option_t.get())
        roll_all = int(roll_t.get())


        count = 0
        keeper = []
        printer = []


        for roll in range(1, roll_all+1):
            garuntee += 1
            if roll % 10 != 0:
                get.append(choices(box, weights=rate_box, k=1))
                if choices(box, weights=rate_box, k=1) in ssr_box: #ถ้าได้ SSR การันตีจะรีกับไปที่ 0
                    garuntee = 0
            else:
                if garuntee == garuntee_option: #ได้ SSR แน่นอน การันตีจะรีกับไปที่ 0
                    get.append(choices(ssr_box, weights=ssr_rate, k=1)) # สุ่ม SSR
                    garuntee = 0
                else:
                    get.append(choices(sr_box, weights=sr_rate, k=1)) # สุ่ม SR
                    if choices(sr_box, weights=sr_rate, k=1) in ssr_box: #ถ้าได้ SSR การันตีจะรีกับไปที่ 0
                        garuntee = 0

        #for i in range(len(get)):
            #print(get[i][0])
            #time.sleep(0.2)
        for unit in get:
            if unit not in keeper:
                keeper.append(unit)
        for j in keeper:
            for k in get:
                if j == k:
                    count += 1
            printer.append(count)
            count = 0
        keeper = [i[0] for i in keeper]
        for l in range(len(keeper)):
            print("ได้รับ     %s"%keeper[l], end = " ")
            print("จำนวน     %s"%printer[l]+' ชิ้น')


    garuntee_option_label = Label(root, text="Garuntee Option(ประกัน)", font = 'dubai 11 bold')
    garuntee_option_label.pack()
    garuntee_option_t = Entry(root)
    garuntee_option_t.pack()



    roll_label = Label(root, text="กี่ Roll", font = 'dubai 11 bold')
    roll_label.pack()
    roll_t = Entry(root)
    roll_t.pack()

    garuntee_submit = Button(root, text='Submit', command=sampling_calculate_g, font = 'dubai 11 bold', bg = 'tomato')
    garuntee_submit.pack()






root = Tk()
root.title("Gacha_simulater")
root.geometry("500x700")


item_label = Label(root, text="Item", font = 'dubai 11 bold')
item_label.pack()
item_t = Entry(root, width=40)
item_t.pack()


tier_label = Label(root, text="Tier", font = 'dubai 11 bold')
tier_label.pack()
tier_t = Entry(root, width=40)
tier_t.pack()

rate_label = Label(root, text="Rate", font = 'dubai 11 bold')
rate_label.pack()
rate_t = Entry(root, width=40)
rate_t.pack()

button_frame = Frame(root)
button_frame.pack()

button_get = Button(root, text='Get', font = 'dubai 11 bold', command = get, bg = 'tomato')
button_get.pack()

button_clear = Button(root, text='Clear', font = 'dubai 11 bold', command = clears, bg = 'oldlace')
button_clear.pack()




sampling_get = Button(root, text='Sampling', font = 'dubai 11 bold', command = sampling_option, bg = 'tomato')
sampling_get['state'] = DISABLED
sampling_get.pack()




root.mainloop()
