from urllib import response
import openai

def gpt3(stext):
    openai.api_key = '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'
    response = openai.Completion.create(
        engine = 'text-davinci-001',
        prompt = stext,
        temperature = 0.76,
        max_tokens = 1000,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0

    )
    content = response.choices[0].text.split('.')
    #print(content)
    return response.choices[0].text

# query = 'who is the best footballer in the world?'

# response = gpt3(query)
# print(response)