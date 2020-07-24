import tkinter as tk

event_name_label = tk.Label(text = 'Event Name')
event_name_label.grid(row = 0,column = 1)
info_bt1 = tk.Button( text='Infomation', width=20, height=2)
info_bt1.grid(row=1, column=1, sticky='E')
join_event_bt = tk.Button(text='Join Event', width=20, height=2)
join_event_bt.grid(row=1, column=0, sticky='E')
cancel_bt = tk.Button(text='Cancel', width=20, height=2)
cancel_bt.grid(row=1, column=2, sticky='E')

tk.mainloop()