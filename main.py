import os
from shutil import copyfile

osuSongsFolderPath = "D:\Games\osu!\Songs"


def getAudioFilename(file_path):
    with open(file_path,'r', encoding='utf-8') as f:
        # je sais pas si ça sert à grand chose de l'opti
        for line in f.read().splitlines():
            data = line.split(': ')
            
            if data[0] == 'AudioFilename':
                return data[1]

    return ''

print(getAudioFilename('D:\Games\osu!\Songs/162368 BABYMETAL - Gimme Chocolate!! [no video]/BABYMETAL - Gimme Chocolate!! (Rad-) [Extra].osu'))

def check_extension(fileName, ext):
    return fileName.split('.')[-1:][0] == ext

def BMlistDifficulties(bm_folder_path):
    return [bm_folder_path+'/'+f for f in os.listdir(
        bm_folder_path) if check_extension(bm_folder_path+'/'+f, "osu")]

def getAllBeatmapsFolderPath(osuSongsDir):
    # pour chaque element du dossier osuSongDir on recupère osuSongsdir+/+element si l'element est bien un dossier
    return [osuSongsDir+'/'+e for e in os.listdir(osuSongsDir) if os.path.isdir(osuSongsDir+'/'+e)]

mapsPaths = getAllBeatmapsFolderPath(osuSongsFolderPath)

for mapPath in mapsPaths:
    
    mapName = mapPath.split('/')[-1]    # il y a toujours les chiffres devant et nous on veux les enlever
    mapName = ''.join(mapName.split()[1:])
    print('[=========={}===========]'.format(mapName))
    try:
        randDiff = BMlistDifficulties(mapPath)[-1]
        musicFileName = getAudioFilename(randDiff)
        musicFilePath = mapPath + '/' + musicFileName
        musicFileExt = musicFileName.split('.')[-1]
        
        copyfile(musicFilePath, './out/{}.{}'.format(mapName, musicFileExt))

    except:
        print('no diff file in this directory')
        

