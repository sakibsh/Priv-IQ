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
