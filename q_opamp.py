# MIT License
# 
# Copyright (c) 2025 Edward Chalk (edward@fleetingswallow.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import openai
from dataclasses import dataclass
from typing import Dict, Any, Tuple
import json

# ---------------------- Data Structures and Output Format Selection ----------------------

@dataclass
class RhetoricalAnalysis:
    """Represents the rhetorical analysis of an opinion"""
    ethos: str
    logos: str
    energeia: str
    content: str

# Menu of supported output types (add or adjust as needed)
OUTPUT_TYPES = {
    1: "Factual Summary",
    2: "Advertising Copy",
    3: "Legal Statement",
    4: "Inspirational Message",
    5: "Press Release",
    6: "Technical Report",
    7: "Social Media Post",
    8: "Policy Recommendation",
    9: "Email Draft",
    10: "Editorial Opinion",
    11: "Other (Custom)"
}

# Prompts for fixed output types (1-10)
FINAL_OUTPUT_PROMPTS = {
    "Factual Summary": (
        "Rewrite the synthesis as a concise, objective summary. "
        "Use clear bullet points or a short paragraph to present the key findings and differences. "
        "Avoid persuasive or emotional language; focus only on the facts and logical distinctions."
    ),
    "Advertising Copy": (
        "Transform the synthesis into a compelling advertising message that would engage potential customers. "
        "Use persuasive, energetic language and focus on benefits. "
        "Aim for a catchy, memorable, and motivating style."
    ),
    "Legal Statement": (
        "Rewrite the synthesis as a formal legal statement suitable for a policy document or contract. "
        "Use precise, unambiguous language. "
        "Avoid emotion and ensure clarity, neutrality, and legal formality."
    ),
    "Inspirational Message": (
        "Turn the synthesis into an uplifting, inspirational message that encourages positive action or mindset. "
        "Use motivational, affirmative language, and focus on empowerment and hope."
    ),
    "Press Release": (
        "Rewrite the synthesis as an official press release for immediate publication. "
        "Use a formal, newsworthy tone. "
        "Include a headline and clear opening paragraph summarizing the main point, followed by supporting details."
    ),
    "Technical Report": (
        "Present the synthesis as a section of a technical report. "
        "Use precise, analytical language suitable for an expert audience. "
        "Break down findings into clear, numbered or bulleted points."
    ),
    "Social Media Post": (
        "Condense the synthesis into a short, engaging social media post suitable for platforms like Twitter or LinkedIn. "
        "Keep it concise, direct, and attention-grabbing. "
        "Use hashtags or emojis only if appropriate."
    ),
    "Policy Recommendation": (
        "Rewrite the synthesis as a set of clear policy recommendations. "
        "Present actionable suggestions with concise justifications. "
        "Use formal, directive language suited for policymakers."
    ),
    "Email Draft": (
        "Transform the synthesis into the body of a professional email draft. "
        "Use a polite, direct tone and clearly outline the main points for the recipient. "
        "Close with a courteous call to action."
    ),
    "Editorial Opinion": (
        "Rewrite the synthesis as an editorial opinion piece for a major publication. "
        "Use persuasive, articulate language and a clear personal or institutional viewpoint. "
        "Support arguments with logic and vivid examples."
    )
}

def select_output_type():
    """
    Presents a menu for the user to select the output format.
    Returns (output_type, is_custom)
    """
    print("Select desired output format:")
    for num, desc in OUTPUT_TYPES.items():
        print(f"{num}. {desc}")
    while True:
        try:
            choice = int(input("Enter the number corresponding to the output type: "))
            if 1 <= choice <= 11:
                if choice == 11:
                    custom_type = input("Enter your custom output type/format: ").strip()
                    return custom_type, True
                else:
                    return OUTPUT_TYPES[choice], False
        except ValueError:
            pass
        print("Invalid input. Try again.")

# ---------------------- Main Class: ConceptualOpAmp ----------------------
class ConceptualOpAmp:
    """
    A conceptual op-amp modeled as a difference engine for rhetorical opinion analysis—
    focusing on extracting, analyzing, and synthesizing qualitative differences (deltas)
    in ethos, logos, and energeia between contrasting viewpoints.
    """
    def __init__(self, api_key: str, system_context: str = "general discussion"):
        """
        Initialize the conceptual op-amp (difference engine).
        Args:
            api_key: OpenAI API key
            system_context: Context for the opinions being analyzed
        """
        self.client = openai.OpenAI(api_key=api_key)
        self.system_context = system_context

    def _analyze_opinion(self, opinion: str) -> RhetoricalAnalysis:
        """
        Qualitatively analyze an opinion for ethos, logos, and energeia.
        """
        prompt = f"""
        Analyze the following opinion in the context of "{self.system_context}" for:

        1. ETHOS (credibility/authority): Briefly describe how this opinion demonstrates credibility and authority.
        2. LOGOS (logical reasoning): Briefly describe how logical and well-reasoned this opinion is.
        3. ENERGEIA (vivid impact): Briefly describe the vivid energy and transformative potential this opinion expresses.

        Opinion: "{opinion}"

        Return your analysis as a JSON object with keys: ethos, logos, energeia (each as a short text description).
        """
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        try:
            analysis = json.loads(response.choices[0].message.content)
            return RhetoricalAnalysis(
                ethos=analysis.get('ethos', ''),
                logos=analysis.get('logos', ''),
                energeia=analysis.get('energeia', ''),
                content=opinion
            )
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            print(f"Error parsing AI response: {e}")
            return RhetoricalAnalysis('', '', '', opinion)

    def _find_ground_truth(self, opinion1: str, opinion2: str) -> str:
        """
        Identify a neutral, baseline ground truth (null hypothesis) from which both opinions deviate.
        """
        prompt = f"""
        Given these two opinions about "{self.system_context}", formulate a NULL HYPOTHESIS that represents the neutral ground truth from which both opinions deviate.
        
        Positive Input Opinion: "{opinion1}"
        Negative Input Opinion: "{opinion2}"
        
        The null hypothesis should be a neutral, baseline statement that neither strongly supports nor opposes either opinion, but from which both can be measured as deviations.
        
        Return only the null hypothesis statement.
        """
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    def _assign_polarity(self, analysis1: RhetoricalAnalysis, analysis2: RhetoricalAnalysis) -> Tuple[RhetoricalAnalysis, RhetoricalAnalysis]:
        """
        Assigns input polarity: the first opinion is treated as positive (+), the second as negative (–).
        """
        return analysis1, analysis2

    def _analyze_rhetorical_delta(self, element: str, positive_analysis: RhetoricalAnalysis, negative_analysis: RhetoricalAnalysis) -> dict:
        """
        Analyze and articulate the qualitative difference (delta) for a rhetorical element between two opinions.
        """
        element_definitions = {
            'ethos': {
                'definition': 'credibility, authority, and trustworthiness',
                'focus': 'How does each opinion establish credibility? What sources of authority do they invoke? How do they build trust with their audience?',
                'examples': 'expertise claims, institutional authority, moral authority, experiential credibility, traditional vs. innovative authority'
            },
            'logos': {
                'definition': 'logical reasoning, evidence, and rational argumentation',
                'focus': 'What logical structure does each opinion use? What evidence or reasoning patterns do they employ? How do they construct their rational arguments?',
                'examples': 'cause-and-effect reasoning, empirical evidence, logical fallacies, deductive vs. inductive reasoning, evidence types'
            },
            'energeia': {
                'definition': 'vivid impact, emotional energy, and transformative potential',
                'focus': 'What emotional energy does each opinion generate? How vivid and impactful is their presentation? What transformative potential do they convey?',
                'examples': 'emotional intensity, vivid imagery, urgency, inspirational power, transformative vision'
            }
        }
        element_info = element_definitions[element]

        null_hypothesis_prompt = f"""
        For the rhetorical element "{element.upper()}" ({element_info['definition']}) in the context of "{self.system_context}", 
        identify the NULL HYPOTHESIS that represents the baseline state.

        FOCUS SPECIFICALLY ON {element.upper()}: {element_info['focus']}

        Positive Input {element}: "{getattr(positive_analysis, element)}" (Opinion: "{positive_analysis.content}")
        Negative Input {element}: "{getattr(negative_analysis, element)}" (Opinion: "{negative_analysis.content}")

        What is the neutral baseline {element} state from which both opinions deviate?
        Focus ONLY on the {element_info['definition']} aspects, not the overall content.

        Return only the {element} null hypothesis statement.
        """
        element_null = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": null_hypothesis_prompt}],
            temperature=0.3
        ).choices[0].message.content.strip()

        delta_prompt = f"""
        Compare ONLY the {element.upper()} in the context of "{self.system_context}":

        {element.upper()} DEFINITION: {element_info['definition']}
        ANALYSIS FOCUS: {element_info['focus']}
        EXAMPLES TO CONSIDER: {element_info['examples']}

        ELEMENT NULL HYPOTHESIS: {element_null}

        POSITIVE INPUT — This is the POSITIVE side of the argument:
        Description: "{getattr(positive_analysis, element)}"
        Opinion: "{positive_analysis.content}"

        NEGATIVE INPUT — This is the NEGATIVE side of the argument:
        Description: "{getattr(negative_analysis, element)}"
        Opinion: "{negative_analysis.content}"

        INSTRUCTIONS:
        1. Focus EXCLUSIVELY on {element_info['definition']}—ignore other rhetorical aspects.
        2. ALWAYS treat the first input as the POSITIVE side of the {element.upper()} comparison.
        3. ALWAYS treat the second input as the NEGATIVE side of the {element.upper()} comparison.
        4. Analyze how each opinion's {element.upper()} approach differs from the null hypothesis.
        5. Describe the directional {element.upper()} difference from negative to positive input.
        6. DO NOT discuss the overall content—focus only on the {element.upper()} rhetorical dimension.

        What specific {element.upper()} difference does the positive input represent that the negative input lacks?
        How do their {element_info['definition']} strategies differ, with the positive input being the affirming side?
        """

        delta_analysis = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": delta_prompt}],
            temperature=0.3
        ).choices[0].message.content.strip()

        return {
            'element': element,
            'null_hypothesis': element_null,
            'positive_input': positive_analysis.content,
            'negative_input': negative_analysis.content,
            'positive_description': getattr(positive_analysis, element),
            'negative_description': getattr(negative_analysis, element),
            'delta_analysis': delta_analysis
        }

    def _calculate_deltas(self, positive_input: RhetoricalAnalysis, negative_input: RhetoricalAnalysis) -> dict:
        """
        Calculate qualitative differences (deltas) in ethos, logos, and energeia between the two inputs.
        """
        return {
            'ethos': self._analyze_rhetorical_delta('ethos', positive_input, negative_input),
            'logos': self._analyze_rhetorical_delta('logos', positive_input, negative_input),
            'energeia': self._analyze_rhetorical_delta('energeia', positive_input, negative_input)
        }

    def _synthesize_output(self, deltas: Dict[str, Dict[str, str]], positive_input: RhetoricalAnalysis,
                          negative_input: RhetoricalAnalysis, ground_truth: str) -> str:
        """
        Synthesize a new, differentiated opinion based strictly on the pure delta outputs.
        """
        prompt = f"""
        You are a conceptual op-amp (difference engine) synthesizing a NEW opinion by applying the qualitative differences identified.

        CONTEXT: {self.system_context}
        BASELINE: {ground_truth}

        DELTA COMPARISONS:
        
        ETHOS DELTA: {deltas['ethos']['delta_analysis']}
        LOGOS DELTA: {deltas['logos']['delta_analysis']}
        ENERGEIA DELTA: {deltas['energeia']['delta_analysis']}

        SYNTHESIS INSTRUCTIONS:
        1. START with the baseline as your foundation.
        2. APPLY each delta transformation.
        3. Synthesize a NEW opinion that embodies these differences.
        4. The result should combine the deltas into a coherent, integrated perspective.
        5. Create something new and comparative—do not reference or copy any single source material.

        Create the synthesized opinion:
        """
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message.content.strip()

    def _resynthesize_output(self, first_synthesis: str, deltas: Dict[str, Dict[str, str]], ground_truth: str, output_type: str, is_custom: bool) -> str:
        """
        Rephrase the synthesis into the desired output type.
        If the output type is custom (Other), generate the prompt dynamically using meta-prompting.
        Otherwise, use a predefined prompt.
        """
        if is_custom:
            # Dynamically generate prompt via meta-prompting
            meta_prompt = (
                f"You are to rephrase a synthesized opinion into the following output format: {output_type}. "
                "Write clear and direct instructions to another AI about how to transform a complex analytical synthesis "
                "into that style/format. Be specific about structure, tone, length, and audience as appropriate. "
                "Output only the instructions, not the rephrased content."
            )
            instructions = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": meta_prompt}],
                temperature=0.3
            ).choices[0].message.content.strip()
            prompt = (
                f"{instructions}\n\n"
                f"SYNTHESIS TO REWRITE:\n\"{first_synthesis}\"\n\n"
                "Provide the output as requested above:"
            )
        else:
            rephrase_instructions = FINAL_OUTPUT_PROMPTS[output_type]
            prompt = (
                f"{rephrase_instructions}\n\n"
                f"SYNTHESIS TO REWRITE:\n\"{first_synthesis}\"\n\n"
                "Provide the output as requested above:"
            )
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()


    def differentiate(self, opinion1: str, opinion2: str, output_type: str, is_custom: bool) -> dict:
        """
        Main function—processes two opinions through the difference engine.
        Returns a dictionary containing the complete analysis and synthesized output.
        """
        print("Starting analysis of input opinions...")
    
        # Step 1: Analyze both opinions
        print("Step 1: Analyzing the first opinion (positive input)...")
        analysis1 = self._analyze_opinion(opinion1)
        print("Step 1: Analyzing the second opinion (negative input)...")
        analysis2 = self._analyze_opinion(opinion2)
    
        # Step 2: Find ground truth (null hypothesis)
        print("Step 2: Determining the neutral ground truth...")
        ground_truth = self._find_ground_truth(opinion1, opinion2)
        print(f"Ground truth identified: {ground_truth}\n")
    
        # Step 3: Assign polarity based on input order (opinion1 = +, opinion2 = -)
        print("Step 3: Assigning polarity to opinions...")
        positive_input, negative_input = self._assign_polarity(analysis1, analysis2)
        print("Polarity assigned.\n")
    
        # Step 4: Calculate qualitative deltas for each element
        print("Step 4: Calculating rhetorical differences (deltas)...")
        deltas = self._calculate_deltas(positive_input, negative_input)
        print("Deltas calculated for ethos, logos, and energeia.\n")
    
        # Step 5: Synthesize output (first stage)
        print("Step 5: Synthesizing the differentiated output...")
        first_synthesis = self._synthesize_output(deltas, positive_input, negative_input, ground_truth)
        print("Initial synthesis complete.\n")
    
        # Step 6: Final output in desired format
        print(f"Step 6: Creating the {output_type} output...")
        final_output = self._resynthesize_output(first_synthesis, deltas, ground_truth, output_type, is_custom)
        print("Final output complete.\n")
    
        return {
            'ground_truth': ground_truth,
            'positive_input': {
                'content': positive_input.content,
                'ethos': positive_input.ethos,
                'logos': positive_input.logos,
                'energeia': positive_input.energeia
            },
            'negative_input': {
                'content': negative_input.content,
                'ethos': negative_input.ethos,
                'logos': negative_input.logos,
                'energeia': negative_input.energeia
            },
            'deltas': deltas,
            'first_synthesis': first_synthesis,
            'final_output': final_output
        }
    


# Example usage
if __name__ == "__main__":
    # Initialize the op-amp (add your OpenAI API key)
    # opamp = ConceptualOpAmp("your-api-key-here", "climate change policy")
    
    # Example opinions
    opinion1 = "We should immediately transition to 100% renewable energy regardless of economic costs to save the planet."
    opinion2 = "We should prioritize economic stability and gradually transition to cleaner energy over the next 50 years."
    
    # Output type selection
    output_type, is_custom = select_output_type()
    
    # Process through the op-amp
    # result = opamp.differentiate(opinion1, opinion2, output_type, is_custom)
    
    # Print results
    # print("Ground Truth:", result['ground_truth'])
    # print(f"\n--- Final Output ({output_type}) ---\n")
    # print(result['final_output'])
    
    print("OpAmp initialized. Uncomment the usage section and add your API key to run.")

