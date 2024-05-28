# Integrating ChatGPT with Excel using API

## Introduction
In this lecture, we will integrate ChatGPT within Excel using an API key. By integrating ChatGPT into Excel, we can use its natural language processing capabilities within our spreadsheet. This allows us to automate complex tasks, generate text-based reports, and even create interactive chat-based interfaces within our spreadsheets.

## Integration Steps

### 1. Preparing Excel
1. **Open Excel and Locate Developer Tab**:
   - If the Developer tab is not visible, add it by right-clicking on the ribbon, selecting "Customize Ribbon," and ensuring the Developer checkbox is checked.

### 2. Opening Visual Basic Editor
1. **Open the Visual Basic Editor**:
   - Click on the Developer tab and then on the "Visual Basic" button.
   - In the VBA editor, open the Project Explorer, expand Microsoft Excel Objects, and select your sheet name.

### 3. Writing VBA Code
1. **Input API Key and Script**:
   - Retrieve your API key from OpenAI by signing in to your OpenAI account, navigating to the dashboard, and generating a new API key.
   - In the VBA editor, input your API key at the top section of the script.

### 4. Assigning Macro to Quick Access Toolbar
1. **Add Macro to Quick Access Toolbar**:
   - Click the arrow icon on the top left corner of Excel, select "More Commands," choose Macros from the left sidebar, and add the macro to the Quick Access Toolbar.

2. **Modify Button Icon (Optional)**:
   - Optionally, you can modify the button icon to your preference.

### 5. Adding Macro Button
1. **Add a Macro Button**:
   - Go to the Developer tab, select "Insert," choose a shape, draw the shape on the screen, and assign the macro to the shape.

### 6. Saving Changes
1. **Save Changes**:
   - When closing the workbook, save the changes to the personal workbook to ensure the codes remain available in all your Excel files.

## Demonstrating ChatGPT Integration
1. **Using ChatGPT for SUM Formula**:
   - Input the prompt "Can you provide an example of the SUM formula?"
   - Execute the macro and see the generated completion in the Excel sheet.

2. **Using ChatGPT for COUNT Formula**:
   - Input the prompt "Could you show me an instance of the COUNT function?"
   - Execute the macro and see the generated completion in the Excel sheet.

## Code Explanation
1. **Module and Functions**:
   - The code contains functions and subroutines for communicating with the ChatGPT API and fetching text responses.
   - **API Endpoint**: The URL of the OpenAI API.
   - **Model**: The name of the pre-trained language model used to generate responses.
   - **Max Tokens**: The maximum number of words to generate.
   - **Temperature**: Controls the creativity of responses.
   - **Regenerate Completion**: Clears the previous output and regenerates a new response.
   - **Add Regenerate Button**: Adds a regenerate button to the Excel sheet.
   - **Parse Response**: Extracts the generated response from the API's response text.

## Example: Using AVERAGE Formula
1. **Prompt for AVERAGE Formula**:
   - Input the prompt "Can you provide us an example of the AVERAGE formula?"
   - Execute the macro and see the generated response in the Excel sheet.

## Conclusion
You have successfully integrated ChatGPT into Excel using VBA macros. This integration opens up a whole new world of possibilities for enhancing your Excel functionalities with natural language processing capabilities.
