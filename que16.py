color1=["red","orange","green", "blue", "white"] 
color2=["black", "yellow", "green", "blue"]

color1_color=[]
color2_color=[]

for color in color1:
    if color not in color2:
        color1_color.append(color)
print(color1_color)

for color in color2:
    if color not in color1:
        color2_color.append(color)
print(color2_color)