from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):

        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title= Label(self.root,text ="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #========Variables========================
       #========Cosmetics========================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gel = IntVar()
        self.lotion = IntVar()

        #========Grocery========================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.dal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        #========Cold drinks=====================
        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumps_up = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()

        #========Total products price & Tax Variables===
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()

        #=======customers=====================
        self.c_name = StringVar()
        self.c_phon_num = StringVar()

        self.c_bill_num= StringVar()
        x = random.randint(1000,1999)
        self.c_bill_num.set(str(x))

        self.search_bill= StringVar()


        #===========customer detail frame==========
        F1=LabelFrame(self.root,text="Customer Details",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Customer Name",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=0,padx=20,pady=5)
        cname_txt =Entry(F1,width=15,textvariable=self.c_name, font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        cn_phone = Label(F1,text="Phone No.",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt =Entry(F1,width=15,textvariable=self.c_phon_num,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cbill_lbl = Label(F1,text="Bill No.",font=("times new roman",18,"bold"),fg="white",bg=bg_color).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt =Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)

        bill_btn =Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)

        #===========cosmetics frame==========
        F2=LabelFrame(self.root,text="Cosmetics",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=185,width=325,height=380)

        bath_lbl = Label(F2,text="Bath Saop",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        f_cream_lbl = Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        f_cream_txt = Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        f_wash_lbl = Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        f_wash_txt = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        h_spray_lbl = Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        h_spray_txt = Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        h_gel_lbl = Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        h_gel_txt = Entry(F2,width=10,textvariable=self.gel,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        b_lotion_lbl = Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        b_lotion_txt = Entry(F2,width=10,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #===========Grocery frame==========
        F3=LabelFrame(self.root,text="Grocery",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=185,width=325,height=380)

        g1_lbl = Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt = Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl = Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt = Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl = Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt = Entry(F3,width=10,textvariable=self.dal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl = Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl = Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl = Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #===========Grocery frame==========
        F4=LabelFrame(self.root,text="Cold Drinks",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=185,width=325,height=380)

        c1_lbl = Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt = Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl = Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt = Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl = Label(F4,text="Cock",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt = Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl = Label(F4,text="Thumps Up",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt = Entry(F4,width=10,textvariable=self.thumps_up,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl = Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt = Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl = Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=======Bill Area================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1010,y=185,width=350,height=380)
        bill_title= Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scroll_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=======Button frame=============
        F6=LabelFrame(self.root,text="Bill Menu",bd=10,relief=GROOVE,font=("times new roman",18,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1= Label(F6,text="Total Cosmetics Price",bg=bg_color,fg="white",font=("times new roman", 14,"bold")).grid(row=0,column=0,padx=1,sticky="w")
        m1_text=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2= Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman", 14,"bold")).grid(row=1,column=0,padx=1,sticky="w")
        m2_text=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3= Label(F6,text="Total Cold Drinks Price",bg=bg_color,fg="white",font=("times new roman", 14,"bold")).grid(row=2,column=0,padx=1,sticky="w")
        m3_text=Entry(F6,width=18,textvariable=self.cold_drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1= Label(F6,text="Cosmetics Tax",bg=bg_color,fg="white",font=("times new roman", 14,"bold")).grid(row=0,column=2,padx=1,sticky="w")
        c1_text=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        c2= Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman", 14,"bold")).grid(row=1,column=2,padx=1,sticky="w")
        c2_text=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3= Label(F6,text="Drinks Tax",bg=bg_color,fg="white",font=("times new roman", 14,"bold")).grid(row=2,column=2,padx=1,sticky="w")
        c3_text=Entry(F6,width=18,textvariable=self.cold_drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_frame =Frame(F6,bd=7,relief=GROOVE)
        btn_frame.place(x=750,width=580,height=105)

        total_btn= Button(btn_frame,command=self.total,text="Total",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        GBill_btn= Button(btn_frame,command=self.bill_area,text="Genrate Bill",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Clear_btn= Button(btn_frame,command=self.clear_data,text="Clear",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        Exit_btn= Button(btn_frame,command=self.exit_app,text="Exit",bg="cadetblue",fg="white",bd=2,pady=15,width=10,font="arial 15 bold").grid(row=0,column=4,padx=5,pady=5)

        
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*60
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p =self.spray.get()*180
        self.c_hg_p =self.gel.get()*120
        self.c_bl_p=self.lotion.get()*180
        self.total_cosmetic_price= float(
                                self.c_s_p+
                                self.c_fc_p+
                                self.c_fw_p+
                                self.c_hs_p+
                                self.c_hg_p+
                                self.c_bl_p
                                )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax = round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))


        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*180
        self.g_d_p=self.dal.get()*60
        self.g_wh_p = self.wheat.get()*140
        self.g_sg_p =self.sugar.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price= float(
                                self.g_r_p+
                                self.g_fo_p+
                                self.g_d_p+
                                self.g_wh_p+
                                self.g_sg_p+
                                self.g_t_p
                                )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax =round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))


        self.d_m_p=self.maza.get()*60
        self.d_co_p=self.cock.get()*60
        self.d_fr_p=self.frooti.get()*50
        self.d_th_p =self.thumps_up.get()*45
        self.d_li_p =self.limca.get()*40
        self.d_sp_p=self.sprite.get()*60
        self.total_cold_drinks_price= float(
                                self.d_m_p+
                                self.d_co_p+
                                self.d_fr_p+
                                self.d_th_p+
                                self.d_li_p+
                                self.d_sp_p
                                )
        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.d_tax = round((self.total_cold_drinks_price*0.01),2)
        self.cold_drinks_tax.set("Rs. "+str(self.d_tax))

        self.total_bill= float(self.total_cosmetic_price+
                               self.total_grocery_price+
                               self.total_cold_drinks_price+
                               self.c_tax+
                               self.g_tax+
                               self.d_tax
                              )


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\twelcome customer\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.c_bill_num.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phon_num.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products\t\tQty\t\tPrice")
        self.txtarea.insert(END,f"\n======================================")

    def bill_area(self):
        self.welcome_bill()
        #=======Cosmetics=======
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        if self.face_cream.get()!=0:
            self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        if self.face_wash.get()!=0:
            self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
        if self.spray.get()!=0:
            self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
        if self.gel.get()!=0:
            self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gel.get()}\t\t{self.c_hg_p}") 
        if self.lotion.get()!=0:
            self.txtarea.insert(END,f"\n Body Lotion\t\t{self.lotion.get()}\t\t{self.c_bl_p}")     

        #=======Grocery=======  
        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get()!=0:
            self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
        if self.dal.get()!=0:
            self.txtarea.insert(END,f"\n Dal\t\t{self.dal.get()}\t\t{self.g_d_p}")
        if self.wheat.get()!=0:
            self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_wh_p}")
        if self.sugar.get()!=0:
            self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_sg_p}")
        if self.tea.get()!=0:
            self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")  

        #=======Drinks=======  
        if self.maza.get()!=0:
            self.txtarea.insert(END,f"\n Maza\t\t{self.soap.get()}\t\t{self.d_m_p}")
        if self.cock.get()!=0:
            self.txtarea.insert(END,f"\n Cock\t\t{self.cock.get()}\t\t{self.d_co_p}")   
        if self.frooti.get()!=0:
            self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_fr_p}")
        if self.thumps_up.get()!=0:
            self.txtarea.insert(END,f"\n Thumps Up\t\t{self.thumps_up.get()}\t\t{self.d_th_p}")
        if self.limca.get()!=0:
            self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_li_p}")
        if self.sprite.get()!=0:
            self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_sp_p}")    

        self.txtarea.insert(END,f"\n--------------------------------------")
        if self.cosmetic_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
        if self.grocery_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get()!="Rs. 0.0":
            self.txtarea.insert(END,f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}") 

        self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {str(self.total_bill)}")      
        self.txtarea.insert(END,f"\n--------------------------------------")
        self.saveBill()
        

    def saveBill(self):
        op = messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/" +str(self.c_bill_num.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. {self.c_bill_num.get()}saved successfully")
        else:
            return    
    
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present = "yes"

        if present == "no":
            messagebox.showerror("Error","Invaild number")    

    def clear_data(self):
          #========Cosmetics========================
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gel.set(0)
        self.lotion.set(0)

        #========Grocery========================
        self.rice.set(0)
        self.food_oil.set(0)
        self.dal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)

        #========Cold drinks=====================
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumps_up.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        #========Total products price & Tax Variables===
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_drinks_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drinks_tax.set("")

        #=======customers=====================
        self.c_name.set("")
        self.c_phon_num.set("")

        self.c_bill_num.set("")
        x = random.randint(1000,1999)
        self.c_bill_num.set(str(x))

        self.search_bill.set("")
        self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit","Do you really want to exit?") 
        if op>0:
           self.root.destroy()   
         




root=Tk()
obj = Bill_App(root)
root.mainloop()