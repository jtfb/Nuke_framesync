import nuke

def refresh_frame_range():
    # Get the selected nodes
    selected_nodes = nuke.selectedNodes()
    
    if not selected_nodes:
        nuke.message("No node selected. Please select a Read node.")
        return
    
    # Loop through selected nodes
    for node in selected_nodes:
        # Check if the node is a Read node
        if node.Class() == "Read":
            # Get the first and last frame from the Read node
            first_frame = int(node['first'].getValue())
            last_frame = int(node['last'].getValue())
            
            # Set the Nuke timeline to match the frame range of the selected node
            nuke.root()['first_frame'].setValue(first_frame)
            nuke.root()['last_frame'].setValue(last_frame)
            
            # Optionally, set the current frame to the first frame of the range
            nuke.frame(first_frame)
            
            nuke.message("Frame range updated to match the selected Read node.")
            return
    
    nuke.message("Selected node is not a Read node. Please select a Read node.")

# Run the function
refresh_frame_range()
