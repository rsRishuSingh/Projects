# Required imports for the script functionality
import requests, threading, time
import os, shutil
import pyttsx3, speech_recognition as sr
from concurrent.futures import ThreadPoolExecutor as tpe

# Initializing the speech recognizer and text-to-speech engine
r = sr.Recognizer()  # Recognizer object for speech recognition
engine = pyttsx3.init()  # Text-to-speech engine initialization
number = 0

""" Voice Configuration """
# Setting up the voice properties for text-to-speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Using the female voice

""" Rate Configuration """
rate = engine.getProperty('rate')  # Retrieving current speaking rate
print(rate)  # Displaying current rate
engine.setProperty('rate', 150)  # Adjusting to a slower speaking rate

# Function to download and save an image
def ImageDownloader(obj, n):
    if not os.path.exists("DeleteME"):  # Check if "DeleteME" folder exists
        os.mkdir("DeleteME")  # Create folder if not exists

    print(f"We are starting download {n}")
    open(f'DeleteME/image{n}.jpg', 'wb').write(obj.content)  # Save the image
    print(f"Downloading {n} Ended")

# Function to manage image downloading
def Image_meta(num):
    engine.say(str1 := "Image download started")
    engine.runAndWait()  # Wait for speech synthesis to complete

    list_of_started_tasks = []  # List to keep track of threads

    t1 = time.perf_counter()  # Start timer
    for i, j in enumerate(range(num), start=1):
        image_obj = requests.get("https://loremflickr.com/3200/2400")  # Get image
        task = threading.Thread(target=ImageDownloader, args=[image_obj, i])  # Create thread
        task.start()  # Start thread
        list_of_started_tasks.append(task)  # Add thread to list

    # Wait for all threads to complete
    for task in list_of_started_tasks:
        task.join()

    print('Time Taken to Download Image Files', time.perf_counter() - t1)
    engine.say("Image download ended")
    engine.runAndWait()

# Function to download a video
def VideoDownloader(url, n):
    text = requests.get(url)
    if not os.path.exists("DeleteME"):
        os.mkdir("DeleteME")  # Create folder if not exists

    print(f"We are starting download {n+1}")
    with open(f'DeleteME/Video{n+1}.mp4', 'wb') as file_Object:
        file_Object.write(text.content)  # Save video content

# Function to manage video downloads
def Video_meta():
    # List of video URLs
    list_of_video = [
        'https://download-video.akamaized.net/...1.mp4',
        'https://vod-progressive.akamaized.net/...2.mp4',
        'https://vod-progressive.akamaized.net/...3.mp4',
    ]

    engine.say("Video download started")
    engine.runAndWait()

    t1 = time.perf_counter()  # Start timer
    with tpe() as executor:
        executor.map(VideoDownloader, list_of_video, range(len(list_of_video)))  # Parallel execution
    print('Time Taken to Download Video Files', time.perf_counter() - t1)

    engine.say("Video download ended")
    engine.runAndWait()

# Function to download a PDF
def PdfDownloader(url, n):
    text = requests.get(url)
    if not os.path.exists("DeleteME"):
        os.mkdir("DeleteME")  # Create folder if not exists

    print(f"We are starting download {n+1}")
    with open(f'DeleteME/PDF{n+1}.pdf', 'wb') as file_Object:
        file_Object.write(text.content)  # Save PDF content

# Decorator function to add speech notifications for PDFs
def decorator_For_pdf(PDF_meta):
    def decofunc():
        engine.say("PDF download started")
        engine.runAndWait()

        PDF_meta()

        engine.say("PDF download ended")
        engine.runAndWait()

    return decofunc

@decorator_For_pdf
def PDF_meta():
    # List of PDF URLs
    list_of_pdf = [
        'http://dtu.ac.in/Web/notice/2023/oct/file1042.pdf',
        'http://dtu.ac.in/Web/notice/2023/sep/file0928.pdf',
    ]

    t1 = time.perf_counter()  # Start timer
    with tpe() as executor:
        executor.map(PdfDownloader, list_of_pdf, range(len(list_of_pdf)))  # Parallel execution
    print('Time Taken to Download PDF Files', time.perf_counter() - t1)

# Function to sort downloaded files into respective folders
def parallelsorting(file):
    # Move files to appropriate folders based on extension
    if file.endswith('.jpg'):
        shutil.move(f'DeleteMe/{file}', f'Sycamore/Image folder/{file}')
    elif file.endswith('.mp4'):
        shutil.move(f'DeleteMe/{file}', f'Sycamore/Video folder/{file}')
    elif file.endswith('.pdf'):
        shutil.move(f'DeleteMe/{file}', f'Sycamore/PDF folder/{file}')

# Function to organize files into folders
def file_sorting():
    List_of_files_in_DeleteMe = os.listdir('DeleteMe')  # List all files
    if not os.path.exists("Sycamore"):
        os.mkdir("Sycamore")  # Create parent folder

    # Create subfolders
    for folder in ('Image folder', 'Video folder', 'PDF folder'):
        if not os.path.exists(f"Sycamore/{folder}"):
            os.mkdir(f"Sycamore/{folder}")

    engine.say("File sorting started")
    engine.runAndWait()

    t1 = time.perf_counter()
    with tpe() as executor:
        executor.map(parallelsorting, List_of_files_in_DeleteMe)  # Parallel sorting
    print("Time taken in file sorting: ", time.perf_counter() - t1)

    engine.say("File sorting ended")
    engine.runAndWait()

# Main logic for the script
while number < 1:
    number = 1

    name = input("Enter Your Name: ")
    engine.say(f'{name}, say: Start the execution')
    engine.runAndWait()

    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.1)  # Adjust for noise
            print("Wait")
            time.sleep(2)
            print("Speak:\n\n\U0001F914\n\n")
            audio2 = r.listen(source2)  # Listen for audio
            text = r.recognize_google(audio2).lower()  # Convert speech to text
            print('\tDid you say', text)
    except:
        print("Error occurred. Please provide input in text.")
        text = input("\nType: Start the execution").lower()
    finally:
        if __name__ == '__main__':
            if text == 'start the execution':
                engine.say('Execution started')
                engine.runAndWait()

                Image_meta(10)  # Download 10 images
                # Video_meta()  # Uncomment to download videos
                PDF_meta()  # Download PDFs
                file_sorting()  # Sort files

                engine.say('Work ended')
                engine.runAndWait()

                time.sleep(60)
                shutil.rmtree('DeleteMe')  # Delete temporary folder
                engine.say('DeleteMe folder deleted')
                engine.runAndWait()
