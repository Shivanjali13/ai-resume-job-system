import warnings
warnings.filterwarnings("ignore")
import spacy
import json
import pickle
import random
from spacy.training import Example

# Load training data
train_data = pickle.load(open('data/training/train_data.pkl', 'rb'))
print("Sample training data:\n", train_data[0])

# Create blank English model
nlp = spacy.blank("en")


# --------- REMOVE OVERLAPPING ENTITIES ----------
def remove_overlapping_entities(train_data):
    cleaned_data = []

    for text, annotations in train_data:
        entities = annotations["entities"]
        entities = sorted(entities, key=lambda x: (x[0], x[1]))

        filtered = []
        last_end = -1

        for start, end, label in entities:
            if start >= last_end:
                filtered.append((start, end, label))
                last_end = end

        cleaned_data.append((text, {"entities": filtered}))

    return cleaned_data


# --------- TRAIN MODEL ----------
def train_model(train_data):

    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    # Add labels
    for _, annotations in train_data:
        for ent in annotations['entities']:
            ner.add_label(ent[2])

    # Disable other pipes
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

    with nlp.disable_pipes(*other_pipes):

        optimizer = nlp.begin_training()

        for itn in range(10):
            print("Starting iteration:", itn)

            random.shuffle(train_data)
            losses = {}

            for text, annotations in train_data:
                try:
                    doc = nlp.make_doc(text)
                    example = Example.from_dict(doc, annotations)

                    nlp.update(
                        [example],
                        drop=0.2,
                        sgd=optimizer,
                        losses=losses
                    )

                except Exception as e:
                    print("Skipped example due to error:", e)

            print("Losses:", losses)

    # Save trained model
    nlp.to_disk("skill_model")
    print("\nModel saved inside 'skill_model' folder")


# --------- CLEAN DATA ----------
train_data = remove_overlapping_entities(train_data)

# --------- TRAIN ----------
train_model(train_data)