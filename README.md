# fam-music-downoad
Download Music From FAM

A Python project to download entire albums, song by song from freeallmusic.

DISCLAIMER: This project has been built for educational purposes only, for understanding the working web API requests and headers. Please support the artists by getting your music from official sources.

## Bugs
* The downloaded tracks are verified once downloaded to make sure that the songs are completely downloaded. But sometimes, post verification downloads seem to fail, resulting in broken tracks. In such cases either re-run the script or download the song manually.


## To Do 
* Convert this into a web application.
* Create Artist Folder.
* Handle exceptions such as connection breaks.
* Remove requirement to enter total tracks
* Only enter artist and album name, no ID (if I am not too lazy)



## Usage

1. Install all the dependencies with

    ``` pip3 install -r requirements.txt ```

2. Run the script with 

    ``` python3 test.py ```

3. Enter the Album ID. The album ID is the the 12 digit number after the URL of the album at FAM. For example if the URL is 
``` https://freeallmusic.top/album/2830-2511-0877 ```
the Album ID would be 
``` 2830-2511-0877 ```.


4. Enter the number of songs present in the album.

5. The album will be downloaded and stored at /downloads/<album_name>.

Note: The number of songs entered is basically going to download tracks 1 through the number you entered. If you enter a smaller number than the total number of tracks, the album would be partially download till that point only. But any other forms of partial album downloads are not supported. You will need to edit the script and explicitly mention the tracks you want to download if you wish to do so.
