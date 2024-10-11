newphase = "rainstorm"
        #   012345678
        #   123456789 -- college board version
# create a new variable called shortphrase
# and assign it a value nu s;comg
# the newphase variable by removing the first 3 letters and the last 3 letters
# the first 3 characters are "rai"
# the last 3 charcters are "orm"
# substring(string, start, end)

shortphrase = newphase[3:len(newphase)-3]

# college board version [4:len(newphase)-6]
print(shortphrase)
# explain lem(newphase) - 3 = 9-3 = 6
# why does it end with 6?
# because the last index is not incldued