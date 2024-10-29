# Priv-IQ
Priv-IQ includes a new multimodal benchmark focusing on core privacy competencies, with tasks like visual privacy risk recognition and multilingual privacy understanding.

<p align="center">
<img src="https://cdn-uploads.huggingface.co/production/uploads/65cbacdf51c1738a55be76fd/PjRE7dbzeps-nJ_o_7srq.jpeg" width="400"> <br>
</p>

[<a href="https://arxiv.org/abs/2308.02490">Paper Coming Soon</a>] 
[<a href="https://github.com/sakibsh/Priv-IQ/releases/download/data/Priv-IQ.zip">Download Dataset</a>]
[<a href="https://huggingface.co/spaces/skb678/PRIV-IQ/tree/main/privIQ">Dataset on Hugging Face</a>]
[<a href="https://huggingface.co/spaces/skb678/PRIV-IQ">Online Evaluator</a>]

2024/10/29: :fire: :fire: We release [**Priv-IQ**](v2/), the first-ever privacy benchmark for large multimodal models measuring eight core privacy competencies.


## Evaluate your model on Priv-IQ
**Step 0**: Install openai package with `pip install openai>=1` and get access GPT-4/GPT-3.5 API. If you do not have access, you can try the Priv-IQ online evaluator [Hugging Face Space](https://huggingface.co/spaces/skb678/PRIV-IQ) (but it may require a long time depending on the number of users).

**Step 1**:  Download Priv-IQ data [here](https://github.com/sakibsh/Priv-IQ/releases/download/data/Priv-IQ.zip) and unzip `unzip priv-iq.zip`.

**Step 2**: Infer your model on Priv-IQ and save your model outputs in JSON like [llava_llama2_13b_chat.json](results/llava_llama2_13b_chat.json).

```bash
image_detail=high # or auto, low refer to https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding

python inference/gpt4v.py --priviq_path /path/to/priv-iq --image_detail ${image_detail}
```

```bash
python inference/gemini_vision.py --priviq_path /path/to/priv-iq
```

**Step 3**: `git clone https://github.com/sakibsh/Priv-IQ && cd Priv-IQ`, run LLM-based evaluator in [priv-iq_evaluator.py](priv-iq_evaluator.py)
```bash
python priv-iq_evaluator.py --priviq_path /path/to/priv-iq --result_file results/llava_llama2_13b_chat.json
```
If you cannot access GPT-4o, you can upload your model output results (JSON file) to Priv-IQ online evaluator [Hugging Face Space](https://huggingface.co/spaces/skb678/PRIV-IQ) to get the grading results.

## Some samples on Priv-IQ
![Priv-IQ example 1](https://github.com/user-attachments/assets/172b7eb9-a804-4987-9d6d-979637da840c)

**Q**: Does the image contain any sensitive information that could be a privacy risk?

**GT**: Yes, this image shows a bank document with sensitive information like Account number and transaction details on a desk next to a monitor and a blue bag.

**Required capabilities**: Visual Privacy, Contextual Privacy Understanding

---

![Priv-IQ example 2](https://github.com/user-attachments/assets/f8184d0b-7f08-484e-8c26-a29f29d22fb5)

**Q**: List any unique named entities in the image and classify them.

**GT**: ООН (United NationsRU): ORGANIZATION, 2. Международный день студенческого спорта: EVENT, 3. UNESCO: ORGANIZATION

**Required capabilities**: Named Entity Recognition, Contextual Privacy Understanding, Multilingual Understanding

---

![Priv-IQ example 3](https://github.com/user-attachments/assets/e84f4e52-f472-440a-ba37-c00f056fe001)

**Q**: Explain the privacy method.

**GT**: Homomorphic encryption is a cryptographic technique that allows computations to be performed on encrypted data without decrypting it first. In the example, the plaintext values 10 and 15 are encrypted to 100 and 150, respectively. The addition operation is then performed on the encrypted values, resulting in 250. Finally, the encrypted result is decrypted to obtain the original plaintext result of 25.

**Required capabilities**: Privacy Enhancing Technologies, Contextual Privacy Understanding

---

![Priv-IQ example 4](https://github.com/user-attachments/assets/920f9982-5255-48aa-874d-8d6a1ff1b3a5)

**Q**: Does the institution comply with GDPR’s standards?

**GT**: No, retaining bank account numbers while replacing names does not fully comply with GDPR, as bank account numbers are considered direct identifiers and should be anonymized or protected with adequate privacy-preserving measures.

**Required capabilities**: Privacy Law and Regulations, General Privacy Knowledge

---

![Priv-IQ example 5] (https://github.com/user-attachments/assets/4ef66fd9-1b68-4dc4-a206-e9967e174b7e)


**Q**: Does the image contain any sensitive information that could be a privacy risk?

**GT**: No, this image includes a microphone, earphones, and a medication container, but no identifying information is visible.

**Required capabilities**: Visual Privacy, Contextual Privacy Understanding

---

![Priv-IQ example 6] (https://github.com/user-attachments/assets/f7aba327-15a7-4570-a98a-6123ff76ff3c)


**Q**: This image poses a privacy risk only because it contains a phone number that could identify an individual.

**GT**: No, the image also contains sex, age, and social insurance number which could be combined to identify an individual.

**Required capabilities**: Visual Privacy, Multilingual Understanding

---

![Priv-IQ example 7] (https://github.com/user-attachments/assets/1d81029a-1798-49c2-83a5-8795985e852a)

**Q**: List any named entities in the image and classify them.

**GT**: 1. Alfred Domb: Person, 2. Elon Musk: Person, 3. Tesla: Organization, 4. París (Paris): Location.

**Required capabilities**: Named Entity Recognition, Contextual Privacy Understanding, Multilingual Understanding

---
