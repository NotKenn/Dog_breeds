from flask import Flask, render_template, request
import pickle
import fastbook
fastbook.setup_book()

from fastbook import *
from fastai.vision.widgets import *
from fastai.metrics import error_rate


model = pickle.load(open('dog_breeds_dataset.pkl', 'rb'))
learn_inf = load_learner('export.pkl')

def extract_words_before_keywords(text, keywords):
    results = []
    for keyword in keywords:
        try:
            # Find the index of the keyword in the list of words
            keyword_index = text.index(keyword)
            
            # Extract the word immediately before the keyword
            if keyword_index > 0:
                word_before = text[keyword_index - 1].strip()
                results[keyword] = word_before
            else:
                # Handle the case where the keyword is the first word
                results[keyword] = None
        except ValueError:
            # Handle the case where the keyword is not found in the text
            results[keyword] = None
    return results

def extract_values_with_keywords(text, keywords):
    results = []
    for keyword in keywords:
        index = text.find(keyword)
        if index != -1:
            value_start = index + len(keyword)
            value = text[value_start:].strip()
            # Extract only until the next comma or end of the string
            comma_index = value.find(',')
            if comma_index != -1:
                value = value[:comma_index].strip()
            results.append(value)
    return results

def remove_words_with_keywords(input_text, keywords):
    for keyword in keywords:
        input_text = input_text.replace(keyword, "")
    return input_text.strip()


app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predictO():
    imagefile = request.files['imagefile']
    imagepath = "./images/" + imagefile.filename
    imagefile.save(imagepath)

    img = load_image(imagepath)
    imgpred = learn_inf.predict(img)[0]
    result = imgpred

    # text = request.form['textinput']
    # keywords = ["height", "fur color", "country of origin", "color of eyes", "common health problems", "common traits"]
    # keyword2 = ["inch",""]
    # keyword3 = []
    # result = str(extract_values_with_keywords(text, keywords))
    # for word in keyword2:
    #     result = result.replace(word, "")
    # for word in keyword3:
    #     result = result.replace(word, "")

    return render_template('index.html', prediction=result)


if __name__ == "__main__":
    app.run(port=3000, debug=True)