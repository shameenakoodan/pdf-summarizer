from groq import Groq
import os
from dotenv import load_dotenv
from pdf_reader import detect_language

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def chunk_text(text, max_length=3000):
    chunks = []
    current = ""

    for line in text.split("\n"):
        if len(current) + len(line) < max_length:
            current += line + "\n"
        else:
            chunks.append(current.strip())
            current = line + "\n"

    if current.strip():
        chunks.append(current.strip())

    return chunks


def summarize_chunk(chunk, target_language, length="medium"):
    length_instructions = {
        "short": "Summarize in 3–5 bullet points.",
        "medium": "Summarize in 6–10 bullet points.",
        "detailed": "Summarize in 10–15 bullet points with more explanation."
    }

    prompt = f"""
    {length_instructions[length]}

    Write the summary in {target_language}.
    Use clear, concise bullet points.

    Text:
    {chunk}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def summarize_text(full_text, length="medium", target_language=None):
    detected_lang = detect_language(full_text)
    target_language = target_language or detected_lang

    chunks = chunk_text(full_text)
    partial_summaries = []

    for chunk in chunks:
        summary = summarize_chunk(chunk, target_language, length)
        partial_summaries.append(summary)

    combined_prompt = f"""
    Combine the following partial summaries into one clean, structured summary.
    Remove repetition and organize ideas logically.

    Final summary language: {target_language}
    Tone: neutral, professional.

    Partial summaries:
    {partial_summaries}
    """

    final_response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": combined_prompt}]
    )

    return final_response.choices[0].message.content
