# waverider-generator
**IMPORTANT: Main Modules are Under /src file**

 Outputs a cone-derived waverider from given basic flowfield information and user-defined trailing edge. Main modules including solving Taylor-Maccoll equation and streamline tracing to form the lower surface

 User can specify their UDF (User Defined Function) for the TE (Trailing Edge). 
 
 The program gives a visualization of:
 1. Diagram of the base cone, conical shock and user-defined trailing edge at the base plane.
 2. 3D wireframe of the resulting cone-derived waverider

 The program gives outputs of .txt files for modelling in CAD software, enable this function in the output module of main.py
 
 Theory Guide and User Menu will be uploaded shortly under /doc file
 
 <img src="https://github.com/ExusiaiVAL/Waverider-Generator/blob/main/Images/Programme%20Example%20Output%20Image.PNG" alt="Programme Example Output Image" width="300"/> <img src="https://github.com/ExusiaiVAL/Waverider-Generator/blob/main/Images/CAE%20Visualization.PNG" alt="CAE Visualization" width="350"/>

**Left:** Output Wireframe View of Calculated Waverider from Python Programme; **Right:** View in Solidworks After Importing the Output Curves from this Programme

 <img src="https://github.com/ExusiaiVAL/Waverider-Generator/blob/main/Images/Programme%20Output%20CAE.png" alt="Programme Example Output Image" width="300"/>
 **Figure:** Example Output Format for CAE Platforms (Solidworks, CATIA...). Specifies a Resolution = 12 Results in 12*2 .txt Files, Each Containing a Traced Streamline that Formed the Lower Surface, Plus 3 Curves Specifing the Leading, Trailing Edge and Lower Surface Baseine
