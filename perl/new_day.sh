#!/bin/bash
# new_day.sh
# Quick Function to create a new day.
#

cp -rf DayX Day"$@" &&
cd Day"$@" &&
sed -e "s/DayX/Day$@/g" -e "s/Day X/Day $@/g" DayX.pl > Day"$@".pl &&
rm DayX.pl
