# Purpose: To create a python GUI with a list of maintenance services in the
# form of check buttons. Users will select the services and the total will
# display after selecting all the services.

import tkinter

class AutomotiveGUI:
    def __init__(self):
        # Create the root widget
        self.main_window = tkinter.Tk()

        # Create three frames. Middle for the check buttons and the two for labels.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create seven IntVar objects to use with the Checkbuttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # Create the checkbutton widgets in the mid frame.
        msg = tkinter.Message(self.mid_frame, text ='Welcome to the Automotive Shop. What services can we help you with today?')
        msg.config(bg='red', font=('times', 24))
        self.cb1 = tkinter.Checkbutton(self.mid_frame, text='Oil Change - $30.00', \
                                       variable=self.cb_var1, \
                                       command=self.oil_change)
        self.cb2 = tkinter.Checkbutton(self.mid_frame, text='Lube Job - $20.00', \
                                       variable=self.cb_var2, \
                                       command=self.lube_job)
        self.cb3 = tkinter.Checkbutton(self.mid_frame, text='Radiator Flush - $40.00', \
                                       variable=self.cb_var3, \
                                       command=self.radiator_flush)
        self.cb4 = tkinter.Checkbutton(self.mid_frame, text='Transmission Flush - $100.00', \
                                       variable=self.cb_var4, \
                                       command=self.transmission_flush)
        self.cb5 = tkinter.Checkbutton(self.mid_frame, text='Inspection - $35.00', \
                                       variable=self.cb_var5, \
                                       command=self.inspection)
        self.cb6 = tkinter.Checkbutton(self.mid_frame, text='Muffler Replacement - $200.00', \
                                       variable=self.cb_var6, \
                                       command=self.muffler)
        self.cb7 = tkinter.Checkbutton(self.mid_frame, text='Tire Rotation - $20.00', \
                                       variable=self.cb_var7, \
                                       command=self.tire_rotation)

        # Pack the Checkbuttons
        msg.pack()
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Create and pack the Label widgets for bottom frame.
        self.bottom_label = tkinter.Label(self.bottom_frame, text='Your Total for these services is $')
        self.total = tkinter.StringVar()
        self.total.set('0.00')
        self.total_label = tkinter.Label(self.bottom_frame, \
                                         textvariable = self.total)
        self.bottom_label.pack(side='left')
        self.total_label.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop.
        tkinter.mainloop()

    # function to update the self.total value, each service becomes a
    # individual function and when checked it will add the desired amount
    print('Welcome to the Automotive Shop, what services can we help you with today?')
    def oil_change(self):
        total = float(self.total.get())
        if self.cb_var1.get():
            total += 30.00
        else:
            total -= 30.00
        total = format(total, '.2f')
        self.total.set(total)
    def lube_job(self):
        total = float(self.total.get())
        if self.cb_var2.get():
            total += 20.00
        else:
            total -= 20.00
        total = format(total, '.2f')
        self.total.set(total)
    def radiator_flush(self):
        total = float(self.total.get())
        if self.cb_var3.get():
            total += 40.00
        else:
            total -= 40.00
        total = format(total, '.2f')
        self.total.set(total)
    def transmission_flush(self):
        total = float(self.total.get())
        if self.cb_var4.get():
            total += 100.00
        else:
            total -= 100.00
        total = format(total, '.2f')
        self.total.set(total)
    def inspection(self):
        total = float(self.total.get())
        if self.cb_var5.get():
            total += 35.00
        else:
            total -= 35.00
        total = format(total, '.2f')
        self.total.set(total)
    def muffler(self):
        total = float(self.total.get())
        if self.cb_var6.get():
            total += 200.00
        else:
            total -= 200.00
        total = format(total, '.2f')
        self.total.set(total)
    def tire_rotation(self):
        total = float(self.total.get())
        if self.cb_var7.get():
            total += 20.00
        else:
            total -= 20.00

          
        total = format(total, '.2f')
        self.total.set(total)

# Create an instance of the AutomotiveGUI class.
auto_gui = AutomotiveGUI()
         

        
              

