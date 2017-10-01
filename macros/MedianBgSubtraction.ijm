imageTitle = getTitle();
rename("orig.tif"); 
run("Duplicate...", "title=orig-median.tif");
run("Median...", "radius=17");
imageCalculator("Subtract create", "orig.tif","orig-median.tif");
rename( "bgcorr-"+imageTitle );
