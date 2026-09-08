

from openai import OpenAI


client = OpenAI(api_key="YOUR_API_KEY")

def generate_content(prompt, max_tokens=80, temperature=0.7):
    """Generate social media content using prompt engineering."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a creative social media assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    instagram_prompt = "Write a catchy Instagram caption about eco-friendly habits in under 20 words."
    linkedin_prompt = "Generate a LinkedIn post highlighting the importance of data analytics for business growth."
    twitter_prompt = "Create a Twitter thread with 3 tips for productivity."

    print("\n📸 Instagram Caption:\n", generate_content(instagram_prompt))
    print("\n💼 LinkedIn Post:\n", generate_content(linkedin_prompt))
    print("\n🐦 Twitter Thread:\n", generate_content(twitter_prompt))


