from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"


# a) Get predictions

nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def nlp_qna(context,question):

    QA_input = {
        'question': question,
        'context': context
    }
    res = nlp(QA_input)

    return res

'''res = nlp_qna(context, question)
print(res)'''
'''# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
'''
context="The tiger, majestic and powerful, epitomizes the essence of the wild. With its striking orange fur adorned by bold black stripes, it roams through dense jungles and grasslands with a graceful yet intimidating presence. As one of the largest and most formidable predators on Earth, the tiger commands respect and admiration. Sadly, due to habitat loss and poaching, many tiger species are endangered, highlighting the urgent need for conservation efforts to protect these magnificent creatures for generations to come."
question="What is the colour of fur of tiger?"

print(nlp_qna(context, question))

