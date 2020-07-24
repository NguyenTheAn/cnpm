import tkinter as tk


label1=tk.Label(text='Event Name:')
label1.grid(row = 0,column = 0)
event_name_label = tk.Label(text = 'Event Name From DB')
event_name_label.grid(row = 0,column = 1)

label2=tk.Label(text='Description:')
label2.grid(row = 1,column = 0)
event_des_label = tk.Label(text = 'Description From DB')
event_des_label.grid(row = 1,column = 1)

label3=tk.Label(text='Start Date:')
label3.grid(row = 2,column = 0)
start_date_label = tk.Label(text = 'Date From DB' + 'Month form DB' + 'Year from DB')
start_date_label.grid(row = 2,column = 1)

label4=tk.Label(text='End Date:')
label4.grid(row = 3,column = 0)
end_date_label = tk.Label(text = 'Date From DB' + 'Month form DB' + 'Year from DB')
end_date_label.grid(row = 3,column = 1)

cancel_bt = tk.Button(text='Cancel', width=20, height=2)
cancel_bt.grid(row=4, column=2, sticky='E')

tk.mainloop()