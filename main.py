import math

def isSameSign(a, b):
    if a < 0 and b < 0 or a > 0 and b > 0:
        return True
    return False

# earth location
lat = float(input("Enter your latitude in degrees: "))
long = float(input("Enter your longitude in degrees: "))
# celestial object
dec = float(input("Enter celestial object declination in degrees: "))
ra = float(input("Enter celestial object right ascension: "))

# compute local hour angle http://star-www.st-and.ac.uk/~fv/webnotes/chapter6.htm
lst = 0 # TODO
lha_hours = lst - ra
lha = lha_hours * 15 # https://www.traditionaloven.com/tutorials/angle/convert-astronomical-hour-angle-to-degree-unit.html

# rough estimation if it it possible to see the celestial object at all
# https://flatearth.ws/star-visibility
if dec + lat > 90:
    print("celestial object is always visible in the north")
elif dec + lat < -90:
    print("celestial object is always visible in the south")
elif dec - lat > 90 or dec - lat < -90:
    print("is the star never visible from your location" )
else:
    print("the star is sometimes visible from your location")

# calculate the azimuth of the celestial object - ABC-method https://www.youtube.com/watch?v=8MaRXY-RONE
a = math.tan(math.radians(lat)) / math.tan(math.radians(lha))
if isSameSign(a, lat) and not (lha > 90 and lha < 270):
    a *= -1
b = math.tan(math.radians(dec)) / math.sin(math.radians(lha))
if not isSameSign(b, dec):
    b *= -1
c = a + b
if not isSameSign(a, b):
    # substract smaller from bigger one, set label that of bigger one
    if a > b:
        c = a - b
        if not isSameSign(c, a): c *= -1
    else:
        c = b - a
        if not isSameSign(c, b): c *= -1
azimuth = math.degrees(math.atan(1/c/math.cos(math.radians(lat))))
ew = "east/west"
if lha > 180: ew = "east"
if lha < 180: ew = "west"
ns = "north/south"
if c > 0: ns = "north"
if c < 0: ns = "south"
print("azimuth: " + ns + " " + str(azimuth) + " " + ew)

# calculate the altitude of a celestial object https://www.youtube.com/watch?v=cCeLavlYeNk&t=2s
hc = math.cos(math.radians(lha)) * math.cos(math.radians(lat)) * math.cos(math.radians(dec))
if isSameSign(lat, dec):
    hc += math.sin(math.radians(lat)) * math.sin(math.radians(dec))
else:
    hc -= math.sin(math.radians(lat)) * math.sin(math.radians(dec))
hc = math.degrees(math.asin(hc))
print("altitude: " + str(hc))
