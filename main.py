import requests
import json
from typing import List
from bs4 import BeautifulSoup
import ollama

MODEL = "CognitiveComputations/dolphin-llama3.1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        self.url = url
        response = requests.get(url, headers=headers)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""
        links = [link.get('href') for link in soup.find_all('a')]
        self.links = [link for link in links if link]

    def get_contents(self):
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"

link_system_prompt = """
You are provided with a list of links found on a webpage.
You must decide which links would be relevant for a company brochure,
such as 'About', 'Company', or 'Careers/Jobs' pages.

Respond in JSON format like this:
{
    "links": [
        {"type": "about page", "url": "https://example.com/about"},
        {"type": "careers page", "url": "https://example.com/careers"}
    ]
}
"""

def get_links_user_prompt(website):
    user_prompt = f"Here is the list of links on {website.url}. Please determine which are relevant for a company brochure. Respond in JSON format.\n\n"
    user_prompt += "\n".join(website.links)
    return user_prompt

def get_links(url):
    website = Website(url)
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    result = response['message']['content']
    return json.loads(result)

def get_all_details(url):
    result = "Landing page:\n"
    result += Website(url).get_contents()
    links = get_links(url)
    print("Found links:", links)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += Website(link["url"]).get_contents()
    return result

system_prompt = """
You are an assistant analyzing a company website and creating a short brochure
for prospective customers, investors, and recruits. Respond in markdown format.

Include details about company culture, customers, and careers/jobs if available.
"""

def get_brochure_user_prompt(company_name, url):
    user_prompt = f"Company Name: {company_name}\n\n"
    user_prompt += "Here are the contents of its landing page and relevant pages:\n"
    user_prompt += get_all_details(url)
    return user_prompt[:5000]

def create_brochure(company_name, url):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ]
    )
    result = response['message']['content']
    print("\nGenerated Brochure:\n")
    print(result)

# Run the script
create_brochure("Aiman", "https://aiman-portfolio-mu.vercel.app/")
