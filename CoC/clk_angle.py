hh=21
mm=00
hh=hh%12
h=(hh*360)//12+(mm*360)//(12*60)
m=(mm*360)//60
angle=abs(h-m)
if angle>180:
    angle=360-angle
print(angle)