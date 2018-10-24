run("Duplicate...", "title=median");
run("Median...", "radius=31");
imageCalculator("Subtract create 32-bit", "local-background-test.tif","median");
selectWindow("Result of local-background-test.tif");