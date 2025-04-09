import colorgram

# extract 12 warna dari gambar yang dipilih
# warna yang diekstrak berdasarkan warna yang paling mendominasi

color= colorgram.extract(r'D:\_Coolyeah\Udemy\100Days Python\Day 18\image.jpg', 12)

print(color[0].rgb.r)

colorTuppleCollection = []

def rgbExtractor(r, g, b):
    rgbTupple = (r, g, b)
    return rgbTupple

for x in range(len(color)):
    rgbTemp = []
    for y in range(3):
        
        rgbTemp.append(color[x].rgb[y])
        
    colorTuppleCollection.append(rgbExtractor(rgbTemp[0], rgbTemp[1], rgbTemp[2]))
    
print(colorTuppleCollection)

colorList = [(199, 176, 117), (124, 37, 24), (208, 221, 212), (166, 106, 57), (6, 57, 83), (185, 158, 54), (220, 224, 228), (108, 68, 84), (113, 161, 175), (40, 37, 35)]