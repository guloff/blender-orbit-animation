# Blender Orbit Animation Script

## Description

This repository contains a Python script designed to be used within **Blender** to animate the orbits of planetary objects around a central body (like the Sun). The script calculates the movement of each planet along circular orbits and generates keyframe animations over a specified number of frames.

Each planet starts with a random position on its orbit and moves at different speeds based on its distance from the central object (closer planets make more revolutions). The orbits are calculated in the XY plane, and you can customize various parameters like total frames, number of revolutions, and radius of orbits.

## Features

- **Circular Orbits**: Objects move along predefined circular paths in the XY plane.
- **Customizable Parameters**: The script automatically adjusts the number of orbits based on the distance from the central object.
- **Keyframe Animation**: Keyframes are automatically inserted for every frame of the animation, allowing smooth transitions between frames.
- **Multiple Objects**: Supports multiple planets or objects that are dynamically detected and animated.

## Requirements

- **Blender**: The script is designed to work within Blender's scripting environment.
- **Python**: Blender uses its built-in Python environment for executing this script.

## How to Use

1. **Open Blender**: Start Blender and ensure your scene contains a central object (named `"Sun"`) and multiple objects representing planets (with names starting with `"Planet"`).
   
2. **Run the Script**:
   - Open the **Scripting** tab in Blender.
   - Paste the contents of `orbit_animation.py` into the text editor or load the `.py` file directly.
   - Run the script by clicking the **Run Script** button.

3. **Animation Creation**:
   - The script automatically finds objects named "Sun" and those starting with "Planet".
   - It calculates the orbits and inserts keyframes for the animation.
   - You can adjust the total number of frames, the speed of rotation, and other parameters by modifying the script.

4. **Customize Your Scene**:
   - Add as many planet objects as you like, and the script will handle their orbits automatically.
   - Adjust the positions and scaling of the planets before running the script to achieve the desired orbital effect.

## Script Parameters

- **Total Frames**: The number of frames over which the animation will take place (default is `250` frames).
- **Max Orbits**: The maximum number of revolutions for the closest planet (default is `3.0`).
- **Min Orbits**: The minimum number of revolutions for the farthest planet (default is `0.5`).

### Example Code

```python
total_frames = 250
max_orbits = 3.0
min_orbits = 0.5
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This script was developed to facilitate the creation of orbital animations in Blender, making it easier to animate complex systems such as solar systems or other rotating objects.
