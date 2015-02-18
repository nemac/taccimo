var areas = new Array();
function area(areaID,areaName,areaXMin,areaYMin,areaXMax,areaYMax)
{
    this.areaID=areaID;
    this.areaName=areaName;
    this.areaXMin=areaXMin;
    this.areaYMin=areaYMin;
    this.areaXMax=areaXMax;
    this.areaYMax=areaYMax;
}

areas.push(new area("1", "United States", -15000000, 2000000, -6000000, 7000000));
areas.push(new area("2", "Buncombe County, NC", -9226268, 4220851, -9147183, 4275404));
areas.push(new area("3", "Haywood County, NC", -9268349, 4203480, -9210991, 4272032));
areas.push(new area("4", "Madison County, NC", -9235357, 4255811, -9173357, 4308116));
areas.push(new area("5", "Henderson County, NC", -9210991, 4184231, -9156912, 4231393));
areas.push(new area("6", "Transylvania County, NC", -9245301, 4167183, -9191637, 4220851));
areas.push(new area("7", "Fairview", -9197926, 4222031, -9145146, 4246873));
areas.push(new area("8", "Waynesville", -9263847, 4216924, -9211067, 4241766));
areas.push(new area("9", "Black Mountain", -9188448, 4235732, -9135668, 4260574));
areas.push(new area("10", "Swannanoa", -9197926, 4233152, -9145146, 4257994));
areas.push(new area("11", "Hendersonville", -9204423, 4194303, -9151643, 4219145));
areas.push(new area("12", "Brevard", -9234856, 4182686, -9182076, 4207528));
areas.push(new area("13", "Mills River", -9215938, 4203133, -9163158, 4227975));
areas.push(new area("14", "Asheville", -9216538, 4231222, -9163759, 4256064));
