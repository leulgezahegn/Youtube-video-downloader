import os
import requests
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    filters,
    MessageHandler,
)
from pytube import YouTube  
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
load_dotenv()

TOKEN = os.getenv("TOKEN")
SAVE_PATH = "vedio"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! Send me a YouTube video link and I will download it with subtitles."
    )


def delete_files(file):
    try:
        os.remove(file)
        print(f"{file} deleted.")
    except FileNotFoundError:
        print(f"{file} not found.")
    except PermissionError:
        print(f"Sizda {file} You don't have permission to delete")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")


async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if not update.message.text.startswith("https://www.youtube.com/") and not update.message.text.startswith("https://youtu.be/"):
            return await context.bot.send_message(chat_id=update.effective_chat.id, text="Send me youtube vedio URL")
        r = requests.get(update.message.text)
        if "Video unavailable" in r.text:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="URL in invalid")

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Vedio downloading ...")
        
        #downlod vedio
        youtube_link = update.message.text
        yt = YouTube(youtube_link)
        file = yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download(SAVE_PATH)
        video_title = file.title()
        video_file = f"{video_title}"
        await update.message.reply_document(open(video_file, 'rb'))
        os.remove(video_file)

        #downlod subtitle
        transcript = YouTubeTranscriptApi.get_transcript(youtube_link.split("=")[1])
        formatter = SRTFormatter()
        caption = formatter.format_transcript(transcript)
        with open(f'{video_title}.srt', 'w') as the_file:
            the_file.write(caption)
        subtitle_file = f"{video_title}.srt"
        await update.message.reply_document(open(subtitle_file, 'rb'))
        os.remove(subtitle_file)
    except Exception as ex:  
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Server error: Somthing went wrong")
        print("Error: ", ex)
    finally:
        pass
        delete_files(video_file, )
        delete_files(video_file+".srt")


def main() -> None:
    print("App running")
    app = ApplicationBuilder().token(TOKEN).read_timeout(3000).write_timeout(3000).build()

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download_video))
    app.add_handler(CommandHandler("start", start))

    app.run_polling()


if __name__ == "__main__":
    main()
