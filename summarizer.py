from dotenv import load_dotenv
import os
from groq import Groq
load_dotenv()  # loads the .env file

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)
#Breaks long text PDF text into ~3000 character chunks so th model can handle them
def chunk_text(text, max_length=3000):
    chunks  = []
    current = ""
    for line in text.split("\n"):
        if len(current) + len(line) <max_length:
            current += line + "\n"
        else:
            chunks.append(current)
            current = line + "\n"
    if current:
        chunks.append(current)
    
    return chunks

#Sends each chunk to the AI model with a clear summarization prompt
def summarize_chunk(chunk):
   prompt = f"""
    Summarize the following text in clear, concise bullet points.
    Focus only on the key ideas.

    Text:
    {chunk}
    """
   response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
   )
   return response.choices[0].message.content.strip()

#Splits the text

#Summarizes each chunk

#Combines all partial summaries into one polished final summary

#This avoids token limits and produces a clean result.
def summarize_text(full_text):
    chunks = chunk_text(full_text)
    partial_summaries = []

    for chunk in chunks:
        summary = summarize_chunk(chunk)
        partial_summaries.append(summary)

    combined_prompt = f"""
    Combine the following partial summaries into one clean, structured summary.
    Remove repetition and organize the ideas logically.

    Partial summaries:
    {partial_summaries}
    """
    final_response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages=[{"role": "user", "content": combined_prompt}]
    )

    return final_response.choices[0].message.content