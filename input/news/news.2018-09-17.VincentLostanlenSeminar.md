
title: Vincent Lostanlen
-----------------


**QMUL School of Electronic Engineering and Computer Science**

**Centre for Digital Music Seminar Series**

** Lecture by Vincent Lostanlen, NYU
**

**Date/time: 3pm-4pm, Monday, 17th September 2018**

**Location: GC (Graduate Centre) 2.22**

Open to academics, students, alumni, public; all welcome. 
Admission is FREE, no pre-booking required.


Abstract: 
Convolutional operators in the time-frequency domain: what makes music 
special?

The past decade has witnessed a breakthrough of deep convolutional 
networks (convnets) in computer vision. Yet, in order to adapt these 
architectures to audio classification tasks, it rarely suffices to 
replace 2-d convolutions over the spatial coordinates of the image by 
1-d convolutions over the temporal axis of the raw waveform. Instead, 
most convnets for automatic speech recognition (ASR), as well as 
detection and classification of acoustic scenes and events (DCASE), are 
trained on a 2-d representation of acoustic energy in the 
time-frequency, such as the pointwise logarithm of mel-frequency 
spectrogram (logmelspec). Such an association between logmelspec and 
convnet is progressively becoming the default baseline in bioacoustic 
classification, as once were MFCC-GMM-HMM pipelines. However, music 
information retrieval (MIR) has not benefited from the same steady 
progress: in long-lasting challenges such as automatic chord recognition 
or musical instrument classification, logmelspec-convnets only perform 
marginally better than shallower architectures, even in the large data 
regime.
In this talk, I will argue that a major obstacle to the applicability of 
convnets in MIR, above the lack of large-scale annotated datasets, is 
the inadequacy of 2-d spectrotemporal receptive fields for modeling some 
of the essential attributes of music perception: pitch, harmony, tempo, 
and meter. In particular, octave equivalence -- that is, the cognitive 
wrapping of a continuous frequency axis onto a spiral which makes a full 
turn at every octave  -- is too often addressed merely as a spurious 
factor of intra-class in music signal analysis, rather than a resource 
for improving sparsity and reducing statistical overfitting in learned 
representations.
After reviewing some of the most compelling arguments in favor of octave 
equivalence (from music theory, ethnomusicology, auditory neuroscience, 
and unsupervised learning), I will address the question of building 
convolutional operators in the time-frequency domain that disentangle 
temporal variations in pitch chroma from variations in pitch height. 
  spiral scattering transform (Lostanlen, DAF-x 2015) and spiral 
convolutional networks (Lostanlen, DAF-x 2016). While the former enjoys 
a better theoretical interpretability, in terms of linearization of 
velocity parameters in the harmonic source-filter model, the latter can 
be readily integrated into an end-to-end learning pipeline for 
multipitch estimation in polyphonic music signals. Then, I will discuss 
future research directions, at the intersection of graph signal 
processing and the neo-Riemannian music theory: diagonalizing the 
Laplacian operator of the Tonnetz graph yields a basis of so-called 
"eigenprogressions" (Lostanlen, ISMIR-LBD 2018), i.e. Fourier-like atoms 
in the chord space of major and minor triads that are informative of 
harmonic similarity while being invariant to musical key, thus leading 
to state-of-the-art results in a task of supervised composer recognition 
from symbolic music data.cot2017/). 
His most recent projects involve the design and evaluation of systems to support 1) therapeutic gait training 
using Rhythmic Auditory Stimulation (RAS), 2) auditory training and second language learning.
