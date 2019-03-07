![Logo](https://image.prntscr.com/image/z8OYRQfSSbWCAJIMBjUJQQ.png)

# YTubeBOT - Youtube Bot
Simple bot that was development in python 3.7, that automatically watch youtube videos. It can be used to give more views in your channel helping in the spread and increase followers/subscribers because your videos begin to gain new positions in research mechanics.

## Concept proof

### Overview
The search time was seven days, but the script was run in only two days (48h).
![Overview](https://image.prntscr.com/image/oDbzCOL7Q2mQY_uq6ebmZw.png)

### Reach
![Reach](https://image.prntscr.com/image/AMrVxRlrRvq93grZDPcRnw.png)

## Script image
![Script](https://image.prntscr.com/image/bpElLpX_T0e3IBWvc5quHw.png)

## Description
- The script reads the "./config/playlist.json" file, multiplies the instance for each video by the configured value, and starts the chromedriver. - The mechanic has a system that identifies that the video is running, at the end it will be loaded again generating a view.

```json
[
     {
          "url": "https://www.youtube.com/...",
          "views": 50
     },
     {
          "url": "https://www.youtube.com/...",
          "views": 50
     }
]
```

- If the video modifies the URL for some reason the script identifies and corrects this problem.

- The script uses "selenium" to watch the videos, passing some settings that improve performance and do not interrupt the use of the computer.

- The script was developed using "asyncio" so you need python 3.7, so we can perform asynchronous functions.

- Inside script file "./app.py", you will configure how many async instances to launch, ie: instances = 1

- The instance multiplies the drivers to watch the videos, ie, will instantiate for each video the configured value.

## Running script

```python
pip install -r requirements.txt
python app.py
```

## Observations
- The script can be improved and modified, so feel free to use it any way you like.

- I will not be responsible for any problems related to youtube, because it is a project focused only for studies, keep this in mind.

- The script did not generate revenue in two days because the channel tested does not exceed 300 subscribers, it might help on this issue on channels with more than 1k of subscribers (maybe?).

- I hope it helps someone, and can help in studies aimed at webcrawler + selenium.

- Put "?autoplay=1" in end of video link and use absolute link, final link will be like: https://www.youtube.com/watch?v=xxxxxxxxxxx?autoplay=1




