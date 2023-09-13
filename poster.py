import tkinter as tk
from PIL import Image, ImageTk


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='#6393a6')
        self.controller = controller
        
        # ------------------------------------------------------------------------------------------------
        
        
        label = tk.Label(self, text="NATIONAL EDUCATION POLICY", font=("Times New Roman", 30,"bold"), bg="#6393a6")
        label.place(x=770, y=60)

        def move_label():
            x, y = label.winfo_x(), 60
            while x <=70:
                break
            else: 
                label.place(x=x-2, y=y)
                
            self.after(10, move_label)

        move_label()

        label1 = tk.Label(self, text="The National Education Policy is a", font=("Helvetica Neue", 17, "bold"), bg="#6393a6")
        label1.place(x=170, y=150)

        label2 = tk.Label(self, text="comprehensive framework for education in India.", font=("Helvetica Neue", 17, "bold"), bg="#6393a6")
        label2.place(x=100, y=190)

        label3 = tk.Label(self, text="The policy was last revised in 2020,", font=("Helvetica Neue", 17, "bold"), bg="#6393a6")
        label3.place(x=170, y=248)

        label4 = tk.Label(self, text="it seeks to transform the Indian education system.", font=("Helvetica Neue", 17, "bold"), bg="#6393a6")
        label4.place(x=100, y=285)

        
        # ----------------------------------------------------------------------------------------------------

        def move():
            show()
            show_btn()
            
        def show(x=1800):
            if x > 50:
                canvas.place(x=x, y=570)
                self.after(30, show, x-10)
                

                
        bg_canvas = tk.Canvas(self, width= 1700, height=415, background="#6393a6", highlightthickness=0)
        bg_canvas.place(x=-10, y=470)
        

        canvas = tk.Canvas(self, width=1700, height=190, background="#6393a6", highlightthickness=0)
        canvas.place(x=1800,y=570)

        bg_canvas.create_rectangle(0,295,1700,800, width=4, fill="#009A17")

        #track
        bg_canvas.create_line(0,295, 1700,295, width=4)
        bg_canvas.create_line(0,310, 1700,310, width=4)

        
        xx1 = 30
        xx2 = 70
        for i in range(30):
            bg_canvas.create_rectangle(xx1,310,xx2,320, width=3, fill="black")
            xx1 += 50
            xx2 += 50
            xx1 += 20
            xx2 += 20
            
    

        canvas.create_oval(37,110, 50,130, width=2, fill='#4C4C47',outline='#4C4C47')
        canvas.create_rectangle(73,78, 103,90, width=2, fill='#4C4C47',outline='#4C4C47')
        canvas.create_line(63,88, 115,88, width=6, fill='#4C4C47')
        canvas.create_polygon(55,65, 75,77, 100,77, 120,65, width=2, fill='#4C4C47')
        canvas.create_polygon(55,65, 75,55, 100,55, 120,65, width=2, fill='#4C4C47')
        canvas.create_line(72,77, 104,77, width=3, fill='#D9D8D7')
        canvas.create_rectangle(73,45, 103,55, width=2, fill='#4C4C47',outline='#4C4C47')
        canvas.create_line(72,55, 104,55, width=3, fill='#D9D8D7')
        canvas.create_line(64,44, 113,44, width=5, fill='#4C4C47')
        canvas.create_rectangle(130,75, 148,93, fill='#D9D8D7')
        canvas.create_rectangle(160,67, 180,95, fill='#D9D8D7')

        canvas.create_rectangle(60,91, 260,153, width=2, fill='#C13230',outline='#C13230')
        canvas.create_oval(45,90, 80,153, width=3, fill='#A52A28',outline='#C13230')

        canvas.create_rectangle(200,50, 300,153, width=2, fill='#183A58',outline='#183A58')
        canvas.create_rectangle(190,91, 200,153, width=2, fill='#A52A28',outline='#A52A28')
        canvas.create_rectangle(60,115, 190,115, width=5, fill='#A52A28',outline='#A52A28')

        #Black cap
        canvas.create_rectangle(190,30, 310,58, width=2, fill='#183A58')
        canvas.create_polygon(165,22, 245,8, 330,22, 255,40, fill='white', outline='white')
        canvas.create_polygon(165,20, 245,8, 330,20, 255,35, fill="#183A58")
        canvas.create_line(320,20, 320,50, width=4, fill='#183A58')

        #Engine window
        canvas.create_rectangle(218,70, 238,95, width=2, fill='#D9D8D7')
        canvas.create_rectangle(258,70, 278,95, width=2, fill='#D9D8D7')

        #Engine base
        canvas.create_rectangle(60,153, 290,175, width=2, fill='black')
        canvas.create_line(280,165, 325,165, width=10, fill='black')
        canvas.create_line(323,157, 323,173, width=5, fill='#7E2220')

        canvas.create_line(54,153, 80,153, width=4, fill='#7E2220')
        canvas.create_line(55,153, 23,188, width=4, fill='#7E2220')
        canvas.create_line(80,151, 80,187, width=4, fill='#7E2220')
        canvas.create_line(24,188, 82,188, width=4, fill='#7E2220')
        canvas.create_line(63,153, 43,188, width=4, fill='#7E2220')
        canvas.create_line(70,153, 63,188, width=4, fill='#7E2220')

        #engine wheel
        global x1,y1,x2,y2
        x1=90
        y1=155
        x2=140
        y2=191
        def wheel(x1,y1,x2,y2):
            canvas.create_oval(x1,y1, x2,y2, width=3,outline='#28242C')
            canvas.create_oval(x1+3,y1+3, x2-3,y2-3, width=3,outline='#A62929')
            
        def wheel_line(x1,y1,x2,y2):
            x1+=17
            y1+=5
            x2-=17
            y2-=5
            canvas.create_line(x1,y1, x2,y2 ,width=3, fill='#7E2220')   
            x1+=18
            y1+=1
            x2-=18
            y2-=2
            canvas.create_line(x1,y1, x2,y2, width=3, fill='#7E2220')
            x1+=10
            y1+=16
            x2-=10
            y2-=16
            canvas.create_line(x1,y1, x2,y2, width=3, fill='#7E2220')
            x1-=1
            y1-=8
            x2+=1
            y2+=8
            canvas.create_line(x1,y1, x2,y2, width=3, fill='#7E2220')
                        
        wheel(x1,y1,x2,y2)
        wheel_line(x1,y1,x2,y2)

        x11=160
        y11=155
        x22=210
        y22=190
        wheel(x11,y11,x22,y22)
        wheel_line(x11,y11,x22,y22)

        #engine_big_Wheel
        x111=230
        y111=130
        x222=310
        y222=190
        wheel(x111,y111,x222,y222)

        canvas.create_line(270,135, 270,188 ,width=4, fill='#7E2220')
        canvas.create_line(299,142, 245,177 ,width=4, fill='#7E2220')
        canvas.create_line(235,155, 308,165 ,width=4, fill='#7E2220')
        canvas.create_line(250,140, 290,182 ,width=4, fill='#7E2220')

        canvas.create_line(117,173, 185,173 ,width=4, fill='#28242C')
        canvas.create_line(183,170, 270,160  ,width=4, fill='#28242C')

        def compartment(x_1,x_2):
            
            canvas.create_oval(x_1,50, x_2,75, width=3,fill='#183A58',outline='#183A58')

            x_1+=6
            x_2-=5
            canvas.create_rectangle(x_1,70, x_2,150, width=2, fill='#C13230',outline='')

            x_1-=6
            x_2+=5
            canvas.create_rectangle(x_1,65, x_2,75, width=2,fill='#183A58',outline='#183A58')    

            canvas.create_rectangle(x_1,145, x_2,155, width=3,fill='#183A58',outline='#183A58')
            
            #train base
            x_1+=17
            x_2-=15 
            canvas.create_rectangle(x_1,157, x_2,174, width=2, fill='#4C4C47', outline="")

            x_1-=10
            x_2+=10    
            canvas.create_rectangle(x_1,162, x_2,170, width=2, fill='#4C4C47', outline="")

        def compt_wheel_line(x1,y1,x2,y2):
            x1+=28
            y1+=2
            x2-=27
            y2-=1
            canvas.create_line(x1,y1,x2,y2,width=3, fill='#7E2220')
        
            x1+=20
            y1+=8
            x2-=23
            y2-=7
            canvas.create_line(x1,y1,x2,y2,width=3, fill='#7E2220')

            x1-=43
            y1+=7
            x2+=50
            y2-=8
            canvas.create_line(x1,y1,x2,y2,width=3, fill='#7E2220')

            x1+=5
            y1-=10
            x2-=8
            y2+=11
            canvas.create_line(x1,y1,x2,y2,width=3, fill='#7E2220')

        #compartment_1

        compartment(330,530)    #comp_1
        canvas.create_line(338,159, 338,174, width=5, fill='#7E2220')
        canvas.create_line(525,159, 525,174, width=5, fill='#7E2220')

        compt_wheel_line(360,148,415,190)
        wheel(360,148,415,190)

        compt_wheel_line(440,148, 495,190)
        wheel(440,148, 495,190)

        canvas.create_line(385,170, 471,170, width=4, fill='#28242C')

        #compartment_2

        compartment(540,740)   #comp_2

        canvas.create_line(548,159, 548,174, width=5, fill='#7E2220')
        canvas.create_line(735,159, 735,174, width=5, fill='#7E2220')

        compt_wheel_line(570,148, 625,190)
        wheel(570,148, 625,190)

        compt_wheel_line(650,148, 705,190)
        wheel(650,148, 705,190)


        canvas.create_line(594,170, 681,170, width=4, fill='#28242C')


        ####compartment_3

        compartment(750,950)    #comp_3

        canvas.create_line(758,159, 758,174, width=5, fill='#7E2220')
        canvas.create_line(945,159, 945,174, width=5, fill='#7E2220')

        compt_wheel_line(780,148, 835,190)
        wheel(780,148, 835,190)

        compt_wheel_line(860,148, 915,190)
        wheel(860,148, 915,190)

        canvas.create_line(804,170, 891,170, width=4, fill='#28242C')

 

        #compartment_4

        compartment(960,1160)     #comp_4

        canvas.create_line(968,159, 968,174, width=5, fill='#7E2220')
        canvas.create_line(1155,159, 1155,174, width=5, fill='#7E2220')

        compt_wheel_line(990,148, 1045,190)
        wheel(990,148, 1045,190)

        compt_wheel_line(1070,148, 1125,190)
        wheel(1070,148, 1125,190)

        canvas.create_line(1014,170, 1101,170, width=4, fill='#28242C')


        #compartment_5
        compartment(1170,1370)

        canvas.create_line(1178,159, 1178,174, width=5, fill='#7E2220')
        canvas.create_line(1365,159, 1365,174, width=5, fill='#7E2220')

        compt_wheel_line(1200,148, 1255,190)
        wheel(1200,148, 1255,190)

        compt_wheel_line(1280,148, 1335,190)
        wheel(1280,148, 1335,190)

        canvas.create_line(1224,170, 1311,170, width=4, fill='#28242C')
        
        btn_train = tk.Button(self, text="FEATURES",font=("Times",20, "bold"),bg="#6393a6",command=lambda:move())
        btn_train.place(x = 290, y = 360)
        
        # -----------------------------------------------------------------------------------------------------------------

        info_canvas = tk.Canvas(self, width=750, height=470, highlightthickness=10, highlightbackground="#6393a6", bg="#183E59")
        info_canvas.place(x=770, y=0)

       
        def update(i):
            # info_canvas.delete("all")
            info_canvas.itemconfig(a, image = info[i][0])
            info_canvas.itemconfig(b, text = info[i][1])
            info_canvas.itemconfig(c, text = info[i][2])
        
        def resize_image(e):
            global a, info, b, c
            
            info = [
                [
                    ImageTk.PhotoImage(Image.open("welcome_1.png")), 
                    "NAMASTE",
                    "Let's take a close view on the\nFeatures of NEP."
                ],
                
                [
                    ImageTk.PhotoImage(Image.open("access_edu_1.png")), 
                    "ACCESS TO EDUCATION",
                    "One of the primary goals of a national educational policy is to ensure that every child has access to education, regardless of their socioeconomic status, gender, or ethnicity. \n\n\nThis may involve increasing the number of schools and classrooms, providing transportation for students in remote areas, and providing financial assistance for families who cannot afford to pay for their children's education."
                ],
                
                [
                    ImageTk.PhotoImage(Image.open("curriculum_1.png")), 
                    "CURRICULUM DEVELOPMENT",
                    "National educational policies also typically include guidelines for the development of curricula that are relevant, up-to-date, and aligned with the needs of the country's workforce and society. \n\n\nThis may involve identifying key subjects that are essential for students to learn, such as language, mathematics, and science, and creating standards and benchmarks for student achievement in these areas."
                ],
                
                [
                    ImageTk.PhotoImage(Image.open("teacher_1.png")), 
                    "TEACHER DEVELOPMENT",
                    "To ensure that students receive quality education, national educational policies often include provisions for teacher training and development. \n\n\nThis may involve providing teachers with ongoing professional development opportunities, such as workshops and seminars, and ensuring that teachers have access to the latest teaching methods and technology."
                ],
                
                [
                    ImageTk.PhotoImage(Image.open("evaluation_1.png")), 
                    "ASSESSMENT AND EVALUATION",
                    "National educational policies often include provisions for assessing and evaluating student performance and teacher effectiveness. \n\n\nThis may involve developing standardized tests and other measures to evaluate student achievement and tracking student progress over time. It may also involve evaluating teacher performance through classroom observations, student feedback, and other methods."
                ],
                
                [
                    ImageTk.PhotoImage(Image.open("resource_1.png")), 
                    "RESOURCE ALLOCATION",
                    "National educational policies typically address issues related to funding and resource allocation, including how much funding should be allocated to education, how it should be distributed among schools, and how it should be used to support student learning. \n\n\nThis may involve establishing mechanisms for accountability and transparency in the use of education funds and ensuring that schools in disadvantaged areas receive adequate resources to meet the needs of their students."
                ]
            ]
            
            a = info_canvas.create_image(20, 220, image=info[0][0], anchor='nw')
            b = info_canvas.create_text(400,100,text=info[0][1],font=("Times New Roman", 30, 'bold'), fill='white', width=700)
            c = info_canvas.create_text(530, 300, text=info[0][2], font=("Helvetica Neue", 13, 'bold'), fill='white', width=350)

            
        
            
        btn_1 = tk.Button(self, text=" Access to \nEducation",font=("Helvetica Neue",16, "bold"),bg="#C13230",command=lambda:update(1),borderwidth=0, activebackground="#C13230")
        btn_1.place(x = 1900, y = 649)
        
        
        btn_2 = tk.Button(self, text="Curriculum \nDevelopment",font=("Helvetica Neue",16, "bold"),bg="#C13230",command=lambda:update(2),borderwidth=0, activebackground="#C13230")
        btn_2.place(x = 1900, y = 649)
        
        btn_3 = tk.Button(self, text=" Teacher \nTraining",font=("Helvetica Neue",16, "bold"),bg="#C13230",command=lambda:update(3),borderwidth=0, activebackground="#C13230")
        btn_3.place(x = 1900, y = 649)
        
        btn_4 = tk.Button(self, text="Assessment\nEvaluation",font=("Helvetica Neue",16, "bold"),bg="#C13230",command=lambda:update(4),borderwidth=0, activebackground="#C13230")
        btn_4.place(x = 1900, y = 649)
        
        btn_5 = tk.Button(self, text="Resource\nAllocation",font=("Helvetica Neue",16, "bold"),bg="#C13230",command=lambda:update(5),borderwidth=0, activebackground="#C13230")
        btn_5.place(x = 1900, y = 649)
        
        def show_btn(x=2180):
            y=649
            if x > 435:
                btn_1.place(x=x+830, y=y)
                btn_2.place(x=x+610, y=y)
                btn_3.place(x=x+415, y=y)
                btn_4.place(x=x+195, y=y)
                btn_5.place(x=x, y=y)
                self.after(30, show_btn, x-10)
                
        
        
            
        # Bind the function to configure the parent window
        self.bind("<Configure>", resize_image)
        
        # ------------------------------------------------------------------------

        back_btn = tk.Button(self, text="Back",font=("Helvetica Neue",16, "bold"),bg="#009A17",command=lambda: controller.show_frame("StartPage"))
        back_btn.place(x = 1250, y = 810)
        
        exit_btn = tk.Button(self, text="Exit",font=("Helvetica Neue",16, "bold"),bg="#009A17",command=self.controller.destroy)
        exit_btn.place(x = 1350, y = 810)