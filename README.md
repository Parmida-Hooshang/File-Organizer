# File Organizer
#### By Parmida Hooshang

### Overview:
+ This simple tool helps you organize all the files in a folder and its subfolders by their last-modified dates. After running this program, there will be a folder for each year in which a file has been modified, and in each folder, the files will be seperated into at most five groups: photos, videos, docs, audios, others.

    |Folder|Formats|
    |---|---|
    |photos|jpg, jpeg, png|
    |videos|mp4, avi, 3gp, mpeg, mkv, wmv, mov, gif|
    |docs|doc, docx, pdf, txt, md, xls, xlsx, html, pptx|
    |audio|wav, mp3, aac, flac, m4a, wma, alac|
    |others|others|


### Prerequisites:
+ You need to have python installed on your device and added to your path environment.

### Guidelines:
+ Download the python file "organizeFiles.py"
+ Navigate to where the file is located and open Terminal/cmd.
+ Paste the command below:
    + Linux/Mac: `$ python3 organizeFiles.py src_folder_path dst_folder_path`
    + Windows: `> python organizeFiles.py src_folder_path dst_folder_path`
+ `src_folder_path` is where the original files and folders are locatetd and `dst_folder_path` is where you want the organized folders located.
+ An example on windows: `> python organizeFiles.py F:\testing\bigFolder F:\destination`

### Example
+ Imagine the hierarchy below:

    src_folder<br>
    ├── xxx.jpg<br>
    ├── some_photos<br>
    │----├── yyy.3gp<br>
    │----├── zzz.jpg<br>
    │----├── uuu.JPG<br>
    │----├── ttt.jpg<br>
    │----└── note.txt<br>
    ├── A<br>
    │----└── B<br>
    │----------├── music.mp3<br>
    │----------└── book.pdf<br>
    └── vid1<br>
    ------├── images<br>
    ------│----└── image.JPG<br>
    ------└── VID.mp4<br>

+ The destination is described below:

    dst_folder<br>
    ├── 2024<br>
    │----├── photos<br>
    │----│----└── uuu.JPG<br>
    │----└── audio<br>
    │----------└── music.mp3<br>
    ├── 2023<br>
    │----├── photos<br>
    │----│----└── xxx.jpg<br>
    │----├── videos<br>
    │----│----└── VID.mp4<br>
    │----└── docs<br>
    │----------└── book.pdf<br>
    └── 2018<br>
    ----├── photos<br>
    ----│----├── image.JPG<br>
    ----│----├── zzz.jpg<br>
    ----│----└── ttt.jpg <br>
    ----└── videos<br>
    ----------└── yyy.3gp<br>
