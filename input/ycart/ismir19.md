title: Blending Acoustic and Language Model Predictions for Automatic Music Transcription
-------------------------------------

<h2>
Adrien Ycart, Andrew McLeod, Emmanouil Benetos and Kazuyoshi Yoshii - <i>ISMIR 2019</i>
</h2>

<h3>
Presentation
</h3>

<p>
On this page can be found the supplementary material for:<br>
Adrien Ycart, Andrew McLeod, Emmanouil Benetos and Kazuyoshi Yoshii.
  "Blending Acoustic and Language Model Predictions for Automatic Music Transcription"
  <i>20th International Society for Music Information Retrieval Conference (ISMIR), </i>
  November 2019, Delft, Netherlands.</li>
</p>

<h3>
Code
</h3>

<p>
The code to reproduce the experiments presented in the paper can be found at this address:
<a href=https://github.com/adrienycart/MLM_decoding> https://github.com/adrienycart/MLM_decoding </a>
</p>

<h3>
Examples of results
</h3>

<p>
Here, we propose selected examples to illustrate our model's performance: one where our model is successful, one where it fails.
In both cases, we display a figure comparing:
<ul>
	<li> The ground truth
	<li> The transcription obtained by thresholding the posteriogram at 0.5
	<li> The transcription obtained with HMM smoothing
	<li> The transcription obtained with our system in PM+S configuration
	<li> The posteriogram 
	<li> The predictions made by the language model
</ul>
</p>

<p>
All comparisons are shown using a 16th-note timestep, hence the varying number of frames in both examples. The images can be displayed full size by using right-clicking the image and selecting "Open image in new tab".
</p>
<p>
We also propose the ground truth, thresholded posteriogram, HMM-smoothed posteriogram and PM+S transcriptions converted to MIDI format (<a href="ycart/data/ismir19/ismir19_examples_MIDI.zip"> download all MIDI files here</a>).
</p>


<h4>
Successful example
</h4>

<img src="ycart/data/ismir19/good_comparison.png" alt="Good Comparison" width="2000" class="center">

<p>
Here, our model manages to successfully detect the short notes around frame 250, while the other two baseline models do not.
This is mostly due to our language model: the MLM predictions show that it is able to recognise that pattern of short, repeated notes.
</p>

<h4>
Unsuccessful example
</h4>

<img src="ycart/data/ismir19/bad_comparison.png" alt="Bad Comparison" width="2000" class="center">

<p>
Here, our model does not improve much compared to the other two baseline models.
If anything, it over-fragments notes, (e.g. around frame 80), and even adds some false positives (e.g. around frame 160).
We can see that the MLM predictions are very blurry, failing to predict any note with confidence.
</p>

