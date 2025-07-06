#!/usr/bin/env python3
"""
Opinion OpAmp Runner
A simple interface to run the conceptual operational amplifier for opinion analysis
"""

import sys
from getpass import getpass

# Import the q-opamp module and select_output_type function
try:
    import q_opamp
    from q_opamp import ConceptualOpAmp, select_output_type
except ImportError as e:
    print(f"❌ Error importing q_opamp9.py: {e}")
    print("Make sure q_opamp9.py is in the same directory as this script")
    sys.exit(1)

def get_user_input():
    """Get user inputs for the opinion analysis"""
    print("**Conceptual OpAmp Difference Engine**")
    print("=" * 50)
    
    # Get API key
    api_key = getpass("Enter your OpenAI API key: ")
    if not api_key.strip():
        print("❌ API key is required")
        sys.exit(1)
    
    # Get system context
    print("\n📋 System Context")
    context = input("Enter the discussion context/topic (e.g., 'climate change policy', 'education reform'): ").strip()
    if not context:
        context = "general discussion"
    
    # Get first opinion (positive input)
    print("\n💭 First Opinion (Positive Input)")
    print("Enter the first opinion (press Enter twice when done):")
    opinion1_lines = []
    while True:
        line = input()
        if line == "" and opinion1_lines:
            break
        opinion1_lines.append(line)
    opinion1 = "\n".join(opinion1_lines).strip()
    if not opinion1:
        print("❌ First opinion cannot be empty")
        sys.exit(1)
    
    # Get second opinion (negative input)
    print("\n💭 Second Opinion (Negative Input)")
    print("Enter the second opinion (press Enter twice when done):")
    opinion2_lines = []
    while True:
        line = input()
        if line == "" and opinion2_lines:
            break
        opinion2_lines.append(line)
    opinion2 = "\n".join(opinion2_lines).strip()
    if not opinion2:
        print("❌ Second opinion cannot be empty")
        sys.exit(1)
    
    return api_key, context, opinion1, opinion2

def display_results(result, final_outputs):
    """Display the op-amp analysis results in a formatted way"""
    print("\n" + "="*70)
    print("🎯 CONCEPTUAL OP-AMP ANALYSIS RESULTS")
    print("="*70)
    
    # Ground Truth
    print("\n⚖️  GROUND TRUTH (NULL HYPOTHESIS):")
    print("-" * 40)
    print(f"{result['ground_truth']}")
    
    # Input Analysis
    print("\n📊 INPUT ANALYSIS:")
    print("-" * 40)
    print(f"\n➕ POSITIVE INPUT (Opinion 1):")
    print(f"   Content: {result['positive_input']['content']}")
    print(f"   Ethos:    {result['positive_input']['ethos']}")
    print(f"   Logos:    {result['positive_input']['logos']}")
    print(f"   Energeia: {result['positive_input']['energeia']}")
    print(f"\n➖ NEGATIVE INPUT (Opinion 2):")
    print(f"   Content: {result['negative_input']['content']}")
    print(f"   Ethos:    {result['negative_input']['ethos']}")
    print(f"   Logos:    {result['negative_input']['logos']}")
    print(f"   Energeia: {result['negative_input']['energeia']}")
    print(f"\n📈 RHETORICAL DELTAS:")
    print("-" * 40)
    print(f"\n🎭 ETHOS DELTA:")
    print(f"   Null Hypothesis: {result['deltas']['ethos']['null_hypothesis']}")
    print(f"   Analysis: {result['deltas']['ethos']['delta_analysis']}")
    print(f"\n🧠 LOGOS DELTA:")
    print(f"   Null Hypothesis: {result['deltas']['logos']['null_hypothesis']}")
    print(f"   Analysis: {result['deltas']['logos']['delta_analysis']}")
    print(f"\n⚡ ENERGEIA DELTA:")
    print(f"   Null Hypothesis: {result['deltas']['energeia']['null_hypothesis']}")
    print(f"   Analysis: {result['deltas']['energeia']['delta_analysis']}")
    print(f"\n🔬 FIRST SYNTHESIS (DELTA SYNTHESIS):")
    print("-" * 40)
    print(f"{result['first_synthesis']}")
    print("\n" + "="*70)
    
    # Display all final outputs generated
    for idx, (out_type, out_text) in enumerate(final_outputs):
        print(f"\n🎭 FINAL OUTPUT ({out_type}):")
        print("-" * 40)
        print(f"{out_text}")
        print("\n" + "="*70)

def main():
    """Main function to run the opinion amplifier"""
    try:
        # Get user inputs
        api_key, context, opinion1, opinion2 = get_user_input()
        
        # Output type selection
        output_type, is_custom = select_output_type()
        
        # Initialize the op-amp
        print(f"\n🔧 Initializing Opinion OpAmp with context: '{context}'")
        opamp = ConceptualOpAmp(api_key, context)
        
        # Process the opinions (full workflow)
        print("\n🚀 Processing opinions through the conceptual op-amp...")
        print("This may take a moment as we analyze the rhetorical components...")
        result = opamp.differentiate(opinion1, opinion2, output_type, is_custom)
        # Store all reformattings
        final_outputs = [(output_type, result['final_output'])]
        
        # Show all output (full analysis, deltas, first output)
        display_results(result, final_outputs)
        
        # Now ask if the user wants another context, only display new output
        while True:
            more_context = input("\n🌀 Would you like the output in a different context/format? (y/n): ").strip().lower()
            if more_context not in ['y', 'yes']:
                break
            # User selects new output type
            new_output_type, new_is_custom = select_output_type()
            # Use only the first_synthesis for further restatement!
            new_final = opamp._resynthesize_output(
                result['first_synthesis'],
                result['deltas'],
                result['ground_truth'],
                new_output_type,
                new_is_custom
            )
            final_outputs.append((new_output_type, new_final))
            print(f"\n🎭 FINAL OUTPUT ({new_output_type}):")
            print("-" * 40)
            print(f"{new_final}")
            print("\n" + "="*70)
        
        # Ask if user wants to save results
        save_choice = input("\n💾 Would you like to save these results to a file? (y/n): ").lower()
        if save_choice in ['y', 'yes']:
            filename = input("Enter filename (without extension): ").strip()
            if not filename:
                filename = "opamp_results"
            with open(f"{filename}.txt", "w", encoding="utf-8") as f:
                f.write("CONCEPTUAL OP-AMP ANALYSIS RESULTS\n")
                f.write("="*50 + "\n\n")
                f.write(f"Context: {context}\n\n")
                f.write(f"Ground Truth: {result['ground_truth']}\n\n")
                f.write(f"Positive Input (Opinion 1): {result['positive_input']['content']}\n")
                f.write(f"Ethos: {result['positive_input']['ethos']}, ")
                f.write(f"Logos: {result['positive_input']['logos']}, ")
                f.write(f"Energeia: {result['positive_input']['energeia']}\n\n")
                f.write(f"Negative Input (Opinion 2): {result['negative_input']['content']}\n")
                f.write(f"Ethos: {result['negative_input']['ethos']}, ")
                f.write(f"Logos: {result['negative_input']['logos']}, ")
                f.write(f"Energeia: {result['negative_input']['energeia']}\n\n")
                f.write(f"Ethos Delta:\n")
                f.write(f"  Null: {result['deltas']['ethos']['null_hypothesis']}\n")
                f.write(f"  Analysis: {result['deltas']['ethos']['delta_analysis']}\n\n")
                f.write(f"Logos Delta:\n")
                f.write(f"  Null: {result['deltas']['logos']['null_hypothesis']}\n")
                f.write(f"  Analysis: {result['deltas']['logos']['delta_analysis']}\n\n")
                f.write(f"Energeia Delta:\n")
                f.write(f"  Null: {result['deltas']['energeia']['null_hypothesis']}\n")
                f.write(f"  Analysis: {result['deltas']['energeia']['delta_analysis']}\n\n")
                f.write(f"First Synthesis (Delta Synthesis):\n{result['first_synthesis']}\n\n")
                for out_type, out_text in final_outputs:
                    f.write(f"Final Output ({out_type}):\n{out_text}\n\n")
            print(f"✅ Results saved to {filename}.txt")
    
    except KeyboardInterrupt:
        print("\n\n👋 Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check your API key and try again")
        sys.exit(1)

if __name__ == "__main__":
    main()
