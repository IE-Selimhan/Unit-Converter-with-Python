from tkinter import *
from tkinter import ttk 

def calculateFeetToMeters(*args):
    try:
        value = float(firstValue.get())
        secondValue.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
def calculateMileToKilometers(*args):
    try:
        value = float(firstValue.get())
        secondValue.set(int(1.6093 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
def calculateinchToCentimeters(*args):
    try:
        value = float(firstValue.get())
        secondValue.set(int(2.5400 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
def calculategallonToLiters(*args):
    try:
        value = float(firstValue.get())
        secondValue.set(int(3.7854 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
def calculatelbsToKilograms(*args):
    try:
        value = float(firstValue.get())
        secondValue.set(int(0.4535 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

app = Tk()
app.title("Unit Converter")

def selected(event):
	global firstValue
	global secondValue
	if optionsCombo.get() == "FEET TO METERS":
		mainframe = ttk.Frame(app, padding="4 4 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		app.columnconfigure(0, weight=1)
		app.rowconfigure(0, weight=1)

		firstValue = StringVar()
		feet_entry = ttk.Entry(mainframe, width=7, textvariable=firstValue)
		feet_entry.grid(column=2, row=1, sticky=(W, E))

		secondValue = StringVar()
		ttk.Label(mainframe, textvariable=secondValue).grid(column=2, row=2, sticky=(W, E))

		ttk.Button(mainframe, text="Calculate", command=calculateFeetToMeters).grid(column=3, row=3, sticky=W)

		ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
		ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
		ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

		for child in mainframe.winfo_children():
			child.grid_configure(padx=5, pady=5)
		feet_entry.focus()
		app.bind("<Return>", calculateFeetToMeters)

	elif optionsCombo.get() == "MILE TO KILOMETERS":
		mainframe = ttk.Frame(app, padding="4 4 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		app.columnconfigure(0, weight=1)
		app.rowconfigure(0, weight=1)

		firstValue = StringVar()
		mile_entry = ttk.Entry(mainframe, width=7, textvariable=firstValue)
		mile_entry.grid(column=2, row=1, sticky=(W, E))

		secondValue = StringVar()
		ttk.Label(mainframe, textvariable=secondValue).grid(column=2, row=2, sticky=(W, E))

		ttk.Button(mainframe, text="Calculate", command=calculateMileToKilometers).grid(column=3, row=3, sticky=W)

		ttk.Label(mainframe, text="mile").grid(column=3, row=1, sticky=W)
		ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
		ttk.Label(mainframe, text="kilometers").grid(column=3, row=2, sticky=W)

		for child in mainframe.winfo_children():
			child.grid_configure(padx=5, pady=5)

		mile_entry.focus()
		app.bind("<Return>", calculateMileToKilometers)

	elif optionsCombo.get() == "INCHES TO CENTIMETERS":
		mainframe = ttk.Frame(app, padding="4 4 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		app.columnconfigure(0, weight=1)
		app.rowconfigure(0, weight=1)

		firstValue = StringVar()
		inches_entry = ttk.Entry(mainframe, width=7, textvariable=firstValue)
		inches_entry.grid(column=2, row=1, sticky=(W, E))

		secondValue = StringVar()
		ttk.Label(mainframe, textvariable=secondValue).grid(column=2, row=2, sticky=(W, E))

		ttk.Button(mainframe, text="Calculate", command=calculateinchToCentimeters).grid(column=3, row=3, sticky=W)

		ttk.Label(mainframe, text="inches").grid(column=3, row=1, sticky=W)
		ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
		ttk.Label(mainframe, text="centimeters").grid(column=3, row=2, sticky=W)

		for child in mainframe.winfo_children():
			child.grid_configure(padx=5, pady=5)

		inches_entry.focus()
		app.bind("<Return>", calculateinchToCentimeters)

	elif optionsCombo.get() == "GALLON TO LITERS":
		mainframe = ttk.Frame(app, padding="4 4 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		app.columnconfigure(0, weight=1)
		app.rowconfigure(0, weight=1)

		firstValue = StringVar()
		gallon_entry = ttk.Entry(mainframe, width=7, textvariable=firstValue)
		gallon_entry.grid(column=2, row=1, sticky=(W, E))

		secondValue = StringVar()
		ttk.Label(mainframe, textvariable=secondValue).grid(column=2, row=2, sticky=(W, E))

		ttk.Button(mainframe, text="Calculate", command=calculategallonToLiters).grid(column=3, row=3, sticky=W)

		ttk.Label(mainframe, text="gallon").grid(column=3, row=1, sticky=W)
		ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
		ttk.Label(mainframe, text="liters").grid(column=3, row=2, sticky=W)

		for child in mainframe.winfo_children():
			child.grid_configure(padx=5, pady=5)

		gallon_entry.focus()
		app.bind("<Return>", calculategallonToLiters)

	else:
		optionsCombo.get() == "POUND TO KILOGRAMS"
		mainframe = ttk.Frame(app, padding="4 4 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		app.columnconfigure(0, weight=1)
		app.rowconfigure(0, weight=1)

		firstValue = StringVar()
		lbs_entry = ttk.Entry(mainframe, width=7, textvariable=firstValue)
		lbs_entry.grid(column=2, row=1, sticky=(W, E))

		secondValue = StringVar()
		ttk.Label(mainframe, textvariable=secondValue).grid(column=2, row=2, sticky=(W, E))

		ttk.Button(mainframe, text="Calculate", command=calculatelbsToKilograms).grid(column=3, row=3, sticky=W)

		ttk.Label(mainframe, text="pound").grid(column=3, row=1, sticky=W)
		ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
		ttk.Label(mainframe, text="kilograms").grid(column=3, row=2, sticky=W)

		for child in mainframe.winfo_children():
			child.grid_configure(padx=5, pady=5)

		lbs_entry.focus()
		app.bind("<Return>", calculatelbsToKilograms)

options = [
	"FEET TO METERS",
	"MILE TO KILOMETERS",
	"INCHES TO CENTIMETERS",
	"GALLON TO LITERS",
	"POUND TO KILOGRAMS",
	]

optionsCombo = ttk.Combobox(app, value=options)
optionsCombo.set("Select Units")
optionsCombo.bind("<<ComboboxSelected>>", selected)
optionsCombo.grid(column=4, row=4, sticky=E)




app.mainloop()

