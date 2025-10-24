from queue import Empty

obj = {
    "one":1,
    "two":2,
    "three":3
}

# it adds new item(s)
obj.update({
    "four":4,
    "five":5
})

# updates value if key exist
obj.update({
    "four":6,
    "five":7
})

bin = b''

bin += b'45'

print(bin)

sayi = 44
# print(int(bin, 16))
# print(hex(sayi))
# print(int(hex(sayi), 16))

deger = None

if not deger:
    girinti = 5#this value can be used inside if __name__ == "__main__" block

co2_data = [1, 2]

o2_data = [1, 2, 0, 5]

dict1 = {"gas": None }
dict2 = { }
sozluk = { }
if __name__ == "__main__":
    
    veri_kumesi = {'o2': [{'ts': 1754369587283, 'value': 4.8}, {'ts': 1754368558673, 'value': 4.77}, {'ts': 1754367529794, 'value': 4.8},
                      {'ts': 1754366500972, 'value': 4.77}, {'ts': 1754365472239, 'value': 4.77}, {'ts': 1754364443487, 'value': 4.8},
                        {'ts': 1754363414683, 'value': 4.77}, {'ts': 1754362385959, 'value': 4.77}, {'ts': 1754361357315, 'value': 4.77},
                          {'ts': 1754360328430, 'value': 4.77}, {'ts': 1754359299562, 'value': 4.77}, {'ts': 1754358271037, 'value': 4.77},
                            {'ts': 1754357242081, 'value': 4.77}, {'ts': 1754356213179, 'value': 4.77}]}
    
    sozluk[872] = veri_kumesi
    
    #deletes if key is exist, rasises KeyError if key is not exist
    del sozluk[872]
    
    sozluk[872] = veri_kumesi

    #pop() returns deleted value. To avoid any KeyError, use pop(key, None).
    d = sozluk.pop(872, None)#deleted value stored in 'd'
    d = sozluk.pop(871, None)
    #if deleted value is not necassary, sozluk.pop(872, None) can be used 

 

