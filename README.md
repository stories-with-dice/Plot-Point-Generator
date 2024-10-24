# Plot Point Generator for Adventure Crafter


This Python script allows you to roll for Adventure Crafter plot points.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Swampens/Plot-Point-Generator.git
```

2. Navigate to the project directory:

```bash
cd Plot-Point-Generator
```

## Usage


### CLI mode

1. You can provide the list of themes from the CLI

```bash
python adventure_roll.py --themes "Tension, Social, Personal, Mystery, Action"
```

This generates five plot points by default.

2. You can change the nr of Plot Points with the `--points` argument.

```bash
python adventure_roll.py --themes "Tension, Social, Personal, Mystery, Action" --points 2
```

3. You can let the program randomly assign theme priorities with `--random`

### Interactive mode

1. Run the script:

```bash
python adventure_roll.py
```

2. Follow the on-screen instructions to input theme priorities.
3. Press Enter to roll a new plot point.

## Theme Priorities

- **1:** Action
- **2:** Tension
- **3:** Mystery
- **4:** Social
- **5:** Personal

## Input Example

Example priority input:
```
Input: 2,4,5,3,1
```

```
Theme priority: Tension, Social, Personal, Mystery, Action
```
