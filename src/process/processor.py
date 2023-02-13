import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer


class Processor:
    def __init__(self):
        if torch.cuda.is_available():
            self.device = torch.device("cuda")

            print('There are %d GPU(s) available.' % torch.cuda.device_count())

            print('We will use the GPU:', torch.cuda.get_device_name(0))
        else:
            print('No GPU available, using the CPU instead.')
            self.device = torch.device("cpu")

        self.model = T5ForConditionalGeneration.from_pretrained("NlpHUST/t5-small-vi-summarization")
        self.tokenizer = T5Tokenizer.from_pretrained("NlpHUST/t5-small-vi-summarization")
        self.model.to(self.device)
        self.model.eval()

    def summarize(self, text):
        tokenized_text = self.tokenizer.encode(text, return_tensors="pt").to(self.device)
        summary_ids = self.model.generate(
            tokenized_text,
            max_length=256,
            num_beams=5,
            repetition_penalty=2.5,
            length_penalty=1.0,
            early_stopping=True
        )
        summarized_text = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summarized_text
