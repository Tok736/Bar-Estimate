from string import punctuation

from transliterate import translit

def make_permalink(prompt: str) -> str:
    prompt = translit(prompt.lower(), "ru", reversed=True)
    for p in punctuation:
        prompt = prompt.replace(p, "")
    return prompt.replace(" ", "_")