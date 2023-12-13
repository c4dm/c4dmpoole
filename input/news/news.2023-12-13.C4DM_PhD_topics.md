title: Centre for Digital Music PhD topics for 2024

-------------------

Please find below outline PhD topics offered by academics in the Centre for Digital Music for 2024 start. Candidates are invited to contact the relevant academic by email to elaborate on what the research will entail. In several cases, there is a significant opportunity to jointly shape the direction of research. 

Opportunities include internally and externally funded positions for PhD projects to start in Autumn 2024, with one position starting in Spring 2024. It is also possible to apply as a self-funded student or with funding from another source. Studentship opportunities include: 

* One PhD studentship at the [Centre for Doctoral Training in AI and Music](https://www.aim.qmul.ac.uk/apply/) (home students, Spring 2024 start) 

* [S&E Doctoral Research Studentships for Underrepresented Groups](http://eecs.qmul.ac.uk/phd/phd-studentships/se-doctoral-research-studentships-202425-for-underrepresented-groups/) (home students, Autumn 2024 start, 4 positions funded across the Faculty of Science & Engineering) 

* [CSC PhD Studentships in Electronic Engineering and Computer Science](http://eecs.qmul.ac.uk/phd/phd-studentships/csc-phd-studentships-in-electronic-engineering-and-computer-science/) (Autumn 2024 start, two positions allocated for the Centre for Digital Music) 

* [CONACyT Scholarships](https://www.qmul.ac.uk/scholarships/items/conacyt-scholarships.html) (Autumn 2024 start) 

<hr>

**Model-based Deep Learning for Audio**

Supervisor: [Mark Sandler](mailto:mark.sandler@qmul.ac.uk)

Most of today’s Deep Learning models learn from data. In many tasks and applications, there are pre-existing deterministic models that already do a very good job. This includes for example, the synthesis of acoustic musical instruments, for which excellent physical models of resonators have been developed over many decades. Yet, these deterministic models are not perfect because they fail to capture the individual and nuanced effects of, say, the way the wood in a violin body affects the timbre. Model based Deep Learning brings together the best of data-driven Deep Learning and existing, domain-knowledge-based modelling. This PhD will examine this paradigm in one or more of the following application domains: drum synthesis, plucked or hammered string synthesis, room acoustic modeling, harmonic analysis (key and chord) and others that the candidate is invited to suggest. It is expected that the advantages include reducing the size of training data sets, faster training and smaller, more computationally efficient models. Note that the models themselves can be derived from data, using techniques like Dynamic Mode Decomposition [2] (e.g. for source separation) or Sparse Identification of Non-linear Dynamics (SINDy) [3] (e.g. for musical instrument modelling). 

[1] N. Shlezinger, J. Whang, Y. C. Eldar and A. G. Dimakis, "Model-Based Deep Learning," in Proceedings of the IEEE, vol. 111, no. 5, pp. 465-499, May 2023, doi: 10.1109/JPROC.2023.3247480.  

[2] J.N. Kutz, X. Fu, and S.L. Brunton, "Multi-resolution dynamic mode decomposition." arXiv:1506.00564(2015). 

[3] Kadierdan Kaheman, J. Nathan Kutz and Steven L. Brunton, “SINDy-PI: a robust algorithm for parallel implicit sparse identification of nonlinear dynamics”, Proc. R. Soc. A.4762020027920200279 https://doi.org/10.1098/rspa.2020.0279 

<hr>

**Explainable AI by applying Linear Algebra to the Understanding Neural Audio**

Supervisor: [Mark Sandler](mailto:mark.sandler@qmul.ac.uk)

At its heart, Deep Learning relies on Linear Algebra. For example, in a fully connected layer, the core operation is an Affine Transform, ie a Matix/Vector Multiplication with a Vector Addition. During training the matrix of weights is altered, epoch by epoch and the network processes the input such that the output more closely approximates the ground truth. This project will explore the use of Linear Algebra theory to examine how Deep Learning learns, ie how the weight matrices change during learning in the framework of an important Neural Audio application domain. The specific domain of application will be selected via dialogue between the candidate and the supervisor and might include source separation, neural synthesis and harmonic analysis. This will lead to greater understanding and interpretability of Deep Learning, and more efficient models. 

[1] Paul, Vlad S., and Philip A. Nelson. ‘Matrix Analysis for Fast Learning of Neural Networks with Application to the Classification of Acoustic Spectra’. The Journal of the Acoustical Society of America 149, no. 6 (June 2021): 4119–33. https://doi.org/10.1121/10.0005126.  

[2] Bermeitinger, Bernhard, Tomas Hrycej, and Siegfried Handschuh. ‘Singular Value Decomposition and Neural Networks’, 27 June 2019. https://doi.org/10.1007/978 3 030 30484 3_13 

[3] Martin, Charles H., Tongsu (Serena) Peng, and Michael W. Mahoney. ‘Predicting Trends in the Quality of State-of-the-Art Neural Networks without Access to Training or Testing Data’. Nature Communications 12, no. 1 (5 July 2021): 4122. https://doi.org/10.1038/s41467-021-24025-8.  

<hr>

**Modelling the Transmission and Development of Musical Styles and Ideas**

Supervisor: [Simon Dixon](mailto:s.e.dixon@qmul.ac.uk)

Large-scale automatic analysis of features from music databases allows us to study relationships between pieces across time and location, and to trace how musical ideas and styles spread, grow and develop. At one level, this provides evidence of influence between musicians or composers, which can be seen in imitation of patterns and styles. At another level, it could facilitate the linking of external events in the surrounding culture to developments in the music of that culture. Recent work has led to the annotation of a growing corpus of jazz recordings for performing research on this topic. Applicants are invited to develop the ideas from this line of work and propose a PhD project that aligns with their interests and knowledge. The project could involve enabling technologies such as transcription, instrument identification, performer style modelling, or modelling networks of influence. 

<hr>

**Combining Deep Learning and Music Theory**

Supervisor: [Simon Dixon](mailto:s.e.dixon@qmul.ac.uk)

Deep learning has significantly boosted the accuracy of analytic and generative music models, providing a powerful framework for extracting knowledge from data. However, the paradigm shift from feature-engineering and logic to latent spaces and trainable operations comes at the cost of interpretability and expressive power. We invite you to submit a project proposal for a PhD exploring the combination of deep learning and the rich body of prior knowledge that we can derive from music theory. We imagine that prior knowledge can be used to complement or constrain the kind of patterns that are learnable, leading to more interpretable models and lower data requirements. Depending on your interests, you might choose to focus on analytic or generative models in the audio or symbolic music domain.

<hr>

**Explainable AI for Sound Scene Analysis**

Supervisors: [Lin Wang](mailto:lin.wang@qmul.ac.uk) and [Emmanouil Benetos](mailto:emmanouil.benetos@qmul.ac.uk)

Deep-learning models have revolutionized state-of-the-art technologies for environmental sound recognition motivated by their applications in healthcare, smart homes, or ambient assisted living. However, most of the systems used for these applications are based on black boxes and, therefore, cannot be interpreted, i.e. the rationale behind their decisions is unknown. Despite remarkable advances in the model performance , the research in explainable machine learning in the audio domain is still limited. The PhD topic aims to fill this gap. Applicants are invited to develop ideas to reduce this gap by proposing explainable deep-learning models for automatic sound event detection and classification in real-life environments. 

<hr>

**Deep Audio Inpainting for Musical Signals**

Supervisor: [Lin Wang](mailto:lin.wang@qmul.ac.uk)

Real-life audio signals often suffer from local degradation and lost information. Examples include short audio intervals corrupted by impulse noise and clicks, or a clip of audio wiped out due to damaged digital media or packet loss in audio transmission. Audio inpainting is a class of techniques that aims to restore lost information with newly generated samples without introducing audible artifacts. In addition to digital restoration, audio inpainting also finds wide applications in audio editing (e.g. noise removal in live music recording) and music enhancement (e.g. audio bandwidth extension and super-resolution). Recently, intrigued by the tremendous success in image and video inpainting, deep learning-based approaches started attracting attention in the research community, but still in the infant stage. Applicants are invited to develop ideas to investigate the possibility of adapting deep learning frameworks from various domains inclusive of audio synthesis and image inpainting for audio inpainting. 

<hr>

**Resource-efficient machine learning for music**

Supervisor: [Emmanouil Benetos](mailto:emmanouil.benetos@qmul.ac.uk)

State-of-the-art models for music information research are often very hard to run on small and embedded devices such as mobile phones, single-board computers, and other microprocessors. At the same time, the computational cost, footprint, and environmental impact for building and deploying deep learning models for making sense of music data is constantly increasing. This PhD project will investigate methods for creating resource-efficient models for music understanding, applied to various tasks in music information research that involve music audio data, such as automatic music transcription, audio fingerprinting, or music tagging. Methods to be investigated can include but are not limited to sparse training, network pruning, binary neural networks, post-training inference, and knowledge distillation. The successful candidate will investigate, propose and develop novel machine learning methods and software tools for resource-efficient music understanding, and will apply them to address tasks of their choice within the wider field of music information research. This will result in models that can be deployed on small or embedded devices, or on offline models where learning and inference times and computational resources are drastically reduced. 

<hr>

**Timbre tools for the digital instrument maker**

Supervisor: [Charalampos Saitis](mailto:c.saitis@qmul.ac.uk)

This PhD addresses the role of timbre in the design of sound synthesis and AI tools for digital instrument makers. The traditional luthier will select rosewood to create a dark and complex guitar sound. The analog synth designer may choose optical components for crafting warm tones. Yet timbre is conspicuously absent from the digital luthier’s toolbox. Making digital musical instruments (DMIs) is still based on concepts from early analog and digital synthesis, and relies on classical tools like oscilloscopes and signal generators. This project will seek to shift this perspective of DMI design to a more sound-based, timbre-first practice.  

What is a ‘timbre tool?’ It supports the timbral design of DMIs. It is a tool for makers, not for musicians (who are not makers) and audiences. It can be about sensor design and fabrication, interfacing between the physical and digital worlds, or enabling expressive control at multiple levels of meaningful abstraction. Machine learning and AI provide interesting opportunities to interface with sound via timbre and can be a point of entry for creating a timbre tool. SP-Tools and the FluCoMa Toolkit are good examples, as are approaches to interactive exploration of latent space in neural audio synthesis. 

The premise of this project is to promote a learn-by-making approach: through creating digital instruments using flexible, open-ended tools for timbral design, amongst other tools, people can learn about sound synthesis, become more aware of timbre phenomena, and craft compelling new instruments. 

<hr>

**Intelligent audio production for the hearing impaired**

Supervisor: [Josh Reiss](mailto:joshua.reiss@qmul.ac.uk)

This project will explore new approaches to audio production to address hearing loss, a growing concern with an aging population. The overall goal is to investigate, implement and validate original strategies for mixing audio content such that it can be delivered with improved perceptual quality for hearing impaired people. 

Music content is typically recorded as multitracks, with different sound sources on different tracks. Similarly, soundtracks for television and radio content typically have dialogue, sound effects and music mixed together with normal-hearing listeners in mind. But a hearing impairment may result in this final mix sounding muddy and cluttered. The research team here have made strong advances on simulating hearing loss, understanding how to mix for hearing loss, and attempting to automatically deliver enhanced mixes for hearing loss. But these initial steps identified many unresolved issues and challenges. Why do hearing loss simulators differ from real world hearing loss, and how can this be corrected? How should hearing loss simulators be evaluated and how should they be used in the music production process.? What is the best approach to mix audio content to address hearing loss? These questions will be investigated in this project. 

<hr>

**Machine learning of physical models**

Supervisor: [Josh Reiss](mailto:joshua.reiss@qmul.ac.uk)

Physical models of sound generating phenomena are widely used in digital musical instruments, noise and vibration modelling, and sound effects. They can be incredibly high quality, but they also often have a large number of free parameters that may not be specified just from an understanding of the phenomenon.  

Machine learning from sample libraries could be the key to improving the physical models and speeding up the design process. Not only can optimisation approaches be used to select parameter values such that the output of the model matches samples, the accuracy of such an approach will give us insight into the limitations of a model. It also provides the opportunity to explore the overall performance of different physical modelling approaches, and to find out whether a model can be generalised to cover a large number of sounds, with a relatively small number of exposed parameters. 

This work will explore such approaches. It will build on recent high impact research from the team in relation to optimisation of sound effect synthesis models. Existing physical models will be used, with parameter optimisation based on gradient descent. Performance will be compared against recent neural synthesis approaches, that often provide high quality synthesis but lack a physical basis. It will also seek to measure the extent to which entire sample libraries could be replaced by a small number of physical models with parameters set to match the samples in the library. 

The student will have the opportunity to work closely with research engineers from the start-up company Nemisindo, though will also have the freedom to take the work in promising new directions. Publishing research in high impact venues will be encouraged. 

  

Industry involvement: 

This is affiliated with Nemisindo Ltd., an SME spunout from QMUL and based on C4DM research. Nemisindo will provide in-kind support with an estimated value of £50k. This includes access to engineers, data sets and source code, placement or internship. Travel costs would be covered. 

<hr>

**Incorporating hierarchical structure into automatic music labelling**

Supervisor: [Johan Pauwels](mailto:j.pauwels@qmul.ac.uk)

Hierarchies are omnipresent in music labels. For example, consider a 4-note chord, which can be reduced to its 3 most important notes or extended to a number of 5-note chords. Likewise, a time signature tells us both the number of beats per measure (2, 3, 4) and the way beats are subdivided (into 2 or 3 parts). Since many approaches to automatic music labelling consist of training a deep learning classifier, it makes intuitive sense to use a hierarchy of classes instead of a single flat level. Otherwise the separation between all classes will be considered equally important, which is clearly not the case for hierarchical labels. Nonetheless, flat classification has been the default approach up to now. However, new techniques have been proven promising in the context of musical instrument and everyday sound recognition. The aim of this PhD project is to explore how existing hierarchical classification techniques can be adapted to specific music labelling tasks and to develop new techniques. The proposed labelling tasks are chord recognition and time signature determination, but these can be adapted to suit the candidate’s interests. 

The ideal candidate has an interest in the latest deep learning techniques, but is willing to fall back on classical machine learning to create strong baselines or if the situation otherwise requires so. An amateur-level understanding of music theory is useful, but should not hold you back from applying since it can be easily learnt if motivated. 

<hr>

**Deep Learning for efficient personal HRTF acquisition**

Supervisor: [Johan Pauwels](mailto:j.pauwels@qmul.ac.uk)

Head-Related Transfer Functions (HRTFs) store the filtering effect your head and ears have on incoming sound, which allows us to perceive direction. Because of physiological differences, HRTFs are specific to each individual, and can be considered as your personal configuration file that allows the best possible playback of virtual audio sources. Using a personalised HRTF, as opposed to a generic one, improves sound localisation and immersion for communication, healthcare, music and gaming AR/VR applications. Measuring one’s personal HRTF, however, requires a dedicated lab setup as well as time, which makes it impossible to do for a large population. This project aims to use deep learning to synthesise HRTFs from a variety of multimodal, easy to acquire sensor data such as images or 3D models. Several deep learning techniques can be explored, from CNNs to GANs to graph neural networks, depending on your personal interests. 





(<i>13 Dec 2023</i>)
