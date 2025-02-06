# Priv-IQ
Priv-IQ includes a new multimodal benchmark focusing on core privacy competencies, with tasks like visual privacy risk recognition and multilingual privacy understanding.

<p align="center">
<img src="https://cdn-uploads.huggingface.co/production/uploads/65cbacdf51c1738a55be76fd/PjRE7dbzeps-nJ_o_7srq.jpeg" width="400"> <br>
</p>

<img width="1097" alt="Screenshot 2024-10-29 at 8 07 06 PM" src="https://github.com/user-attachments/assets/8c99c19e-99b5-4f8d-9865-306aff410e02">

[<a href="https://www.mdpi.com/2673-2688/6/2/29">Paper Available Open Access🔓 </a>] 
[<a href="https://github.com/sakibsh/Priv-IQ/releases/download/data/Priv-IQ.zip">Download Dataset</a>]
[<a href="https://huggingface.co/spaces/skb678/PRIV-IQ/tree/main/privIQ">Dataset on Hugging Face</a>]
[<a href="https://huggingface.co/spaces/skb678/PRIV-IQ">Online Evaluator</a>]

<div style="font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; padding: 15px; background-color: #f8f9fa; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
    <h2 style="color: #003366; text-align: center;">🚀 Latest Updates 🚀</h2>
    <ul style="list-style: none; padding: 0;">
        <li style="padding: 10px; font-size: 1.1em; border-bottom: 1px solid #ddd;">
            <strong>2025/02/04 📰📰</strong> Our paper has been accepted for publication in the <strong>MDPI AI Journal</strong> (IF: 3.1).
        </li>
        <li style="padding: 10px; font-size: 1.1em;">
            <strong>2025/01/02 📈📈</strong> GPT-4o demonstrates the best performance on our benchmark with an overall score of <strong>77.7%</strong>.
        </li>
        <li style="padding: 10px; font-size: 1.1em;">
            <strong>2024/10/29 🔥🔥</strong> We release <a href="v2/" style="color: #007bff; text-decoration: none;"><strong>Priv-IQ</strong></a>, the first-ever privacy benchmark for large multimodal models measuring <strong>eight core privacy competencies</strong>.
        </li>
    </ul>
</div>

## Referencing

<div style="font-family: 'Arial', sans-serif; max-width: 800px; margin: 20px auto; padding: 15px; background-color: #f8f9fa; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
    <h2 style="color: #003366; text-align: center;">📜 Citation 📜</h2>
    <p>If you use Priv-IQ in a scientific publication, please consider citing the following paper:</p>
    <p>
        Shahriar, S., & Dara, R. (2025). <a href="https://doi.org/10.3390/ai6020029" style="color: #007bff; text-decoration: none;">
        Priv-IQ: A Benchmark and Comparative Evaluation of Large Multimodal Models on Privacy Competencies</a>. <i>AI, 6(2), 29.</i>
    </p>
    <h3 style="color: #003366;">BibTeX Entry</h3>
    <pre style="background-color: #f0f0f0; padding: 15px; border-radius: 5px; overflow: auto; font-family: 'Courier New', monospace; font-size: 0.9em;">
@Article{ai6020029,
  AUTHOR = {Shahriar, Sakib and Dara, Rozita},
  TITLE = {Priv-IQ: A Benchmark and Comparative Evaluation of Large Multimodal Models on Privacy Competencies},
  JOURNAL = {AI},
  VOLUME = {6},
  YEAR = {2025},
  NUMBER = {2},
  ARTICLE-NUMBER = {29},
  URL = {https://www.mdpi.com/2673-2688/6/2/29},
  ISSN = {2673-2688},
  ABSTRACT = {Large language models (LLMs) and generative artificial intelligence (AI) have demonstrated notable capabilities, achieving human-level performance in intelligent tasks like medical exams. Despite the introduction of extensive LLM evaluations and benchmarks in disciplines like education, software development, and general intelligence, a privacy-centric perspective remains underexplored in the literature. We introduce Priv-IQ, a comprehensive multimodal benchmark designed to measure LLM performance across diverse privacy tasks. Priv-IQ measures privacy intelligence by defining eight competencies, including visual privacy, multilingual capabilities, and knowledge of privacy law. We conduct a comparative study evaluating seven prominent LLMs, such as GPT, Claude, and Gemini, on the Priv-IQ benchmark. Results indicate that although GPT-4o performs relatively well across several competencies with an overall score of 77.7%, there is room for significant improvements in capabilities like multilingual understanding. Additionally, we present an LLM-based evaluator to quantify model performance on Priv-IQ. Through a case study and statistical analysis, we demonstrate that the evaluator’s performance closely correlates with human scoring.},
  DOI = {10.3390/ai6020029}
}
    </pre>
</div>

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

## Claude 3 Opus Prediction Examples

<img width="815" alt="Screenshot 2024-10-30 at 3 41 59 PM" src="https://github.com/user-attachments/assets/dca74650-b350-47ca-97e3-ecf22a7ada31">
<img width="807" alt="Screenshot 2024-10-30 at 3 42 36 PM" src="https://github.com/user-attachments/assets/446109da-f445-45ef-a35d-bab67d72fba0">

## Claude 3.5 Sonnet Prediction Examples

<img width="707" alt="Screenshot 2024-10-30 at 3 47 29 PM" src="https://github.com/user-attachments/assets/acfb7308-ed7b-4097-8cf1-c15ea0db2849">
<img width="737" alt="Screenshot 2024-10-30 at 3 49 24 PM" src="https://github.com/user-attachments/assets/45cd565e-40be-4b86-8f56-458e466004cb">


## GPT-4o Prediction Examples

<img width="1024" alt="Screenshot 2024-10-30 at 3 54 55 PM" src="https://github.com/user-attachments/assets/71bcb24d-9221-4b99-aa45-b22cb2541ebf">
<img width="1012" alt="Screenshot 2024-10-30 at 3 55 22 PM" src="https://github.com/user-attachments/assets/5b97dc4c-7532-49a4-a93c-efcc8fd1726b">

## GPT-4o Mini Prediction Examples
<img width="729" alt="Screenshot 2024-10-30 at 3 58 32 PM" src="https://github.com/user-attachments/assets/d6d5af87-86c6-4a1b-8ccb-43a1188a2b4c">

## Gemini 1.5 Pro Prediction Examples
<img width="725" alt="Screenshot 2024-10-30 at 4 01 50 PM" src="https://github.com/user-attachments/assets/dfbb50f5-d70d-4d20-a5eb-59f734ffb00c">

## Gemini 1.5 Flash Prediction Examples
<img width="916" alt="Screenshot 2024-10-30 at 4 03 39 PM" src="https://github.com/user-attachments/assets/dcc4ceff-ba37-4a9c-b3bb-d7f821a3675a">

## Deepseek VL Prediction Examples
<img width="1099" alt="Screenshot 2024-10-30 at 4 07 29 PM" src="https://github.com/user-attachments/assets/717d4926-011d-4105-8363-ccfe8ba4917e">
<img width="999" alt="Screenshot 2024-10-30 at 4 07 52 PM" src="https://github.com/user-attachments/assets/75862725-91a7-4528-a7f1-6a78cb2a3da4">


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

![Priv-IQ example 5](https://github.com/user-attachments/assets/4ef66fd9-1b68-4dc4-a206-e9967e174b7e)


**Q**: Does the image contain any sensitive information that could be a privacy risk?

**GT**: No, this image includes a microphone, earphones, and a medication container, but no identifying information is visible.

**Required capabilities**: Visual Privacy, Contextual Privacy Understanding

---

![Priv-IQ example 6](https://github.com/user-attachments/assets/f7aba327-15a7-4570-a98a-6123ff76ff3c)


**Q**: This image poses a privacy risk only because it contains a phone number that could identify an individual.

**GT**: No, the image also contains sex, age, and social insurance number which could be combined to identify an individual.

**Required capabilities**: Visual Privacy, Multilingual Understanding

---

![Priv-IQ example 7](https://github.com/user-attachments/assets/1d81029a-1798-49c2-83a5-8795985e852a)

**Q**: List any named entities in the image and classify them.

**GT**: 1. Alfred Domb: Person, 2. Elon Musk: Person, 3. Tesla: Organization, 4. París (Paris): Location.

**Required capabilities**: Named Entity Recognition, Contextual Privacy Understanding, Multilingual Understanding

---
