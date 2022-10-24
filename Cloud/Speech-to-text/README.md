# Step 1: Choose [Awesome-Swiss-German Project](https://cloud.google.com/speech-to-text)

# Step 2: Enable the Speech-to-Text API

You'll be using the Speech-to-Text API in this project. Enable it by clicking Enable APIs:
Unable to enable required APIs

    speech.googleapis.com 

When you see a green checkmark next to all of the APIs listed above, click Next.

 # Step 3:Open Cloud Shell

Cloud Shell is a built-in command-line tool for the console. In this tutorial, you use Cloud Shell to deploy your app.

Open Cloud Shell by clicking

Activate Cloud Shell.


# Step 4: Create an application

    To create a new Python application, run the following command:

` mkdir speech-to-text-python && \
    touch \
    speech-to-text-python/app.py

`
To set the speech-to-text-python directory as your Cloud Shell workspace and open the Cloud Shell Editor, run the following command:
cd speech-to-text-python
cloudshell open-workspace .

To set your project ID in the Cloud Shell terminal, run the following command:

    export PROJECT_ID=<PROJECT-ID>

To learn how to authenticate requests to this API, click Next.

# Step 5 :

Set up authentication

To call the Speech-to-Text API, your application needs to authenticate its identity to the Speech-to-Text service and obtain authorization to perform tasks.

    Create a service account to authenticate your API requests:

gcloud iam service-accounts create \
    speech-to-text-quickstart \
    --project <PROJECT-ID>

Grant your service account the Speech-to-Text API User role:
gcloud projects \
    add-iam-policy-binding \
    <PROJECT-ID> --member \
    serviceAccount:speech-to-text-quickstart@<PROJECT-ID>.iam.gserviceaccount.com \
    --role roles/speech.serviceAgent

Create a service account key:

    gcloud iam service-accounts keys \
        create speech-to-text-key.json \
        --iam-account \
        speech-to-text-quickstart@<PROJECT-ID>.iam.gserviceaccount.com

    Set the key as your default credentials:

export \
    GOOGLE_APPLICATION_CREDENTIALS=speech-to-text-key.json

To learn how to call the Speech-to-Text API, click Next.
      
      Call the Speech-to-Text API

    Open `app.py` in the [Cloud Shell Editor](https://cloud.google.com/shell/docs/editor-overview?hl=en-GB)

in the Cloud Shell Editor by running the following command in your terminal:
` cloudshell open app.py`

Install the Speech-to-Text client library:
` pip3 install --upgrade \
    google-cloud-speech`

In `app.py`, import the Speech-to-Text client library at the beginning of the file:
from google.cloud import speech

Create a Speech-to-Text API client and add a variable that points to the path of the example audio file provided:
` # Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw" `

Add the following code, which transcribes your audio file using the specified configuration, then prints the transcription:
` def transcribe_speech():
  audio = speech.RecognitionAudio(uri=gcs_uri)

  config = speech.RecognitionConfig(
      encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
      sample_rate_hertz=16000,
      language_code="en-US",
  )

  # Detects speech in the audio file
  response = client.recognize(config=config, audio=audio)

  for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript)) `

At the end of your app.py file, call transcribeSpeech():
` transcribe_speech() `

From your terminal, run your application.

 `   python3 app.py `

You should now see the transcribed message in your terminal:

` Transcript: Wie alt isch die ETH Zurich. `

To avoid incurring charges to your account and learn about next steps, click Next.
      
# Step 7:  Clean up

Delete the file containing your service account key.
` rm speech-to-text-key.json `
If you created a project specifically for this tutorial, you can delete it on the Google Cloud console Projects page. 
