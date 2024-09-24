from openai import AzureOpenAI


ENDPOINT = "https://mango-bush-0a9e12903.5.azurestaticapps.net/api/v1"
API_KEY = "${PLACE_HOLDER}"

API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-4o"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020.",
    },
    {"role": "user", "content": "Where was it played?"},
]

completion = client.chat.completions.create(
    model=MODEL_NAME,
    messages=MESSAGES,
)

print(completion.model_dump_json(indent=2))
