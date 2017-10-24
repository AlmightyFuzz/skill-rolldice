# skill-rolldice
Simple opsdroid skill to roll dice

Allows you to roll any number of n sided dice and add a modifier.

# Requirements
None

# Configuration
```
- name: roll-dice
  repo: https://github.com/AlmightyFuzz/skill-rolldice.git
```

# Usage
Just type roll and then the number of dice followed by the dice type and any modifier.

The command takes the form:
`roll [n]d<n>[+n]`
Where `[]` indicates an optional field, `<>` a required input and n represents an integer.

eg: `roll d4` `roll 5d6` `roll 2d8+2`
