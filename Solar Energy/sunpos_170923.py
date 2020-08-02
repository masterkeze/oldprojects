import math

def leapyear(year):  
    if year % 400 == 0:   return True
    elif year % 100 == 0: return False  
    elif year % 4 == 0:   return True  
    else: return False
    
def calc_time(year, month, day, hour=12, minute=0, sec=0):
    month_days = [0,31,28,31,30,31,30,31,31,30,31,30]
    day = day + sum(month_days[:month])
    leapdays = leapyear(year) and day >= 60 and (not (month==2 and day==60))
    # The day in the year
    if leapdays: day += 1
    # Get (JD - 2400000)
    hour = hour + minute / 60.0 + sec / 3600.0 # hour plus fraction
    delta = year - 1949
    leap = delta // 4 # former leapyears
    jd = 32916.5 + delta * 365 + leap + day + hour / 24.0
    # Julian Date - 2451545.0 (noon, 1 January 2000)
    time = jd - 51545
    return time
    #输出为儒略日当前时刻与GMT 2000.1.1 12:00pm的差值

    
def sun_position(year, month, day, hour=12, minute=0, sec=0,
                lat=46.5, longitude=6.5):

    twopi = 2 * math.pi
    deg2rad = math.pi / 180

    time = calc_time(year, month, day, hour, minute, sec)

    # Ecliptic coordinates 黄道坐标
    # Mean longitude 平黄经（轨道角度为0时的经度）
    mnlong = 280.46 + 0.9856474 * time
    mnlong = mnlong % 360
    print("Mean longitude 平黄经",mnlong)

    # Mean anomaly 平近点角
    mnanom = 357.528 + 0.9856003 * time
    mnanom = mnanom % 360
    mnanom = mnanom * deg2rad
    print("Mean anomaly 平近点角",mnanom/deg2rad)

    # Ecliptic longitude and obliquity of ecliptic 
    eclong = mnlong + 1.915 * math.sin(mnanom) + 0.02 * math.sin(2 * mnanom)
    eclong = eclong % 360 #Ecliptic longitude 黄经
    oblqec = 23.439 - 0.0000004 * time # Obliquity of ecliptic 黄赤交角
    eclong = eclong * deg2rad
    oblqec = oblqec * deg2rad
    print("Ecliptic longitude 黄经", eclong/deg2rad)
    print("Obliquity of ecliptic 黄赤交角",oblqec/deg2rad)

    # Celestial coordinates 赤道坐标
    # Right ascension and declination 
    num = math.cos(oblqec) * math.sin(eclong)
    den = math.cos(eclong)
    ra = math.atan(num / den) # Right ascension 赤经
    if den < 0: ra += math.pi 
    if den >= 0 and num < 0: ra += twopi
    dec = math.asin(math.sin(oblqec) * math.sin(eclong)) # Declination 赤纬
    print("Right ascension 赤经",ra/deg2rad)
    print("Declination 赤纬", dec/deg2rad)

    # Local coordinates
    # Greenwich mean sidereal time 格林威治恒星时
    gmst = 6.697375 + 0.0657098242 * time + hour
    gmst = gmst % 24
    if gmst < 0: gmst += 24

    # Local mean sidereal time 本地恒星时
    lmst = gmst + longitude / 15.0
    lmst = lmst % 24
    if lmst < 0: lmst += 24
    lmst = lmst * 15 * deg2rad

    # Hour angle 时角
    ha = lmst - ra
    if ha < -math.pi: ha += twopi
    if ha > math.pi: ha -= twopi
    print("Hour angle 时角: ", ha/deg2rad)

    # Latitude to radians
    lat = lat * deg2rad

    # Solar zenith angle 天顶角
    zenithAngle = math.acos(math.sin(lat) * math.sin(dec) + math.cos(lat) * math.cos(dec) * math.cos(ha))
    # Solar azimuth 太阳方位角
    az = math.acos(((math.sin(lat) * math.cos(zenithAngle)) - math.sin(dec)) / (math.cos(lat) * math.sin(zenithAngle)))
    # Solar elevating angle 太阳高度角
    el = math.asin(math.sin(dec) * math.sin(lat) + math.cos(dec) * math.cos(lat) * math.cos(ha))
    
    el = el / deg2rad
    az = az / deg2rad
    lat = lat / deg2rad

    # Azimuth correction for Hour Angle
    if ha > 0:
        az += 180 #Before noon 午前
    else:
        az = 540 - az #After noon 午后
    az = az % 360
    return(az, el)

##year=int(input("Year: "))
##month=int(input("Month: "))
##day=int(input("Day: "))
##hour=int(input("Hour: "))
##minute=int(input("Minute: "))
##sec=int(input("Second: "))
##lat=int(input("Latitude: "))
##lgt=int(input("Longitude: "))
print("方位角，高度角")
print(sun_position(2017, 10, 11, 18, 2, 30, 22, 114))
#print(sun_position(year, month, day, hour, minute, sec, lat, lgt))
