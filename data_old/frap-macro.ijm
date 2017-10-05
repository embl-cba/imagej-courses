nt = 70;

time = newArray(nt);
bleach = newArray(nt);
bg = newArray(nt);
ctrl = newArray(nt);
ref = newArray(nt);


for (i=0; i<nt; i++) { 
    time[i] = i; 
    bleach[i] = getResult("Mean(bleach)",i); 
    bg[i] = getResult("Mean(bg)",i);
    ctrl[i] = getResult("Mean(ctrl)",i);
    ref[i] = getResult("Mean(ref)",i);
    } 

norm_bleach = bleach[0]-bg[0];
norm_ctrl = ctrl[0]-bg[0];

for (i=0; i<nt; i++) { 
    bleach[i] = (bleach[i]-bg[i])/(ref[i]-bg[i]); 
    ctrl[i] = (ctrl[i]-bg[i])/norm_ctrl;
    } 
    
Plot.create("Line Plot Test", "Frame Number", "Normalised signal", time, bleach);
Plot.setLimits(0,nt,0,1.2);
Plot.setColor("red"); 
Plot.add("Line", ctrl); 
Plot.setColor("green"); 
