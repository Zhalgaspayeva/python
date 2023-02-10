class String:
    def getString(self, str):
        self.str = str

    def printString(self):
        print((self.str).upper())

st = String()
st.getString(input())
st.printString()


    