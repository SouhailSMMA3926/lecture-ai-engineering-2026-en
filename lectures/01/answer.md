# Lecture 01 Answers

## Exercises

- Model's answer to the course-specific question (the 3 homework levels; a summary is fine):


The following answer from the AI model was obtained:
"It looks like you are referring to a specific course, likely **AIE2026** (which usually denotes an Artificial Intelligence Engineering or related course for the year 2026 or academic term 2026). 

Because course codes, curricula, and homework assignments vary wildly depending on the specific university, professor, or online platform (such as Coursera, edX, or a specific university's computer science department) hosting the "AIE2026" course, **there is no universal standard "3 Lists" homework assignment associated with this exact title.**

To help you find the answer, could you provide a little more context?
1. **What is the name of the university, institution, or platform** offering the AIE2026 course?
2. **Who is the instructor?**
3. **What is the topic of the current module or week** (e.g., Python basics, Machine Learning algorithms, Data structures)?

If you can share a snippet of the homework prompt or syllabus, I would be happy to help you break it down and solve it!"

It can be observed that the model doesn't know specific answers. It can also be observed that the answer changes when asked a second time.

- What you noticed when comparing it with the correct meaning in the glossary:

The correct definition from the glossary is : "The structure of AIE2026 homework. There are three levels: \"Basic (review lecture content)\", \"Implementation (write your own code)\", and \"Advanced (research and experimentation)\". Completing any one level completes the homework for that lecture. As a rule, it is not graded."


- Token counts you displayed (input / output):
Input tokens: 18
Output tokens: 232

## Homework

- Level attempted: Basic / Implementation / Advanced
- What you did:Basic/ Implementation/ Advanced
- Results:


-Basic 


--Run 1


@SouhailSMMA3926 ➜ /workspaces/lecture-ai-engineering-2026-en (lec01) $ uv run python -m app.ask "Write a short, creative 3-sentence story about LoRA."
[model] gemini-3.5-flash-lite
[question] Write a short, creative 3-sentence story about LoRA.

Input tokens: 15
Output tokens: 75
The ancient giant AI slumbered, too heavy to shift its massive mountains of frozen memory. Suddenly, a tiny humming-bird of a patch—a LoRA—darted into its ear, whispering a brand-new vocabulary of vibrant pigments. In a single breath, the behemoth awoke, painting galaxies it had never seen before without moving an inch of its original bones.

--Run 2(with another AI model)


@SouhailSMMA3926 ➜ /workspaces/lecture-ai-engineering-2026-en (lec01) $ AIE_MODEL=gemini-3.5-flas
h uv run python -m app.ask "Write a short, creative 3-sentence story about LoRA."
[model] gemini-3.5-flash
[question] Write a short, creative 3-sentence story about LoRA.

Input tokens: 15
Output tokens: 77
The massive neural titan stood frozen, far too heavy for the artist to re-sculpt its billions of parameters. Instead of rebuilding the giant, she attached a LoRA—a delicate harness of low-rank matrices that softly whispered new instructions. Guided by the gentle adapter, the monolith suddenly painted with exquisite, customized grace, learning a whole new world without changing a single core memory.

-Run 3: Rerun for run 1 for comparisation


@SouhailSMMA3926 ➜ /workspaces/lecture-ai-engineering-2026-en (lec01) $ uv run python -m app.ask "Write a short, creative 3-sentence story about LoRA."
[model] gemini-3.5-flash-lite
[question] Write a short, creative 3-sentence story about LoRA.

Input tokens: 15
Output tokens: 71
The monolithic giant of the pre-trained neural network slumbered, infinitely wise yet stubbornly inflexible. Along tiptoed the tiny, weight-efficient sprite of LoRA, whispering a few fleeting parameter adjustments into its ear. Suddenly, the ancient titan awakened, effortlessly pirouetting into an entirely new dance of creation without forgetting a single step of its past.


-Implementation
To be able to ask follow-up questions, the google-genai SDK is used. The ask.py is modified and tested

RESULT: The following answer is obtained upon testing: @SouhailSMMA3926 ➜ /workspaces/lecture-ai-engineering-2026-en (lec01) $ uv run python -m app.ask
[model] gemini-3.5-flash-lite
Interactive Chat Mode initialized. Type 'exit' or 'quit' to end.

You: Hi I am study AI engineering in 2026
[Tokens] Input: 13 | Output: 262
AI: That is an incredible time to be studying AI engineering. By 2026, the field has evolved *massively* from the early generative AI boom of 2023–2024. 

The industry has largely moved past the "hype" phase of just wrapping a basic prompt around an off-the-shelf LLM. Today, AI engineering is much more rigorous, focusing on **reliability, multi-agent systems, edge computing, inference optimization, and deep integration into complex software architectures.**

Since you’re in the thick of your studies right now, how can I help you today? Are you looking for:

1. **Architecture concepts:** Like designing RAG systems, working with agentic workflows, or fine-tuning small language models (SLMs)?
2. **Tech stack advice:** Which frameworks (LangChain, LlamaIndex, PyTorch, vLLM, etc.) and languages are most relevant in 2026?
3. **Career prep:** Portfolio project ideas, interview concepts, or understanding what hiring managers are looking for right now?
4. **Debugging code:** Working through a specific AI/ML assignment or project?

Let me know what you're working on or what's on your mind!

You: Tell me what I am studying and in what year
[Tokens] Input: 287 | Output: 66
AI: You are studying **AI engineering** and the year is **2026**! 

(Based on your first message: *"Hi I am study AI engineering in 2026"*, those are the exact parameters you gave me.) 

How can I help you with your studies today, future engineer?

This interaction proves the implementation was successful.

-Advanced
This involves measuring the latency response. The Python's time module) alongside token counts. It will then be tested for different results.
The following responses were obtained for different questions:

@SouhailSMMA3926 ➜ /workspaces/lecture-ai-engineering-2026-en (lec01) $ uv run python -m app.ask
[question] What are the 3 homework levels in the AIE2026 course?

[Model] gemini-3.5-flash-lite
[Latency] 1.64 seconds
[Tokens] Input: 18 | Output: 188 | Total: 206
[Speed] 114.67 output tokens/sec
Based on the structure of the AIE2026 (Artificial Intelligence Engineering 2026) course, the three homework levels are:

1. **Level 1 (Basic / Beginner):** Focused on foundational concepts, syntax, and getting the basic environment set up and running simple tasks.
2. **Level 2 (Intermediate):** Focused on applying concepts to more complex scenarios, modifying existing models or pipelines, and handling standard data manipulation.
3. **Level 3 (Advanced / Expert):** Focused on deep implementation, optimization, open-ended problem solving, and building or fine-tuning advanced AI architectures. 

*(Note: Depending on the specific platform or cohort dashboard you are using for AIE2026, these may also be referred to simply as **Level 1, Level 2, and Level 3**, or categorized by difficulty as Beginner, Intermediate, and Advanced).*

@SouhailSMMA3926 ➜ /workspaces/lecture-ai-engineering-2026-en (lec01) $ uv run python -m app.ask "What is 2 + 2?"
[question] What is 2 + 2?

[Model] gemini-3.5-flash-lite
[Latency] 0.80 seconds
[Tokens] Input: 9 | Output: 7 | Total: 16
[Speed] 8.79 output tokens/sec
2 + 2 = 4

@SouhailSMMA3926 ➜ /workspaces/lecture-ai-engineering-2026-en (lec01) $ uv run python -m app.ask "What is LoRA in machine learning?"
[question] What is LoRA in machine learning?

[Model] gemini-3.5-flash-lite
[Latency] 3.63 seconds
[Tokens] Input: 9 | Output: 875 | Total: 884
[Speed] 240.97 output tokens/sec
**LoRA**, which stands for **Low-Rank Adaptation**, is a popular and efficient technique used in machine learning (specifically in Natural Language Processing and Computer Vision) to **fine-tune large pre-trained models**. 

Introduced by researchers at Microsoft in 2021, LoRA solves a major bottleneck in AI: how to adapt massive models to specific tasks without spending a fortune on computing power and memory.

Here is a breakdown of how it works, why it matters, and where it is used.
PLEASE NOTE THAT I AM NOT GOING TO PASTE THE WHOLE RESPONSE BECAUSE IT IS VERY LONG.

- Observations and questions: 

-Basic
They are all different answers but revolving around the same components, and the difference can be seen in the words predicited such as giant for gemini-3.5-flash-lite but titan for gemini-3.5-flash. However the variation in Input and output tokens are almost the same.

-Implementation
After implementing the google-genai SDK feature, I told the model an information about me, and I asked a follw-up question to see if it remembers, and it did. This means an interactive chat can take place.

-Advanced
After changing the ask-py code to implement latency and total tokens, I could see the difference between a simple command compared to a more complez ones in terms of longer latency. Moreover it can also be seen in the numbe rof output tokens, whereby a more complex question has a significantly larger amount of output tokens.
