# Training LLMs on AIIA_DATASETS: Llama 3.2 vs Kimi K3

## The Experiment

Yesterday I started training models using the newly created **AIIA_DATASETS**. Goal: teach models to correctly invoke **AIIA Framework** tools.

## Phase 1: Llama 3.2

- 🚀 **Started with Llama 3.2** and the new AIIA_DATASETS
- ✅ **Training looked successful**
- 🎨 **Beautiful moment:** When testing the new version, the model started using **icons within its responses** — exactly the format and style it was trained on. That visual confirmation that training worked was lovely.

## Phase 2: Kimi K3

- 🤖 **Next, tried Kimi K3** — there exists a small version suitable for training
- ⚠️ **Didn't go as smoothly as Llama 3.2** at first
- 📈 **But progress was visible** — step by step, the model improved
- ✅ **Eventually, Kimi training was successful too**

## Phase 3: GGUF Conversion

- 🔄 **Decided to convert Kimi to GGUF format**
- 🔧 **This required modifications to llama.cpp**
- ⏸️ **Paused here** — will continue once OpenCode recharges its credit

## Key Insights

1. **Llama 3.2 adapted quickly** to the AIIA tool-call format and even learned stylistic elements like icons
2. **Kimi K3 needed more patience** but eventually converged
3. **GGUF conversion is the next frontier** — requires llama.cpp tweaks
4. **Training data quality matters** — AIIA_DATASETS provided the structure needed for both models to learn

## Next Steps

- Continue GGUF conversion once credits are available
- Test converted models for inference speed and quality
- Compare Llama 3.2 and Kimi K3 outputs on real AIIA tasks

## See Also

- [AIIA_DATASETS repository](https://github.com/m5it/AIIA_DATASETS)
- [AIIA Framework](https://github.com/m5it/AIIA)
- [KosGen AI Toolkit](https://github.com/m5it)
