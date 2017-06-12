# I Know What You Saw Last Minute - Encrypted HTTP Adaptive Video Streaming Title Classification
#Ran Dubin, Amit Dvir, Ofir Pele, Ofer Hadar
The video titles used in this study are popular YouTube videos from different categories such as news, sports, nature, video action trailers, and GoPro videos. In this study we decided to use the Chrome browser since it is the most popular browser on the market and its popularity is growing. We used the default auto mode of the YouTube player (the player decides which quality representation to download based on estimation of the client network conditions). We used the Selenium web automation tool with ChromeDriver for the crawler, so it will simulate a user video download in exactly the same
manner a normal user behaves. We used Ad-block Plus to eliminate advertisements only in the training datasets. This work assumes that video advertisement exists in the network in real scenarios. We do not assume that the advertisement can be distinguished from the viewed video in the encrypted network traffic level. We found that the video advertisement is distributed in different network flows and the video title download is distributed by several parallel network flows. Therefore, when testing unknown titles (titles that are not in the training titles) we do not filter out the video advertisement. Our algorithms classify each flow separately and we do not assume any prior knowledge about how many different flows exist per download.
 
For this, we collected a dataset that contains 10,000 YouTube streams (that were downloaded via a real-world Internet connection during a period of a month over different real-world network conditions) of 100 video titles (100 streams per video title). As it is not reasonable that a group of people will watch only the above “target” video titles, we added other 2,000 video titles (5,000 streams) which are not included in the “target” video titles set. These titles are used as the unknown titles in the evaluation.

In the following we give the pcaps files of all the video title streams (different download time and network link) as regular download, with delay and with packet lost.


Dataset link: http://www.cse.bgu.ac.il/title_fingerprinting/
Dataset Crawler Available At: https://github.com/randubin/YouTube_video_title_downloader


