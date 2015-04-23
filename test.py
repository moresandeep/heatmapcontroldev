#!/usr/bin/python

import shapefile

sh = shapefile.Reader("barangays/Barangays")

records = sh.records()

for i in range(len(records)):
    record = records[i]
    for j in range(len(record)):
        print "%d: %s" % (j, record[j])
    print
