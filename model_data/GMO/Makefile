#
# Generate binary files from .csv files
# See https://github.com/OasisLMF/ktools/blob/master/docs/md/DataConversionComponents.md
#

#
# Model specific parameters
#
#INVESTIGATION_TIME=500
INVESTIGATION_TIME=5
# TODO extract from intensity_bin_dict.csv (sort|tail -n | awk...)
INTENSITY_BINS=980
DAMAGE_BINS=500

#
# Binary file we want to generate
#
BIN_FILES= \
random.bin \
damage_bin_dict.bin \
footprint.bin \
footprint.idx \
vulnerability.bin \
events.bin \
occurrence.bin \
returnperiods.bin 

#items.bin \

#
# Standard targets
#

all: $(BIN_FILES)

clean:
	rm -f $(BIN_FILES)

#
# OASIS Specifc targets
#

random.bin: random.csv
	randtobin < random.csv > random.bin

damage_bin_dict.bin: damage_bin_dict.csv
	damagebintobin < damage_bin_dict.csv > damage_bin_dict.bin

footprint.idx: footprint.bin
	footprinttobin -i $(INTENSITY_BINS) < footprint.csv > footprint.bin

footprint.bin: footprint.csv
	footprinttobin -i $(INTENSITY_BINS) < footprint.csv > footprint.bin

vulnerability.bin: vulnerability.csv
	vulnerabilitytobin -d $(DAMAGE_BINS) \
		< vulnerability.csv > vulnerability.bin

events.bin: events.csv
	evetobin < events.csv > events.bin

items.bin: items.csv
	itemtobin < items.csv > items.bin

occurrence.bin: occurrence.csv
	occurrencetobin -P$(INVESTIGATION_TIME) < occurrence.csv > occurrence.bin

returnperiods.bin: returnperiods.csv
	returnperiodtobin < returnperiods.csv > returnperiods.bin 

periods.bin: periods.csv
	periodstobin < periods.csv > periods.bin
