# Design a system that Loops Weekly, based on time of week, day, and hour.
# 1. Design a system that removes Rootzone water to main tank.
# 2. The Water that is removed from the rootzone is then mixed with Fresh water to a fill line of 11 Gallons.
# 3. Fresh Water will be pulled from the main line by opening the sink line valve,
#    relying on the water pressure to push water into the tank.
# 4. Once a fill line is reached by timing, it will be mixed with fresh nutrients.
# 5. Start by getting a sample reading of the EC value, logging it to a Spreadsheet on Google using Gspread. "Generally (400E/C)"
# 6. Using that value you can start adding nutrients by using ><and = to.
# 7. Start with Part A, by dosing in .3 Millisecond Intervals, with a 1 minute delay between doses. Once the solution reacheace 650 EC, Log the Value then procced to Part B solution.
# 8. Using Part B, dosing in .3 Millisecond Intervals, with a 1 minute delay between doses. Once the solution reacheace 950 EC, Log the Value then procced to CalMag.
# 9. Using CalMag, dosing in .3 Millisecond Intervals, with a 1 minute delay between doses. Once the solution reacheace 1000 EC, Log the Value then procced to getting a PH reading.
# 10. Proceed the program to PH Balance by getting a sample reading of PH, and Logging it to spreadsheet.
# 11. Then using the Sample PH value you can determine how much PH Down or PH Up to add, PH = (5.8).
# 12. After the PH has been Balanced, Log the PH Value, then let the Mixer pump Mix the nutrients for 10 Minutes Delay.
# 13. Send Mixed nutrients to each bucket based on a second timing value.
# 14. After all buckets have been filled evenly, turn off mixing, and feeding pumps.
# 15. Loop iterates and waits based on time in seconds, using a counter to determine its position.
# SET PRINT FUNCTIONS TO ALL OUTPUTS
