# LLMs
Notes on my studies and learnings of LLMs.,

## What is an LLM?
- LLMs are based on the transformer architecture.  2 main types of transformer arch:
    - Seq2Seq: Encoder-decoder chain.  Text first feeds into the encoder which vectorizes it.  Then, it is processed through an encoder neural network, and the output of that processing gets fed into a decoder.
    - Causal LM: Lacks the encoder portion
- Process for generating a sentence with an LLM
    1. Input a prompt
    2. Prompt is embedded and processed through model --> Probability distribution of next best token
    3. Next best token is put back into input with prompt
    4. Repeat 1-4 appending tokens as you go
    5. Model eventually generates an end of sentence token which says, "Hey we're done"
- Training
    - So consider the process for sentence generation outlined above
    - You start doing that with a prompt and "known"/"correct" response
    - When you get the probability distribution of tokens, you can compare to the "correct" probability distribution of the correct response, take the difference between the two (or some fancier version of taking the difference, frequency cross-entropy loss) to calculate the loss and use that to inform weight updates
    - You begin by training a baseLLM which is only good for next word prediction (basically autocomplete)
    - After creating a baseLLM, you can then move into InstructionTuning -- training a baseLLM model to summarize, translate, etc.
    - Fine tuning ideally includes Reinforcement Learning from Human Feedback (RHLF) -- e.g. the Instruction Tuned model outputs a bunch of summarizations and then humans give a score/reward.  The model is setup to try and maximize that score/reward and we get outputs more aligned with what humans value
## Compute Requirements Management
- Each parameter in an LLM is a number (for 32-bit precision, 4-bytes) and those take up space
    - Rule of thumb: 4GB GPU RAM/1B parameters
- If you quantize to 16bit, you halve the RAM requirement
- During training, due to optimizer states, gradients, activations, etc. you may need up to 20bytes/parameter of RAM
    - 5X what it takes to host it
