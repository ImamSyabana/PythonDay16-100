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