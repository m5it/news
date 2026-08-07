# AIIA Model Recovered from Context Cutoff Using ReplaceLine

## What Happened

We gave the model a follow-up task:

> **Update the 4-in-line game so it has an option to play against AI.**

The model:
1. 📝 Prepared a plan
2. 🛠️ Started editing the file
3. ⚠️ Hit a **context size problem** — the `WriteFile` tool output was cut at around 70%
4. 🧠 **Recovered on its own** using `ReplaceLine` to add the missing content
5. ✅ **Finished the plan successfully**

## The Problem

During the edit, the context filled up:

```text
[after +1901] [Context: 27763/32768 (84.7%)]
[iter 9] [Context: 6432/32768 (19.6%)]
```

The framework automatically cleared context, but the previous `WriteFile` had already been truncated. The file ended up with a broken section like this:

```python
    while True:                                                                                                                                                   
        if is_single_player:                                                                                                                                      
            # AI move in single-player mode                                                                                                                       
            print(f"\nAI thinking...")                                                                                                                            
            ai_move = get_ai_move()                                                                                                                               
            col = ai_move                                                                                                                                         
4
```

That dangling `4` is a clear sign the file write was interrupted.

## The Fix

The model recognized the syntax error and used `ReplaceLine` to replace the broken block with a corrected version:

```xml
<ReplaceLine>
  <fileName>four_in_line.py</fileName>
  <fromLine>210</fromLine>
  <toLine>260</toLine>
  <replacement>
def main():
    """Main game loop."""
    current_player = PLAYER_X
    ...
  </replacement>
</ReplaceLine>
```

After this fix, the code was complete and functional.

## Why This Is Amazing

| Capability | Demonstrated |
|------------|--------------|
| **Planning** | ✅ Prepared a plan before coding |
| **Tool use** | ✅ Used `WriteFile` and `ReplaceLine` |
| **Self-recovery** | ✅ Detected a context-truncation bug and fixed it |
| **Error correction** | ✅ Found the syntax error and repaired it |
| **Context management** | ✅ Continued working after context was cleared |

## The Bigger Picture

This is exactly the kind of behavior AIIA Framework is being trained for:

- 🧠 **Models that do not just execute commands, but adapt when things go wrong.**
- 🔄 **Models that can recover from tool failures and context limits.**
- 🎯 **Models that finish the job even when the environment fights back.**

## Key Insight

> **A model that can recover from its own partial failure is more valuable than a model that only works in perfect conditions.** The 4-in-line game now has an AI opponent — but the real win is that the model fixed itself mid-task.

## See Also

- [Our Model Created a 4-in-Line Game](../README.md)
- [AIIA Framework: New `!REHEAT` Command](aiia_reheat_command_added.md)
- [Conditional Thinking: System Prompt as a Switch](conditional_thinking_based_on_system_prompt.md)
