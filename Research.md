---
layout: default
title: Research
permalink: /research/
---
# Research

Currently, I work with Dr. Rogier Windhorst's cosmology research group at ASU. Though, I have also worked on research in planetary science and astrobiology, both of which I am interested in building upon as future projects. This page includes discriptions, thought processes/work flows, and data/figures for various research projects I have worked on, both formal research and research adjacent class projects. If you are interested in any of this work and want more details or have questions, please email me at semmons3@asu.edu

## Galaxies and Cosmology

### Galactic Star Formation and Quenching (2025-present)

This is my current project. It had had quite a bit of a learning curve as I was not particularly familiar with the methods - very much a "I know those words individually, but not together" kind of situation. That being said, I have Learned a lot and am making progress on the project. 

For this project, I am using the Python package PySersic to fit a sample of several hundred galaxies from JWST images. This is being done for each galaxy twice - once using a multi-band fit of 8 NIRCam filters and again using a single-band fit of H-α maps from NIRISS. The resulting outputs, primarily the Sérsic index and effective radius, can then be compared between the two sets to determine where in the galaxies star formation is still happening and where it has stopped. 

So far, there are no results, but that will hopefully change on the coming weeks. 

## Planetary Science

### PsycheESE (2025-2026)

This project started as the capstone for my astrophysics major (still a year before graduating due to my physics minor and planetary science certificate). Despite that, it is the first (and currently only) research I have done that is published in some way, in this case as an iPoster at the American Astronomical Society 248th meeting in June 2026. A link to the poster can be found <a href="https://aas242-aas.ipostersessions.com/?s=1B-39-73-D9-63-59-E7-2E-81-46-EB-7A-F9-7D-0F-33" target="_blank">here</a> and a GutHub repository with a guide to replicate our methodology, example files, and pdfs of our class presentations and report is <a href="https://github.com/semmons98/PsycheESE" target="_blank">here</a>.

The project lasted 2 semesters, the first was dedicated to conceptualization, study, and planning. For this, the class somewhat followed the process used for projects at NASA and similar organizations - with each group writing and presenting an SRR, PDR, and CDR as well as maintaining subsystem ICDs throughout both semesters. Each group was required to have a Team Lead, Science Lead, and a Lead for each subsystem who was responsible for ensuring that subsystem was complete and functional (though all group members were expected to contribute to all subsystems). These roles were decided on by the group. I was the group's Science Lead - responsible for ensuring our project's output actually answered our science question and was heavily involved with several of the subsystems where I helped to provide accurate input parameters for the Model and Simulation subsystems and reasonable tests for the simulation's accuracy. 

The second semester started with a Delta CDR, focusing on any changes that had occurred over winter break, and the rest of the semester was dedicated to actually doing the project. After setting up our computer, we iterated on our simulations, slowly ramping up the size and complexity as we found and fixed errors or other issues. 

As for the research itself, we used the simulation software *SeisSol* to study the feasability of using artificial impacts and seismometers to study the interior of the asteroid (16) Psyche. We created three simplified models of the asteroid, a homogeneous rocky model, a two layer rock and metal model, and a "blobby" rock and metal model. Our simulated impactor was based on the Small Carry-On Impactor (SCI) from JAXA's Hayabusa2 mission and we used the noise floor of the VBB on the Seismic Experiment for Interior Structure (SEIS) from NASA's InSight mission on Mars. 

<img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/psyche/homogeneous.png?raw=true" width="250" height="132"><img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/psyche/2_layer.png?raw=true" width="250" height="132">  
Homogeneous Model and 2-Layer Model  
<img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/psyche/blobby.png?raw=true" width="250" height="132">  
"Blobby" Model  

For the other inputs, we approximated the impact's seismic moment tensor as an explosion (see the Nishiyama et al. 2021 citation in the poster) which for us looks like: 

<img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/psyche/psycheese%20equations.png?raw=true" width="200" height="150">

We also had to estimate the sheer modulus and Lamé's First Parameter for the rock and metal materials in the models and used a binary search algorithm to find the time and normailization constant. There were some *fun* errors that were found and corrected as we worked, such as having the seismic efficiency being 8 orders of magntiude smaller than anything ever measured. It turns out that there were two issues causing this. First that we were including the seismic efficiency in our seismic moment tensor calculations as it was included in the original approximations. Fixing this helped, but the seismmi efficiency was still 3 orders of magnitude off. After several more simulations and experimenting with inputs, it turned out that because we had our simulated seismic source on the surface of the asteroid a large portion of the energy was being sent out into space instead of into the aseroid; the fix was to shrink the size of the source as small as we reasonably could and very slightly embed it inside the model. 

Our outputs included both animations to visualize the seismic waves traveling through the asteroid and seismograms (note, the animations are sped up 10 times):

<img src="https://github.com/semmons98/PsycheESE/blob/main/animations/homogeneous%20animation.gif?raw=true" width="300" height="233"><img src="https://github.com/semmons98/PsycheESE/blob/main/animations/2%20layer%20optimized%20animation.gif?raw=true" width="300" height="233">  
Homogeneous Model               2-Layer Model  
<img src="https://github.com/semmons98/PsycheESE/blob/main/animations/blobby%20optimized%20animation.gif?raw=true" width="300" height="233">  
"Blobby" Model  

<img src="https://github.com/semmons98/PsycheESE/blob/main/Data/Graphs/Homogeneous%20Model%2080%20Seconds.png?raw=true" width="400" height="241">  
<img src="https://github.com/semmons98/PsycheESE/blob/main/Data/Graphs/2-layer%20Model%2080%20Seconds.png?raw=true" width="400" height="241">  
<img src="https://github.com/semmons98/PsycheESE/blob/main/Data/Graphs/Blobby%20Model%2080%20Seconds.png?raw=true" width="400" height="241">  

In the end, we did determine that this would be possibly with current technology, but there were several limitation primarily relating to time constraints on the size of our simulations. For more detail, take a look at the poster and GitHub repository linked earlier, I have also included a Python script used to read the data output by the simulations on the Programming page of this website. 

### Crater Counting on Charon (2023)

Though for a class, this is arguably my first research project; taking place during my second semester at ASU when I took SES 123 *Earth, Solar System, and Universe; Lab*. The concept is fairly well explained by the title, I counted the craters on Pluto's largest moon Charon. As I was very inexperienced and did not know what kind of tools may exist for this task, I did it by hand, it was incredibly tedious but also kind of fun. My results confirmed existing hypothesis, that Charon has (or had relatively recently) some level of geologic activity - likely cryovolcanism - which resurfaces some parts of the surface. 

My process was to take the following mosaic of New Horizons images from the USGS astrogeology website and open it in photoshop. 

<img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/charon/Charon%20Surface.png?raw=true">

I then applied a grid over it that was scaled such that each square was approximately 32 square kilometers (not accounting for deformations due to the map projections). Then I went through each grid square and counted the number of visible craters - due to the resolution the smallest were approximately 1.5 kilometers in diameter. The number of craters in these grid squares could then be used for analysis and figures. The figures and images from this project are included below: 

<img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/charon/Charon%20Heat%20Map.png?raw=true">

This is a heat map showing the locations of the craters I counted. The white outlines are craters that overlapped more than one grid square, the black areas are those that were unable to be counted due to images either not existing or being too low resolution. Note that due to some error when saving the image, some of the grid lines are faint or invisible. 

<img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/charon/Charon%20Total%20Craters.png?raw=true" width="600" height="450"><img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/charon/Charon%20Northern%20Craters.png?raw=true" width="275" height="206"><img src="https://github.com/semmons98/semmons98.github.io/blob/main/photos/charon/Charon%20Southern%20Craters.png?raw=true" width="275" height="206">

These bar graphs show the number of craters and how they are distributed, open the images in a new tab to see them larger. An interesting detail is that the Northern Hemisphere, being better imaged, has nearly 4 times as many grid squares included than the Southern Hemisphere (1028 vs 262), despite this, I counted only 20 more craters in the Northern Hemisphere. 

## Astrobiology

### Diagnosing Life (2026)

This project was also completed for a class; SES 311 *Astrobiology*. It was the final project for the class and not just a group project, but one where the group was all the students in the class. The class was largely discussion based and this project came out of a debate on different ways of defining life - one student suggested that since it was so difficult to make a solid definition, what if we used a set of diagnostic criteria like the DSM used in psychology and mental health. Our professor, Dr. Sara Walker, decided to have us create these diagnostic criteria, apply them to a number of possible and/or disproven astrobiological life detections as case studies, and write a scientific paper-styled report on it as our final project. Each criterion and each case study had 2-3 students assigned to work on it (the criterion groups and case study groups were largely not the same), then we wrote the paper together. 

The sections I was assigned were "Life can Create" and the possible detection of DMS/DMDS on exoplanet K2-18b. In addition to my assigned sections, I also wrote the abstract and Appendix B and constributed to the Limitations and Next Steps section and the Conclusion, as well as handling much of the formatting, works cited, and some general editing. The details of the methodology and results can be found in the final paper <a href="{{ site.baseurl }}/pdfs/DiagnosingLife_FinalPaper.pdf" target="_blank">here (warning: 40 pages including appendix and references)</a>. Instead, I'm going to use this space to discuss how I would like to improve upon this project, as myself and several of the other more involved students agreed that we really liked the concept, but our execution needed significant work.

The biggest issue we agreed on was that there was a lot of overlap between the criteria, including my own. I think a lot of this comes from our limited timeframe - only about a month for the entire project - but also that we worked on each criterion in a small group with little overlap or communication between them until we tried to apply the codes and write the paper. The other students and I agreed that if we were to build upon or redo this project in the future, we would spend a lot more time unsuring the criteria are unique. 

Beyond just cleaning up the criteria/codes, one specific improvement I would implement would be to separate the criteria into two groups, one would work like the existing ones do, the other would be for things "that are strongly indicative of life’s presence when they are present, but are not found in all life..." (this paper, page 32). This group of criteria could be simple yes or no questions, a yes response indicates nearly certain detection of life, while a no just means we can move on to the next question or section. For example, "Do we detect a technosignature?" if yes, then we have (probably) found life, if no, then we move on to the other criteria since life can easily exist without technology. Another improvement would be to differentiate between answers of "no" and "don't know" for criteria. In other words, some way to quantify the uncertainty in the output. There are two possible ways to go about this described in the Limitations and Next Steps section of the paper. 

In all, I think these would dramatically improve the reliability and consistency of the results, that being said, the current version still does an exellent job of showing how little information we have to verify if a potential biosignature is actually evifence of life, assuming of course that the biosignature detection itself can be verified. 
