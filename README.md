# FrameSync Tool for Nuke

**FrameSync** is a tool designed to automatically refresh the frame range in Nuke based on the selected shot. This script simplifies the process of adjusting frame ranges for EXR sequences, ensuring your project is always in sync with the footage.

## Features

- **Auto-Refresh Frame Range**: Automatically adjusts the frame range in Nuke based on the selected shot.
- **Simple Integration**: Easy to integrate into your existing Nuke workflow.
- **User-Friendly**: Designed to be intuitive and straightforward to use.

## Installation - option 1

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/nuke_framesync.git
2. Add the Script to Nuke: Copy the framesync.py script to your Nuke plugin path. You can find your Nuke plugin path in Nuke's preferences under the "User" tab.

3. Update Nuke Menu: Add the following line to your menu.py to create a menu item for the FrameSync tool:

```bash
  import framesync
  framesync.add_menu()
```
## Installation - option 2

1. Open Nuke and load your project.

2. Open the Script Editor:

3. Go to Script Editor in the Nuke interface.
Paste the Script:

4. Copy and paste the provided script into the Script Editor.
Run the Script:

5. Select the Read node you want to use as the basis for your frame range.
Run the script by clicking the Execute button in the Script Editor or pressing Ctrl+Enter (Windows) / Cmd+Enter (Mac).

## Usage
1. Open Nuke and select the shot you want to adjust.
2. Navigate to the FrameSync menu item and click "Refresh Frame Range".
3. The script will automatically update the frame range based on the selected shot's frame range.

## Example
If your selected shot has a frame range of 1001 to 1100, FrameSync will update your current Nuke script to reflect this range.
