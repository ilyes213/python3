import openai

openai.api_key = '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'

model = openai.Model.retrieve('text-davinci-004')
print(model)
