
title: Polyphonic Music Sequence Transduction with Meter-Constrained LSTM Networks
--------------------------------------

  <h2> Adrien Ycart and Emmanouil Benetos - ICASSP 2018 </h2>

  <h3> Presentation </h3>


  <p>
    In this page can be found all the data and code necessary to reproduce the experiments described in :<br>
    Adrien Ycart and Emmanouil Benetos.
     "Polyphonic Music Sequence Transduction with Meter-Constrained LSTM Networks"
      <i>IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), </i>
      April 2018, Calgary, Canada.
  </p>

  <h3>
Download
</h3>

<font color="red">
<h4>NOTICE:</h4>

The correspondance tables given here should only be used to reproduce the results
in the paper.
They have been replaced by the newer, more complete <a href='http://c4dm.eecs.qmul.ac.uk/ycart/a-maps.html'> A-MAPS dataset</a>.
Please use the A-MAPS dataset if you'd like to use beat annotations for MAPS.
</font>


<p>
  <ul>
    <li> All the data needed to reproduce the experiments
      can be found <a href='http://c4dm.eecs.qmul.ac.uk/datasets/ycart/icassp18/icassp18_data.zip'> here. </a>
      It contains:
      <ul>
        <li> the MAPS MIDI files
        <li> the MAPS posteriograms in CSV format
        <li> the baseline piano-rolls (obtained by median-filtering and thresholding the posteriograms) in CSV format
        <li> the correspondence tables as text files.

      </ul>
    <li> The correspondence tables can be found <a href='http://c4dm.eecs.qmul.ac.uk/datasets/ycart/icassp18/MAPS_corresp_dataset.zip'> here. </a>
      It contains the correspondence tables alone in CSV format, and in the form of a Pickle file.
    <li> The code can be found <a href='http://c4dm.eecs.qmul.ac.uk/datasets/ycart/icassp18/icassp18_code.zip'> here. </a>

  </ul>
</p>

<h3>
MAPS Correspondence Tables Dataset
</h3>
<h4>
Content
</h4>
<p>
The ZIP file contains, for each MIDI file in the MAPS dataset
for which rhythmic ground truth was available,
its rhythm correspondence table in the form of a CSV file.
Each CSV has two columns.
The first one corresponds to the times in seconds.
The second one corresponds to the metrical position, expressed in quarter notes.
The note resolution is a sixteenth note, so the metrical position is a multiple of 0.25.
It has to be noted that a quarter note doesn't always corresponds to a beat: if the meter of the piece is ternary, a beat will correspond to 1.5 quarter notes.
</p>
<p>
The ZIP file also contains the same dataset, directly provided as a Pickle file to be imported in Python. It contains a dictionary where each key is the file name, and each value is a Numpy table of shape [N, 2] where N is the number of sixteenth notes.
</p>

<h4>
Alignment method
</h4>
<p> This dataset was obtained by matching and aligning the MAPS MIDI files with
the <a href="http://piano-midi.de/"> Piano-Midi.de</a> dataset,
that contains the rhythmic ground truth.
The files were aligned using the system described in:<br>

Eita Nakamura, Kazuyoshi Yoshii and Haruhiro Katayose, "Performance error detection and post-processing for fast and accurate symbolic music alignment",  in
<i> 18th International Society for Music Information Retrieval Conference (ISMIR)</i>, 2017.
<br>
The system is available for download <a href="https://midialignment.github.io/demo.html"> here. </a>
</p>
<h4>
Lost data
</h4>
<p>
In some cases, the alignment failed. Most of the time, we were able to manually edit the files to make the alignment work,  while keeping the rhythmic information. Nevertheless, some data was lost in the process.
<ul>
<li>One file was duplicated, we removed the duplicate: MAPS_MUS-chpn-p11-format0_AkPnCGdD.mid / MAPS_MUS-chpn-p11_AkPnCGdD.mid
<li>One piece could not be found in the Piano-Midi.de dataset, it  was present in 3 versions in the MAPS dataset:
MAPS_MUS-chpn-e01_ENSTDkCl.mid,
MAPS_MUS-chpn-e01_SptkBGAm.mid,
MAPS_MUS-chpn-e01_StbgTGd2.mid
<li>One piece actually contained two pieces, we kept only the first one (cut after 36.5 seconds): MAPS_MUS-scn15_5_SptkBGCl.mid
<li> For one piece, the alignment failed at some point. We only kept the first part where the alignment succeeded (cut after 209.75 seconds). This corresponds to 4 files :
MAPS_MUS-liz_et6_StbgTGd2.mid,
MAPS_MUS-liz_et6_ENSTDkCl.mid,
MAPS_MUS-liz_et6_AkPnCGdD.mid,
MAPS_MUS-liz_et6_AkPnBsdf.mid
</ul>
</p>

<h3>
Code
</h3>

<h4>
External dependencies
</h4>

<p>
This code was implemented in Python 2.7.
It uses the following libraries :
<ul>
<li> <b>Tensorflow</b> : version 1.0.0
<li> <b>Numpy</b> : version 1.14.0
<li> <b>PrettyMIDI</b> : version 0.2.6
</ul>


</p>

<h4>
Code Organisation
</h4>

<p>
<ul>
<li><b>dataMaps.py</b> holds the class representing one training example. It corresponds to a couple input-target.
<li><b>datasetMaps.py</b> holds functions relative to the loading and manipulation of
the dataset as a whole (manipulates DataMaps objects)
<li><b>modelMaps.py</b> holds functions defining the model, as well as the training
process.
<li><b>eval_utils.py</b> holds function to compute the evaluation metrics of a given model.
<li><b>display_utils.py</b> holds functions to display some MIDI files and some predictions.
<li><b>utils.py</b> holds some utility functions.
<li><b>script_train_rnn.py</b> is a script allowing to train several models.
<li><b>script_get_measures.py</b> is a script allowing, once some model are trained,
to compute the best threshold on the validation dataset, and use that threshold
to compute the evaluation metrics on the test dataset.
</ul>
</p>

<p>
For any feedback, comments, or issues, do not hesitate to contact the author.
</p>
