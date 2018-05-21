

def main():
    def convertToBinary(n):
        """Function to print binary number
        for the input decimal using recursion"""
        if n > 1:
            convertToBinary(n // 2)
        print(n % 2, end='')

    # decimal number
    dec = int(input("Enter a dec number"))
    type(dec)


    convertToBinary(dec)


if __name__=="__main__":
    main()
