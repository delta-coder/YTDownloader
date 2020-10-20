#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:45:53 2020

@author: delta-coder
"""

from pytube import YouTube

def Downloader(link):
    url = YouTube(link)
    video = url.streams.first()
    video.download()

if __name__ == "__main__":
    Downloader("https://www.youtube.com/watch?v=tD6Zm_1ulYU")