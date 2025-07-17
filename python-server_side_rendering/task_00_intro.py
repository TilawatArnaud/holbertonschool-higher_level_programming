#!/usr/bin/env python3
"""
Task 0: Creating a Simple Templating Program
"""

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list of dictionaries
    if not (isinstance(attendees, list) and 
            all(isinstance(attendee, dict) for attendee in attendees)):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, 1):
        # Create a copy of the template for each attendee
        invitation = template
        
        # Replace each placeholder with the corresponding value or 'N/A'
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            if value is None:  # Handle None values
                value = 'N/A'
            invitation = invitation.replace(f'{{{key}}}', str(value))
        
        # Write to file
        filename = f'output_{i}.txt'
        try:
            with open(filename, 'w') as f:
                f.write(invitation)
            print(f"Generated {filename}")
        except IOError as e:
            print(f"Error writing to {filename}: {e}")


if __name__ == "__main__":
    # Example usage
    example_template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    example_attendees = [
        {"name": "Alice", "event_title": "Python Conference", 
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", 
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", 
         "event_date": None, "event_location": "Boston"}
    ]
    
    generate_invitations(example_template, example_attendees)
