#!/usr/env python

import os

def match(ori_former, ori_latter):
    '''
    use a most intuitive method to match this two string
    and just remove - or _

    a better edition would be using the dp algorithm.
    but I think this one would be enough  ^-^
    '''
    
    former = ori_former
    latter = ori_latter
    
    length = len(former)
    j = 0
    while j < length:
        if j < len(latter) and former[j] != latter[j]:
            if former[j] == '-' or former[j] == '_':
                former = former[:j] + former[j+1:]
                length -= 1
            elif latter[j] == '-' or latter[j] == '_':
                latter = latter[:j] + latter[j+1:]
        if j >= len(latter):
            break
        
        j += 1
    return former, latter

def modify_video_srt_file(video_srt_file):
    '''
    I don't know why I download the srt and mp4 files from Coursera,
    but the srt file cann't correspond to the mp4 file,
    because they have different prefix file name.
    Just some additional - or _.
    So I need to remove these additional digit
    '''

    #sort by the name, so I can run a linear time through these files
    video_srt_file.sort()
    
    
    for i in range(1, len(video_srt_file)):
        
        #In fact I should use a dynamic programming algorithm best 
        if video_srt_file[i][0:7] != video_srt_file[i-1][0:7]:
            continue
        
        #get the match file name
        former, latter = match(video_srt_file[i-1], video_srt_file[i])
        
        try :
            assert len(former) == len(latter) and former[:-3] == latter[:-3]
            assert former[-3:] != latter[-3:]

            if latter != video_srt_file[i]:
                print video_srt_file[i], latter
                os.rename(video_srt_file[i], latter)
                print latter
            if former != video_srt_file[i-1]:
                os.rename(video_srt_file[i-1], former)
                print former

        except AssertionError:
            continue

def return_file_list(path):
    '''get the srt or mp4 file list'''
    video_srt_file = []
    for entry in os.listdir(path):
        if os.path.isdir(entry):
            opendir(entry)
        elif entry.find('.srt') >= 0 or entry.find('.mp4') >= 0:
            video_srt_file.append(entry)
    return video_srt_file
    
def opendir(path):
    '''change to this dir, get the srt or mp4 file list, modify the name'''
    os.chdir(path)
    path = os.getcwd()
    print 'In the director ' + path + ' : '

    video_srt_file = return_file_list(path)    
            
    modify_video_srt_file(video_srt_file)   
                    
    os.chdir('..')    

if __name__ == '__main__':

    path = 'F:\\video'
    opendir(path)

    
    
