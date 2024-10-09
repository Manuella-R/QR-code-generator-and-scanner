import qrcode
title= input('Enter Qrcode title:')
desc = input('Enter Qrcode description:')
img = qrcode.make(desc)
img.save(title+".png")