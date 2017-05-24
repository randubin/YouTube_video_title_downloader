# YouTube_video_title_downloader
This is a windows  python+ selenium +chromedriver project.
The purpose of the project is to download YouTbe encrypted network traffic of Dynamice Adaptive Streaming over HTTP (DASH) videos.
With the help of this downloader we can create a training and testing set in order to classify YouTube video titles.
Please note that the code assume that Selenium and chrome driver are already installed (pease specify the location in the global section). The default profile has ad-blocking abilities (if you don't want to catch advertisment as well).

The crawler maintains the regular user download behavior and was designed to work with YouTube Flash or HTML5 versions in “Auto” quality representation mode. 
The dataset contains 10 subsets:
1.	Main dataset: 100 titles with 100 different downloads per title. Each title is divided in to Train (90%) and Test (10%).
2.	Network Added Delay 100 [ms]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional delay.
3.	Network Added Delay 300 [ms]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional delay.
4.	Network Added Delay 600 [ms]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional delay.
5.	Network Added Delay 900 [ms]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional delay.
6.	Network Added Packet Loss 1 [%]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional packet loss.
7.	Network Added Packet Loss 3 [%]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional packet loss.
8.	Network Added Packet Loss 6 [%]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional packet loss.
9.	Network Added Packet Loss 9 [%]: 10 titles from the dataset (1)  list each has  10 different copies that we added them a fixed additional packet loss.
10.	Titles which are not found in the  Main Dataset list (Train set): 30 video titles each has a single copy download. This dataset does not contain the same titles as the other sets.
Dataset link: http://www.cse.bgu.ac.il/title_fingerprinting/
Dataset Crawler Available At: https://github.com/randubin/YouTube_video_title_downloader
Please note that the duration and the link for each title are ready to download in the crawler code.
For any questions please contact:
dubinr@bgu.post.ac.il

