# Daylio to Daily You Converter
This tool allows you to convert Daylio entries and images into a format that can be imported into Daily You.

## Instructions
### Export from Daylio:
1. In Daylio, go to `More > Edit Moods`
2. Change the mood names to be their default values if they aren't already: (rad, good, meh, bad, awful)

NOTE: Daily You currently only supports 5 moods, if you added more moods to Daylio any days that use them will import as entries with no mood.

4. Exit the `Edit Moods` page and go to `Export Entries`
5. Select `CSV (table)` and choose a location to save the Daylio CSV
6. Select `Export Photos` ahd choose a location to save the entry photos as a .zip file
7. Go to where you saved the photos .zip file and extract the zip
### Convert to Daily You
8. Clone this repo and make sure any dependencies of `daylio-to-daily-you.py` are installed
9. Open your terminal or command line and navigate into the repo
10. Run `daylio-to-daily-you.py` using ```>python3 daylio-to-daily-you.py "path_to_daylio_csv" --images "path_to_folder_with_exported_daylio_images"```

NOTE: If you do not want to import images you can omit `--images`

11. Assuming no errors, the script will generate `daily_you_log.json` as well as any imported images within the repo's `output` folder.

NOTE: Currently Daily You only supports a single image per day. If more than one photo exists for a Daylio entry the first will be selected.

### Import to Daily You
12. In Daily you, select the gear in the top right.
13. Select `Import Logs...`
14. Select `Daily You`
15. Select the `daily_you_log.json` generated by `daylio-to-daily-you.py`
16. Select `Import Images...`
17. Select the photos generated by `daylio-to-daily-you.py`

## Limitations
When you export photos from Daylio they are named based on the date they were added to the entry NOT the date of the entry. This means that if you added a photo a day late that image may end up associated with the next days entry.