from pywebcopy import save_webpage

url = 'https://www.pcmag.com/picks/the-best-computer-monitors'
download_folder = './download'    

kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}

save_webpage(url, download_folder, **kwargs)