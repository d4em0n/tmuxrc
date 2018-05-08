# -*- coding: utf-8 -*-
import plyr
import os
import eyed3
import re

def fix_str(name):
    name = re.sub('\(.+\)', '', name)
    name = re.sub('\[.+\]', '', name)
    name = re.compile('audio|kbps', re.IGNORECASE).sub('', name)
    name = re.sub(' +', ' ', name)
    name = re.sub('ft\..+$|feat.+$','', name)
    return name.encode('ascii', 'ignore').strip()

def get_info(fn):
    mp3 = eyed3.load(fn)
    try:
        artist = mp3.tag.artist
        title = mp3.tag.title
        if len(title) == 0 or len(artist) == 0:
            raise Exception
    except:
        fn = fn[fn.rfind('/')+1:-4]
        fn = fix_str(fn)
        print fn
        artist = fn.split('-')[0][:-1]
        title  = fix_str(fn.split('-')[1][1:])
        
    if artist.find('-') != -1:
        artist = artist[:artist.find('-')-1]
    if artist.find(',') != -1:
        artist = artist[:artist.find(',')]
    return artist, fix_str(title)

def get_mp3():
    f = os.popen("cmus-remote -Q | grep -m 1 file | sed 's/file //g'").read().strip()
    return f

def get_lyric(artist, title):
    qry = plyr.Query(get_type="lyrics", artist=artist, title=title)
    items = qry.commit()
    if len(items) >= 1:
        return items[0].data

nama_file = get_mp3()
artist, judul = get_info(nama_file)
print get_lyric(artist, judul)
