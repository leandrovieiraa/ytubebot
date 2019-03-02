import json, asyncio
import numpy as np
from utils.utils import Utils
from controller import Controller

class Watcher():
    def __init__(self, instances):
        # log init watcher class
        Utils.draw_log(status=True, datetime=Utils.get_current_datetime(), message='Initializing watcher with async instances count: {}'.format(instances))
        
        # call load playlist function
        playlist = self.load_playlist()

        # create new list with instances count
        videos_playlist = list(np.repeat(playlist, instances))

        # watch all videos from playlist
        if len(videos_playlist) > 0:
            self.watch_video(videos_playlist)
        # no videos found
        else:
            Utils.draw_log(status=False, datetime=Utils.get_current_datetime(), message='No videos to play.')        

    def load_playlist(self):   
        # playlist data   
        playlist = {}
        
        # try load playlist data
        try:
            # load playlist data from json file
            with open('./config/playlist.json') as playlist_data:
                playlist = json.load(playlist_data)

            # log load success
            Utils.draw_log(status=True, datetime=Utils.get_current_datetime(), message='Playlist data loaded successfully.')
            
            # return
            return playlist

        # log error on load playlist data
        except Exception as e:
            Utils.draw_log(status=False, datetime=Utils.get_current_datetime(), message='Playlist data loaded with errors: {}'.format(e))
    
    def watch_video(self, videos_playlist):
        # instance loop object for asyncio
        loop = asyncio.get_event_loop()
        
        # tasks
        tasks = []

        # create tasks
        for video_data in videos_playlist:       
            tasks.append(asyncio.ensure_future(Controller.start_controller(video_data)))
        
        # run tasks
        loop.run_until_complete(asyncio.wait(tasks))  
        loop.close()
