import numpy as np
import serial
import re
from math import radians, cos, sin, asin, sqrt 

def distance(lat1, lat2, lon1, lon2,lat_sgn, lon_sgn): 
    
    
    lat1=lat1.split(".")
    latmin=int(lat1[0])%100
    latmin=str(latmin)+'.'+lat1[1]
    latmin=float(latmin)
    latdeg=(float(lat1[0])-int(lat1[0])%100)/100
    lat1=latdeg+latmin/60

    lat2=lat2.split(".")
    latmin2=int(lat2[0])%100
    latmin2=str(latmin2)+'.'+lat2[1]
    latmin2=float(latmin2)
    latdeg2=(float(lat2[0])-int(lat2[0])%100)/100
    lat2=latdeg2+latmin2/60

    lon1=lon1.split(".")
    lonmin=int(lon1[0])%100
    lonmin=str(lonmin)+'.'+lon1[1]
    lonmin=float(lonmin)
    londeg=(float(lon1[0])-int(lon1[0])%100)/100
    lon1=londeg+lonmin/60

    lon2=lon2.split(".")
    lonmin2=int(lon2[0])%100
    lonmin2=str(lonmin2)+'.'+lon2[1]
    lonmin2=float(lonmin2)
    londeg2=(float(lon2[0])-int(lon2[0])%100)/100
    lon2=londeg2+lonmin2/60
    if lat_sgn=='S':
        lat1=lat1*-1
        lat2=lat2*-1
    if lon_sgn=='W':
        lon1=lon1*-1
        lon2=lon2*-1
    
    # The math module contains a function named 
    # radians which converts from degrees to radians. 
    lon1 = radians(lon1) 
    lon2 = radians(lon2) 
    lat1 = radians(lat1) 
    lat2 = radians(lat2) 
       
    # Haversine formula  
    dlon = lon2 - lon1  
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  
    c = 2 * asin(sqrt(a))  
     
    # Radius of earth in kilometers. Use 3956 for miles 
    r = 6371
       
    # calculate the result #REVISAR RESULTADO.
    return(c * r)


bandera =0

#GPS='$GPRMC,203544.000,A,0438.9198,N,07404.3962,W,0.00,247.85,150517,,,A*62'
puntajes=[100,99,96]
pred_env=[3, 3, 5]
pred_env= np.asarray(pred_env)


gps_ser=serial.Serial('com19', baudrate=115200)
while True:
    GPS_data= gps_ser.readline()
    GPS_data= GPS_data.decode('utf-8')
    GPS_data_sel= GPS_data.split(",") 
    if GPS_data_sel[0]=='$GPRMC':
        if bandera==0:
            if GPS_data_sel[2]=='A':
                GPS_data_p0={
                'Time_Stamp':GPS_data_sel[1],
                'Latitude':GPS_data_sel[3],
                'Lat_sgn': GPS_data_sel[4],
                'Longitude':GPS_data_sel[5],
                'Lon_sgn': GPS_data_sel[6]
                }  
                print(GPS_data_p0,'This is going to be the (0,0) point')
            bandera=1
        for i in range(pred_env.shape[0]):
            if pred_env[i]== 3 or pred_env[i]== 4 or pred_env[i] == 5:      
                if GPS_data_sel[2]=='A':
                    GPS_data={
                   'Time_Stamp':GPS_data_sel[1],
                   'Latitude':GPS_data_sel[3],
                   'Lat_sgn': GPS_data_sel[4],
                   'Longitude':GPS_data_sel[5],
                   'Lon_sgn': GPS_data_sel[6]
                    }
                    #print(GPS_data_p0['Latitude'], GPS_data['Latitude'], GPS_data_p0['Longitude'], GPS_data['Longitude'],GPS_data_p0['Lat_sgn'],GPS_data_p0['Lon_sgn'])
                    dist=distance(GPS_data_p0['Latitude'], GPS_data['Latitude'], GPS_data_p0['Longitude'], GPS_data['Longitude'],GPS_data_p0['Lat_sgn'],GPS_data_p0['Lon_sgn']) 
                    print(dist)



