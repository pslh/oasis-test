#! /bin/bash
#
# Generate binary files from .csv files
# See https://github.com/OasisLMF/ktools/blob/master/docs/md/DataConversionComponents.md
#
# TODO consider turning this into a Makefile
#

INVESTIGATION_TIME=500
INTENSITY_BINS=50
DAMAGE_BINS=200

randtobin < random.csv > random.bin
damagebintobin < damage_bin_dict.csv > damage_bin_dict.bin
footprinttobin -i $INTENSITY_BINS < footprint.csv > footprint.bin
vulnerabilitytobin -d $DAMAGE_BINS < vulnerability.csv > vulnerability.bin
evetobin < events.csv > events.bin
itemtobin < items.csv > items.bin
# More Financial Module stuff here
occurrencetobin -P$INVESTIGATION_TIME < occurrence.csv > occurrence.bin
returnperiodtobin < returnperiods.csv > returnperiods.bin 
# periodstobin < periods.csv > periods.bin
