file = input("File name: ")
file = file.replace(".", " ")
fileL = file.split()
n = 0
for f in fileL:
    n+=1
    if n == len(fileL) - 1:
        file = fileL[n].lower()
match file.lower():
    case "gif":
        print(f"image/{file}")
    case "jpg":
        print(f"image/jpeg")
    case "jpeg":
        print(f"image/jpeg")
    case "png":
        print(f"image/{file}")
    case "pdf":
        print(f"application/{file}")
    case "txt":
        print(f"text/{fileL[0]}")
    case "zip":
        print(f"application/{file}")
    case _:
        print("application/octet-stream")
