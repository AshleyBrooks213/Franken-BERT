import torch
from transformers import BertTokenizer, BertForSequenceClassification


class BERT:
    def set_device(self):
        # If there's a GPU available...
        if torch.cuda.is_available():
            # Tell PyTorch to use the GPU.
            device = torch.device("cuda")
        else:
            device = torch.device("cpu")

        return device

    def load_model(self, path):
        # Load a trained model and vocabulary that you have fine-tuned
        model = BertForSequenceClassification.from_pretrained(path)
        tokenizer = BertTokenizer.from_pretrained(path)

        return model, tokenizer

    def predict(self, text, model_path):
        device = self.set_device()

        model, tokenizer = self.load_model(model_path)

        model.to(device)

        # prepare our text into tokenized sequence
        inputs = tokenizer(text, padding=True, truncation=True,
                           max_length=64, return_tensors="pt").to(device)
        # perform inference to our model

        model.to(device)

        outputs = model(**inputs)
        # get output probabilities by doing softmax
        probs = outputs[0].softmax(1)
        # executing argmax function to get the candidate label
        return probs.argmax()
