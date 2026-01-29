while True:
    def input_char():
        char = input("Enter: ").upper()
        return char
    if input_char() == "STOP":
        print("Program stopped.")
        break

    class gp1:
        Gp1 = ["A","E","O","Y"]
        Gp2 = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"]
    class gp2:
        GP1 = []
    if input_char() in gp1.Gp1:
        print("Group 1")
    else:
        print("Group 2")  
