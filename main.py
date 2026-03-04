import qrcode

url = input("Enter Your URL: ")
filename = input("FileName You want to save it as: ")
if not(filename.endswith(".png")):
  filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)
