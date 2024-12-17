

### **README.md**

# 🎙️ Speech-to-Text and Text Summarization Project

This project leverages **OpenAI's Whisper API** for transcribing speech (audio files) to text and **GPT-3.5-turbo** for summarizing the transcribed text. It's implemented in Python and designed for use in **Google Colab**.

---

## 🚀 Features

1. **Speech to Text**: 
   - Uses OpenAI's Whisper API to convert audio files into text.
2. **Text Summarization**:
   - Summarizes the transcribed text using OpenAI's GPT-3.5-turbo model.

---

## 🛠️ Requirements

- Python 3.8+
- OpenAI API key
- Google Colab environment (recommended)

---

## 📦 Installation

1. Install the required OpenAI library:
   ```bash
   pip install openai==0.28
   ```

2. Prepare your **OpenAI API Key**:
   - Store your OpenAI API key securely using Google Colab's `userdata` or replace this line:
     ```python
     from google.colab import userdata
     OPENAI_API_KEY = userdata.get('OpenAi')
     ```
     **Alternative**: Replace `OPENAI_API_KEY` directly in your code:
     ```python
     OPENAI_API_KEY = "your_openai_api_key_here"
     ```

3. Upload audio files to transcribe:
   ```python
   from google.colab import files
   uploaded = files.upload()
   ```
   
4. **Access the Colaboratory**
   ```bash
   Colab : <https://colab.research.google.com/drive/1lNx2Qgk3kVOGHjjGrJhYgYkLD61DiXFY?usp=drive_link>
   
   ```
---

## ⚙️ Code Overview

1. **Transcription**:
   - Reads audio files and sends them to the Whisper model for transcription:
   ```python
   transcription = openai.Audio.transcribe(
       model='whisper-1',
       file=audio_file,
       response_format='text'
   )
   ```

2. **Summarization**:
   - Passes the transcription to GPT-3.5-turbo to summarize it:
   ```python
   def summarize_text(text):
       response = openai.ChatCompletion.create(
           model='gpt-3.5-turbo',
           messages=[
              {"role":"user","content":f"summarize the following text:{text}"}
           ],
           max_tokens=50
       )
       return response['choices'][0]['message']['content']
   ```

3. **Execution Flow**:
   - Upload → Transcribe → Summarize → Display.

---

## 🔧 Usage

1. Run the script in Google Colab.
2. Upload your audio file (e.g., `.mp3`, `.wav`).
3. The script will:
   - Transcribe the audio into text.
   - Summarize the transcribed text.
4. The output is displayed in the Colab notebook:
   - Full transcription.
   - Summarized text.

---

## 📝 Example Output

**Transcription**:  
`"Welcome to our Customer Support Helpline. Did you know you can check your account balance or pay your bills directly from our mobile app? It's quick, easy, and secure. For further assistance, stay on the line to speak with a representative. Thank you for choosing our service.
."`

**Summary**:  
`"This text is informing customers about the benefits of using the mobile app to check account balances and pay bills. Customers are encouraged to stay on the line if they need further assistance. The company appreciates customers choosing their service.
."`

---

## 🌟 Dependencies

- OpenAI Python Library: `openai==0.28`
- Google Colab: To manage file uploads and APIs.

---

## 📂 File Structure

```
.
├── main_script.py       # Main Python script
├── README.md            # Project documentation
└── (Audio files)        # Uploaded by the user
```

---

## 🔑 API Key Setup

1. Visit [OpenAI Platform](https://platform.openai.com/).
2. Generate an API key.
3. Replace the `OPENAI_API_KEY` variable in your script.

---

## 👨‍💻 Contributing

Pull requests are welcome! For significant changes, please open an issue to discuss your proposed modifications.

---


Feel free to add additional details based on your specific requirements or extend it further with instructions on setting up the environment.

Let me know if you need help refining this further! 🚀
