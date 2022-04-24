def Test1():
    #Runs the "Orders" tested application.
    TestedApps.Orders.Run(1, True)
    #Clicks the 'MainForm' object.
    Aliases.Orders.MainForm.Click(62, 29)
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("File|Open...")
    #Opens the 'C:\Sonia\Repo\Sample-Orders\Orders\added.tbl' file via the 'dlgOpen' dialog.
    Aliases.Orders.dlgOpen.OpenFile("C:\\Sonia\\Repo\\Sample-Orders\\Orders\\added.tbl", "Table (*.tbl)")
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.Orders.MainForm.MainMenu.Click("Orders|New order...")
    #Clicks the 'Customer' object.
    Aliases.Orders.OrderForm.Group.Customer.Click(18, 5)
    #Enters the text 'dfft' in the 'Customer' text editor.
    Aliases.Orders.OrderForm.Group.Customer.SetText("dfft")
    #Clicks the 'Street' object.
    Aliases.Orders.OrderForm.Group.Street.Click(35, 5)
    #Enters the text 'sfr' in the 'Street' text editor.
    Aliases.Orders.OrderForm.Group.Street.SetText("sfr")
    #Clicks the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Click(32, 12)
    #Enters '[Caps]' in the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Keys("[Caps]")
    #Enters the text 'A' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("A")
    #Enters '[Caps]' in the 'State' object.
    Aliases.Orders.OrderForm.Group.State.Keys("[Caps]")
    #Enters the text 'Ap' in the 'State' text editor.
    Aliases.Orders.OrderForm.Group.State.SetText("Ap")
    #Clicks the 'City' object.
    Aliases.Orders.OrderForm.Group.City.Click(40, 6)
    #Enters the text 'fd' in the 'City' text editor.
    Aliases.Orders.OrderForm.Group.City.SetText("fd")
    #Clicks the 'Zip' object.
    Aliases.Orders.OrderForm.Group.Zip.Click(30, 14)
    #Enters the text '6567' in the 'Zip' text editor.
    Aliases.Orders.OrderForm.Group.Zip.SetText("6567")
    #Clicks the 'CardNo' object.
    Aliases.Orders.OrderForm.Group.CardNo.Click(189, 13)
    #Enters the text '87678990' in the 'CardNo' text editor.
    Aliases.Orders.OrderForm.Group.CardNo.SetText("87678990")
    #Clicks the 'ButtonOK' button.
    Aliases.Orders.OrderForm.ButtonOK.ClickButton()
    #Closes the 'MainForm' window.
    Aliases.Orders.MainForm.Close()
    #Clicks the 'btnNo' button.
    Aliases.Orders.dlgConfirmation.btnNo.ClickButton()
