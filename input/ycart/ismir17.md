title: A Study on LSTM Networks for Polyphonic Music Sequence Modelling
-------------------------------------

<h2>
Adrien Ycart and Emmanouil Benetos - <i>ISMIR 2017</i>
</h2>

<h3>
Presentation
</h3>

<p>
In this page can be found all the data and code necessary to reproduce the experiments described in :<br>
Adrien Ycart and Emmanouil Benetos.
  <a href="https://ismir2017.smcnus.org/wp-content/uploads/2017/10/60_Paper.pdf">
  “A Study on LSTM Networks for Polyphonic Music Sequence Modelling”</a>
  <i>18th International Society for Music Information Retrieval Conference (ISMIR), </i>
  October 2017, Suzhou, China.</li>
</p>

<h3>
Download
</h3>
<p>
The code can be downloaded <a href="https://code.soundsoftware.ac.uk/projects/ismir17-code">here</a> (under the "Files" tab).
</p>

<h3>
External dependencies
</h3>

<p>
This code was implemented in Python 2.7.
It uses the following libraries :
<ul>
<li> <b>Tensorflow</b> : version 1.0.0
<li> <b>Numpy</b> : version 1.12.0
<li> <b>PrettyMIDI</b> : version 0.2.7
</ul>


</p>

<h3>
Code Organisation
</h3>

<p>
The datasets can be found in the 'data/' folder, split in train, valid and test
subsets.
<ul>
<li><b>dataset.py</b> holds functions relative to the loading and manipulation of
the dataset
<li><b>model.py</b> holds functions defining the model, as well as the training
process.
<li><b>eval_utils.py</b> holds function to compute the evaluation metrics of a given model.
<li><b>display_utils.py</b> holds functions to display some MIDI files and some predictions.
<li><b>script_train_rnn.py</b> is a script allowing to train several models.
<li><b>script_get_measures.py</b> is a script allowing, once some model are trained,
to compute the best threshold on the validation dataset, and use that threshold
to compute the evaluation metrics on the test dataset.
<li><b>script_display_prediction.py</b> is a script allowing, once some model are trained,
to visualise the predictions made by these models with a given MIDI file.
</ul>
</p>
<h3>
Data Saving
</h3>
<p>
For most training and loading functions, you are asked a "base_path".
This variable allows to specify a base path, characterising the current experiment.
Inside that folder, some subfolders will be created for each
(n_hidden,learning_rate) configuration.
When running the training script, the checkpoint files are saved in the folder
'ckpt/', and the summary files are saved in 'summ/'
</p>
<p>
<b>Example :</b> <br>
I run an experiment comparing models with n_hiddens = [128, 256] and
learning_rates = [0.001, 0.01], on the Synth dataset, with quantised timesteps.<br>
I choose as a base_path : 'synth/quantised/'.<br>
The checkpoint files for the model (128,0.01) will be found in :
'ckpt/synth/quantised/128_0.01/'<br>
The summary files for this same model will be found in :
'summ/synth/quantised/128_0.01/'<br>
</p>

<h3>
Known Issues
</h3>
<p>
This was some preliminary code, there were some mistakes that were only spotted
after the submission. They were kept
for the sake of reproducibility.
The user is free to fix them, if they are willing to.
</p>
<p>
Among the known issues are :
<ul>
<li> The dataset is not shuffled between epochs.
<li> When computed with Tensorflow and not Numpy, the evaluation metrics sometimes
output NaN : this is due to the fact that the denominator is negative, and can
easily be fixed by adding a small float value to the denominator.
<li> The function _run_by_batch only works with cross_entropy, not with prediction.
<li> The length of each sequence is not provided as argument to the dynamic_rnn.
<li> When performing data augmentation, all datasets are augmented, while only
the training dataset should be.
</ul>
If there were any other issues, please contact the author.
</p>
