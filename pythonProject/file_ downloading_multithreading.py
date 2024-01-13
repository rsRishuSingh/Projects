# Date 13th October 2023

import requests,threading,time
import os,shutil
import pyttsx3,speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor as tpe




r=sr.Recognizer()                   # initialiser of recognizer
engine= pyttsx3.init()              # initialiser of engine
number=0

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

def ImageDownloader(obj,n):
    
    if(not os.path.exists("DeleteME")):         #folder is created if it does not exist
        os.mkdir("DeleteME")
  
    print(f"we are starting download {n}")
    open(f'DeleteME/image{n}.jpg','wb').write(obj.content)  # writing the file
    #str1=f'image{n} downloaded'
    #engine.say(str1)
    #engine.runAndWait()  # they will become bottle's neck in multiprocessing
    print(f"Downloading {n} Ended")


def Image_meta(num):
   
    engine.say(str1:="image download started")
    engine.runAndWait()             #stopping until speech synthesis ends
    
    list_of_started_tasks=list()  # to be used below
    
    t1=time.perf_counter()

    for i,j in enumerate(range(num),start=1):

        image_obj=requests.get("https://loremflickr.com/3200/2400")         # getting image by request
        
        task=threading.Thread(target=ImageDownloader,args=[image_obj,i])
        task.start()
        list_of_started_tasks.append(task)
    
    i=0
    for _ in list_of_started_tasks:

        list_of_started_tasks[i].join()
        i+=1
    
    print('Time Taken to Download Image Files',time.perf_counter()-t1)
    
    str1="image download ended"
    engine.say(str1)
    engine.runAndWait()

def VideoDownloader(url,n):
    
    text=requests.get(url)
    if(not os.path.exists("DeleteME")):
        os.mkdir("DeleteME")
  
    print(f"we are starting download {n+1}")
    
    file_Object=open(f'DeleteME/Video{n+1}.mp4','wb')
    file_Object.write(text.content)
    file_Object.close()

# PLEASE : check the validity of links before running

def Video_meta():

    list_of_video=['https://download-video.akamaized.net/v2-1/playback/29950fd4-8bbf-4d9e-ba91-1e967a5d92b2/e38749dc?__token__=st=1697219583~exp=1697233983~acl=%2Fv2-1%2Fplayback%2F29950fd4-8bbf-4d9e-ba91-1e967a5d92b2%2Fe38749dc%2A~hmac=635d10cfd220f20e8e62112e2a9bedcd57feb5c5f23d354cf95666806971a6b9&r=dXMtd2VzdDE%3D','https://vod-progressive.akamaized.net/exp=1697234039~acl=%2Fvimeo-transcode-storage-prod-us-east1-h264-1440p%2F01%2F4232%2F8%2F221163277%2F770983850.mp4~hmac=74d3693feed29942361ffef6515cf1794026b6c1cd5a59d942e0ccfc836c97d3/vimeo-transcode-storage-prod-us-east1-h264-1440p/01/4232/8/221163277/770983850.mp4?filename=file.mp4','https://vod-progressive.akamaized.net/exp=1697234082~acl=%2Fvimeo-transcode-storage-prod-us-central1-h264-1440p%2F01%2F2607%2F28%2F713036088%2F3305427178.mp4~hmac=2e84cbe6c4307358942650939b3bb484406bddbb267e73213b4d951abe580474/vimeo-transcode-storage-prod-us-central1-h264-1440p/01/2607/28/713036088/3305427178.mp4?filename=file.mp4','https://vod-progressive.akamaized.net/exp=1697234142~acl=%2Fvimeo-transcode-storage-prod-us-central1-h264-1440p%2F01%2F598%2F29%2F727993861%2F3375378558.mp4~hmac=03818fff26bf2e16e42592ffe6249d930200781d462625518cfa4d82c71f1cdb/vimeo-transcode-storage-prod-us-central1-h264-1440p/01/598/29/727993861/3375378558.mp4?filename=file.mp4','https://vod-progressive.akamaized.net/exp=1697234191~acl=%2Fvimeo-prod-skyfire-std-us%2F01%2F3075%2F20%2F515379416%2F2390463005.mp4~hmac=36c496041e26f0bcad20a983d3e83bda47c87c8667447c8caf74a64ff8e32c4d/vimeo-prod-skyfire-std-us/01/3075/20/515379416/2390463005.mp4?filename=file.mp4']

    str1=" Video download started"
    engine.say(str1)
    engine.runAndWait()
    t1=time.perf_counter()
   
    with tpe() as executor:
           executor.map(VideoDownloader,list_of_video,range(len(list_of_video)))
    
    print('Time Taken to Download Video Files',time.perf_counter()-t1)
    
    engine.say(str1:="video download end")
    engine.runAndWait()
 



def PdfDownloader(url,n):
    
    text=requests.get(url)
    
    if(not os.path.exists("DeleteME")):
        os.mkdir("DeleteME")
  
    print(f"we are starting download {n+1}")
    
    with open(f'DeleteME/PDF{n+1}.pdf','wb') as file_Object:
        file_Object.write(text.content)


def decorator_For_pdf(PDF_meta):
    
    def decofunc():
        str1="PDF download started"
        engine.say(str1)
        engine.runAndWait()

        PDF_meta()

        engine.say(str1:="PDF download end")
        engine.runAndWait()
    
    return decofunc


@decorator_For_pdf
def PDF_meta():

    list_of_pdf=['http://dtu.ac.in/Web/notice/2023/oct/file1042.pdf','http://dtu.ac.in/Web/notice/2023/sep/file0928.pdf','http://dtu.ac.in/Web/notice/2023/sep/file0920.pdf','http://dtu.ac.in/Web/notice/2023/sep/file09110.pdf']

    t1=time.perf_counter()

    with tpe() as executor:
           executor.map(PdfDownloader,list_of_pdf,range(len(list_of_pdf)))
    
    print('Time Taken to Download PDF Files',time.perf_counter()-t1)
    
    
def parallelsorting(file):

    if file.endswith('.jpg'):
        shutil.move(f'DeleteMe/{file}',f'Sycamore/Image folder/{file}')
   
    if file.endswith('.mp4'):
        shutil.move(f'DeleteMe/{file}',f'Sycamore/Video folder/{file}')
    
    if file.endswith('.pdf'):
        shutil.move(f'DeleteMe/{file}',f'Sycamore/PDF folder')/{file}

def file_sorting():
   
    List_of_files_in_DeleteMe=os.listdir('DeleteMe')

    if(not os.path.exists("Sycamore")):
        os.mkdir("Sycamore")
    
    tup=('Image folder','Video folder','PDF folder')
    
    for i in tup:
        
        if(not os.path.exists(f"Sycamore/{i}")):
            os.mkdir(f"Sycamore/{i}")
    
    engine.say(" file Sorting started")
    engine.runAndWait()

    t1=time.perf_counter()
    print("Time taken in file sorting : ",time.perf_counter()-t1)
    with tpe() as executor:
        executor.map(parallelsorting,List_of_files_in_DeleteMe)
    print("Time taken in file sorting : ",time.perf_counter()-t1)
    
    engine.say(str1:=" file Sorting ended")
    engine.runAndWait()


while number<1:
    number=1

    name=input("Enter Your Name : ")
    engine.say(f'{name} say:Start the execution')
    engine.runAndWait()
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.1)
            print("Wait")
            time.sleep(2)
            print("Speak : \n\n\U0001F914\n\n")
            audio2=r.listen(source2)
            text=r.recognize_google(audio2)
        
            text.lower()
            print('\tDid you say',text)
            text.strip('')
           
    except:

        print("Some Error has occured Please provide input in Text\n")
        text=input("\nType :Start the execution")
        text.lower()

    finally:
        if __name__=='__main__':
            
            if text=='start the execution':
            

                engine.say('Execution started')
                engine.runAndWait()

                Image_meta(10)  
                #Video_meta()
                PDF_meta()
                file_sorting()

                
                engine.say('work ended')
                engine.runAndWait()

                time.sleep(60)
                shutil.rmtree('DeleteMe')

                engine.say('DeleteMe folder deleted')
                engine.runAndWait()












