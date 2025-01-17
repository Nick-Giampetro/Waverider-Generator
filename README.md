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

Computational Results From ANSYS Fluent:

Ma = 8.0, Altitude = 25km, Viscous Flowfield

 <img src="https://github.com/ExusiaiVAL/Waverider-Generator/blob/main/Images/ANSYS%20Result%206.png" alt="Programme Example Output Image" width="350"/> <img src="https://github.com/ExusiaiVAL/Waverider-Generator/blob/main/Images/ANSYS%20Result%207.png" alt="Programme Example Output Image" width="350"/>

 **Figure 1&2:** Pressure Contour Lines

  <img src="https://github.com/ExusiaiVAL/Waverider-Generator/blob/main/Images/ANSYS%20Result%202.png" alt="Programme Example Output Image" width="350"/> <img src="https://github.com/ExusiaiVAL/Waverider-Generator/blob/main/Images/ANSYS%20Result%203.png" alt="Programme Example Output Image" width="350"/>

 **Figure 2&3:** Pressure Contour at the Symmetry and the Base Plane

High pressure zone is firmly constrained at the lower surface

 NOTE: There exists negative pressure due to the reference value given to Fluent is below the operating (absolute) pressure. This does not affect the solution for the fields, but only affects the numerical values displayed at post-processing (all pressure values in the field are reduced by a same amount). This minor issue will be fixed when I have time to do a re-computation :)

 
