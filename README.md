# AI Difference Analyzer

**Rhetorical Difference Engine Using a Conceptual OpAmp Approach**
*By Edward Chalk ([edward@fleetingswallow.com](mailto:edward@fleetingswallow.com))*

---

## What is AI Difference Analyzer?

The AI Difference Analyzer is a unique tool that analyzes two opposing opinions and produces a **synthesized, differentiated output** by focusing on their *qualitative rhetorical differences*. It leverages large language models (LLMs, e.g., OpenAI GPT-4) and is inspired by the concept of the **operational amplifier** ("op-amp") from electronics.

---

## The OpAmp Analogy: Why an OpAmp?

An **operational amplifier** ("op-amp") is a foundational electronic component that amplifies the *difference* between two input signals. In its classic configuration:

* It takes a **positive (+)** and a **negative (–)** input.
* The output is proportional to the **difference** between these two signals (multiplied by a gain factor).
* The op-amp itself doesn’t “know” the absolute value of each input; it only cares about the difference.

**Why is this analogy relevant?**

Most traditional debate and AI analysis focuses on absolute positions (“What is Opinion A?” “What is Opinion B?”).
AI\_Difference\_Analyzer instead “amplifies the difference”—systematically extracting, analyzing, and synthesizing *how* the two positions differ in three key rhetorical areas:

* **Ethos:** Credibility, trust, and authority.
* **Logos:** Logic, reasoning, and evidence.
* **Energeia:** Vividness, impact, and transformative potential.

The result is a new, hybrid perspective that expresses the *directional difference*—not just a bland average or compromise.

---

## Learn More: The Conceptual Theory

Want to understand the theory behind this tool?  
Check out this blog post:  
**[The Operational Amplifier of Ideas](https://fleetingswallow.com/operational-amplifier-of-ideas/)**

It covers:
- Why the op-amp analogy matters for information analysis
- What “identifying the difference between inputs” means in practical terms
- How this approach leads to a more creative and actionable qualitative computing paradigm

---

## Flexible Output: Adapt Your Analysis to Any Context

The difference engine doesn’t just give you one answer.
After synthesizing the rhetorical “delta,” it can **reformat the output into multiple communication styles or contexts**, including:

* Factual Summary
* Advertising Copy
* Legal Statement
* Inspirational Message
* Press Release
* Technical Report
* Social Media Post
* Policy Recommendation
* Email Draft
* Editorial Opinion
* ...or any custom format you specify!

This means you can take the **same delta** and instantly “transpose” it for a press release, marketing copy, policy doc, or even a tweet.

---

## How It Works: Under the Hood

1. **Input:** Two contrasting opinions, and a topic context.
2. **Analysis:** Each opinion is analyzed for its ethos, logos, and energeia.
3. **Ground Truth:** The tool identifies a “null hypothesis” (neutral ground truth) from which both opinions deviate.
4. **Delta Extraction:** For each rhetorical element, the qualitative difference (delta) between positive and negative inputs is articulated.
5. **Synthesis:** A new opinion is synthesized by “adding the deltas” to the neutral ground.
6. **Output Formatting:** The synthesized result can be restated in any supported output context.

---

## Usage

### Requirements

* Python 3.8+
* [openai Python package](https://pypi.org/project/openai/) (`pip install openai`)
* OpenAI API key with GPT-4 access

### Files

* **q\_opamp.py** – The main difference engine ([see source][q_opamp.py])
* **run.py** – Sample runner script for command-line use ([see source][run.py])

### Quick Start

1. **Install Dependencies:**

   ```bash
   pip install openai
   ```

2. **Get your OpenAI API Key:**
   [Get it here](https://platform.openai.com/account/api-keys) and have it ready.

3. **Run the Script:**

   ```bash
   python run.py
   ```

4. **Follow the Prompts:**

   * Enter your API key (your input is hidden for security).
   * Enter the topic context (e.g., “climate change policy”).
   * Enter two contrasting opinions (positive and negative input).
   * Select the desired output format from the menu (or specify a custom one).
   * View the analysis and result.

5. **Try More Output Contexts:**
   After your first run, the script will offer to reformat the same analysis for different output types (e.g., change from “Legal Statement” to “Press Release” without repeating the whole analysis).

6. **Save Your Results:**
   You can save all the results to a text file when prompted.

---

## Example (CLI Workflow)

For a sample step-by-step workflow and output, see [Example\_CLI\_Workflow.txt](Example_CLI_Workflow.txt) in this repository.

---

## Advanced Usage

* **Import as a Library:**
  You can also import `ConceptualOpAmp` and `select_output_type` from `q_opamp.py` in your own scripts to automate rhetorical analysis and synthesis.

---

## License

This project is licensed under the MIT License.
See [`q_opamp.py`](q_opamp.py) for full license text.

---

## Credits

Created by Edward Chalk
Contact: [edward@fleetingswallow.com](mailto:edward@fleetingswallow.com)

---

[q_opamp.py]: q_opamp.py
[run.py]: run.py

