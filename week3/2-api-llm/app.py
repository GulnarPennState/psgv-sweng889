import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

topic = input("Enter a topic: ")
prompt = f"Explain {topic} in 2-3 simple sentences for a beginner."
response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt,
)

print("\nAI response:\n")
print(response.output_text)

usage = response.usage
input_price = usage.input_tokens * 0.15 / 1_000_000
output_price = usage.output_tokens * 0.60 / 1_000_000
print(f"\nTokens used: {usage.total_tokens}")
print(f"Estimated price: ${input_price + output_price:.8f}")
